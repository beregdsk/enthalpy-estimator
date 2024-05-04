from enthalpy_estimator import mol_template

import argparse
import json
import ast
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('file', type=str)
args = parser.parse_args()

config = {}
with open(args.file, 'r') as f:
    for line in f:
        split = [s.strip() for s in line.split(':')]
        config[split[0]] = split[1]
        
os.chdir(os.path.dirname(os.path.abspath(args.file)))

if config['method'] == 'gen':
    from enthalpy_estimator.generator import ReactionGenerator as method
elif config['method'] == 'est':
    from enthalpy_estimator.single_reaction import EnthaplyEstimator as method
else:
    print('Unknown method')
    quit()

with open(config['reference'], 'r') as f:
    reference = json.load(f)

target = mol_template(config['xyz'],
                  config['energy'],
                  config['td'],
                  smiles=config['smiles'] if 'smiles' in config else None)

if target['smiles'] is not None:
    from enthalpy_estimator.smiles_vectorizer import SMILESVectorizer as vectorizer
else: 
    from enthalpy_estimator.simple_vectorizer import MolVectorizer as vectorizer

est = method(target, reference, vectorizer, ast.literal_eval(config['iso']) if 'iso' in config else False)
print(est.run(*(ast.literal_eval(c) for c in config['args'].split())))
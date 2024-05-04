from enthalpy_estimator import mol_template
from enthalpy_estimator.single_reaction import EnthaplyEstimator

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('xyz', type=str)
parser.add_argument('energy', type=str)
parser.add_argument('td', type=str)
parser.add_argument('-r', '--reference', type=str, default='reference.json')
parser.add_argument('-i', '--iso', action=argparse.BooleanOptionalAction)
parser.add_argument('-m', '--minimize', action=argparse.BooleanOptionalAction)
parser.add_argument('-o', '--optimize', action=argparse.BooleanOptionalAction)
parser.add_argument('-t', '--threshold', type=float, default=0.5)
parser.add_argument('-s', '--smiles', type=str)
args = parser.parse_args()

with open(args.reference, 'r') as f:
    reference = json.load(f)

target = mol_template(args.xyz,
                  args.energy,
                  args.td,
                  smiles=args.smiles)

if args.smiles is not None:
    from enthalpy_estimator.smiles_vectorizer import SMILESVectorizer as vectorizer
else: 
    from enthalpy_estimator.simple_vectorizer import MolVectorizer as vectorizer

gen = EnthaplyEstimator(target, reference, vectorizer, args.iso)
print(gen.run(args.optimize, args.minimize, args.threshold))
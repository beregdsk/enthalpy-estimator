from enthalpy_estimator import mol_template
from enthalpy_estimator.generator import ReactionGenerator

import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('xyz', type=str)
parser.add_argument('energy', type=str)
parser.add_argument('td', type=str)
parser.add_argument('-r', '--reference', type=str, default='reference.json')
parser.add_argument('-i', '--iso', action=argparse.BooleanOptionalAction)
parser.add_argument('-n', '--maxn', type=int, default=1000)
parser.add_argument('-s', '--smiles', type=str)
parser.add_argument('-o', '--output', type=str)
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

gen = ReactionGenerator(target, reference, vectorizer, args.iso)
gen.run(args.output if args.output is not None else './out/', args.maxn)
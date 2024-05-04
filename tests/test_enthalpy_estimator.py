from enthalpy_estimator import mol_template
from enthalpy_estimator.generator import ReactionGenerator
from enthalpy_estimator.single_reaction import EnthalpyEstimator
from enthalpy_estimator.simple_vectorizer import MolVectorizer
from enthalpy_estimator.smiles_vectorizer import SMILESVectorizer

import json

with open('reference.json', 'r') as f:
    reference = json.load(f)

target = mol_template('./data/m1_00_53-70-3_C22H14_wB97XD.xyz',
                  './data/m1_00_53-70-3_C22H14_wB97XD_ccsdt_cc-pvqz_ecp.txt',
                  './data/m1_00_53-70-3_C22H14_wB97XD.td',
                  smiles='C1=CC=C2C(=C1)C=CC3=CC4=C(C=CC5=CC=CC=C54)C=C32')
gen = ReactionGenerator(target, reference, SMILESVectorizer, True)
gen.run()

est = EnthalpyEstimator(target, reference, MolVectorizer, False)
print(est.run(True, True))
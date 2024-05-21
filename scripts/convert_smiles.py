import reference

import os
from openbabel import pybel
from rdkit import Chem
from rdkit.Chem import AllChem

from enthalpy_estimator import mol_template
reference2 = []

def cleanup_xyz(filename):
        with open(filename, 'r') as f:
            ind = f.readlines()
            
            if ' ' in ind[0]:
                n_atoms = str(len(ind))
                ind = [n_atoms + '\n\n'] + ind
                
            text = ''.join(ind)
            
        with open(filename, 'w') as f:
            f.writelines(text)
        
        return text

for r in reference.reference:
    ref = mol_template(
        f'./data/{r}wB97XD.xyz',
        f'./data/{r}wB97XD_ccsdt_cc-pvqz_ecp.txt',
        f'./data/{r}wB97XD.td',
        reference.name[r],
        '',
        reference.reference[r][0],
        reference.reference[r][1]
    )

    path = ref['xyz'].replace('.xyz','.mol')
    if not os.path.exists(path):
        mol = pybel.readstring('xyz', cleanup_xyz(ref['xyz']))
        mol.write('mol', path)
        
    ref['smiles'] = Chem.MolToSmiles(Chem.MolFromMolFile(path))
    reference2.append(ref)
    
import json
with open("reference.json", "w") as outfile: 
    json.dump(reference2, outfile, indent=4)
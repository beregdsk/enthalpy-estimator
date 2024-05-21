import reference

from enthalpy_estimator import mol_template
reference2 = []
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
    reference2.append(ref)
    
import json
with open("reference.json", "w") as outfile: 
    json.dump(reference2, outfile, indent=4)
import os
import sys

path = sys.argv[1]

for root, dirs, files in os.walk(path):
    for f_name in files:
        if f_name.endswith('.out'):
            with open(os.path.join(root, f_name.replace('.out','.txt')), 'w') as out, open(os.path.join(root, f_name), 'r') as f:
                for line in f:
                    if 'FINAL SINGLE' in line:
                        out.write('E='+line.split()[-1])
                        break

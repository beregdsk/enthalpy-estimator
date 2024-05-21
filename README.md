#Installation
'''
pip install enthalpy_estimator
'''
#Usage
The `scripts` folder includes examples of scripts used to run the calculations.
They utilize the 'reference.json' file which contains information information about the reference species.
'gen_script.py' and 'est_script.py' are command line scripts that that utilize the first (generator) and the second (estimator) method respectively:
The main way to run calculations is the 'run_file.py' script that reads the specified input file:
'''
python run_file.py file.inp
'''
An example of an input file can be found in 'test.inp'.

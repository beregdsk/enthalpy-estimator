#!/usr/bin/python
import sys, string, os, glob
from math import *


f = open (sys.argv[1])

s = f.readline()
s = f.readline()

while string.find(s, "Total Energy ") == -1:
	s = f.readline()
d = string.split(s) 
HF_QZ = d[3]


while string.find(s, "T1 diagnostic") == -1:
	s = f.readline()
d = string.split(s) 
T1_QZ = d[3]

while string.find(s, "LARGEST") == -1:
	s = f.readline()
s = f.readline()
s = f.readline()
d = string.split(s) 
T2_QZ = d[-1]


while string.find(s, "FINAL SINGLE POINT ENERGY") == -1:
	s = f.readline()
d = string.split(s) 
CCSDT_QZ = float(d[-1])

print CCSDT_QZ, sys.argv[1]

f.close()

path=os.getcwd()


f = open(path+"/../TZ/"+sys.argv[1][0:-10]+'tz_ecp.out')

s = f.readline()
s = f.readline()

while string.find(s, "Total Energy ") == -1:
	s = f.readline()
d = string.split(s) 
HF_TZ = float(d[3])


while string.find(s, "T1 diagnostic") == -1:
	s = f.readline()
d = string.split(s) 
T1_TZ = d[3]

while string.find(s, "LARGEST") == -1:
	s = f.readline()
s = f.readline()
s = f.readline()
d = string.split(s) 
T2_TZ = d[-1]


while string.find(s, "FINAL SINGLE POINT ENERGY") == -1:
	s = f.readline()
d = string.split(s) 
CCSDT_TZ = float(d[-1])

print CCSDT_TZ

f.close()

# CBS extrapolation
HF_TZ = float(HF_TZ)
HF_QZ = float(HF_QZ)
HF1 = HF_TZ
HF2 = HF_QZ
A1 = HF1*(1+2*3)**4
A2 = HF2*(1+2*4)**4
A3 = (1+2*3)**4
A4 = (1+2*4)**4
HF_CBS = (A1-A2)/(A3-A4) 
#HF_CBS = (float(HF_QZ)-0.19593*float(HF_TZ))/0.80407
# Martin and Peterson extrapolation
COR1 = CCSDT_TZ - HF_TZ
COR2 = CCSDT_QZ - HF_QZ
A1 = COR1*(1+2*3)**4
A2 = COR2*(1+2*4)**4
A3 = (1+2*3)**4
A4 = (1+2*4)**4
CCSDT_CBS = (A1-A2)/(A3-A4) + HF_CBS

# get the diffuse functions effect

#f = open(path+"/../TZ_AUG/"+sys.argv[1][0:-10]+'tz_ecp-aug.out')

#E_AUG_HF = 0
#E_AUG_CCSDT = 0

#for line in f:
#        if 'Total Energy' in line:
#                d = string.split(line)
#                E_AUG_HF = float(d[3])
#        if 'FINAL SINGLE POINT' in line:
#                d = string.split(line)
#                E_AUG_CCSDT = float(d[-1])                
#f.close()

# get the core correlation effects

f = open(path+"/../TZ_CORE/"+sys.argv[1][0:-10]+'tz_ecp-core.out')

E_CORE_HF = 0
E_CORE_CCSDT = 0

for line in f:
        if 'Total Energy' in line:
                d = string.split(line)
                E_CORE_HF = float(d[3])
        if 'FINAL SINGLE POINT' in line:
                d = string.split(line)
                E_CORE_CCSDT = float(d[-1])                
f.close()

# get the core correlation effects (no AE)

f = open(path+"/../TZ_FCCORE/"+sys.argv[1][0:-10]+'tz_ecp-core.out')

E_CORE_HF0 = 0
E_CORE_CCSDT0 = 0

for line in f:
        if 'Total Energy' in line:
                d = string.split(line)
                E_CORE_HF0 = float(d[3])
        if 'FINAL SINGLE POINT' in line:
                d = string.split(line)
                E_CORE_CCSDT0 = float(d[-1])                
f.close()

# get the iterative triples correction

f = open(path+"/../TZ_IT/"+sys.argv[1][0:-10]+'tz_ecp-it.out')

E_IT_HF = 0
E_IT_CCSDT = 0

for line in f:
        if 'Total Energy' in line:
                d = string.split(line)
                E_IT_HF = float(d[3])
        if 'FINAL SINGLE POINT' in line:
                d = string.split(line)
                E_IT_CCSDT = float(d[-1])                
f.close()

# get DKH correction

#f = open(path+"/../TZ_DKH/"+sys.argv[1][0:-10]+'tz_dkh.out')
f = open(path+"/../TZ_DKH/"+sys.argv[1][0:-11]+'wcvtz_dkh.out')

HF_TZ_DKH = 0
CCSDT_TZ_DKH = 0

for line in f:
        if 'Total Energy' in line:
                d = string.split(line)
                HF_TZ_DKH = float(d[3])
        if 'FINAL SINGLE POINT' in line:
                d = string.split(line)
                CCSDT_TZ_DKH = float(d[-1])                
f.close()


f = open(sys.argv[1][0:-4]+'.txt', 'w')
f.write(sys.argv[1][0:-24]+'\n')
f.write('\n')
f.write('E(HF/CC-PVTZ) = '+str(HF_TZ)+'\n')
f.write('E(DLPNO-CCSD(T)/CC-PVTZ) = '+str(CCSDT_TZ)+'\n')
f.write('T1 (CC-PVTZ)= '+str(T1_TZ)+'\n')
f.write('T2 (CC-PVTZ)= '+str(T2_TZ)+'\n')
f.write('E(HF/CC-PVQZ) = '+str(HF_QZ)+'\n')
f.write('E(DLPNO-CCSD(T)/CC-PVQZ) = '+str(CCSDT_QZ)+'\n')
#f.write('E(HF/TZ-AUG) = '+str(E_AUG_HF)+'\n')
#f.write('E(DLPNO-CCSD(T)/TZ-AUG) = '+str(E_AUG_CCSDT)+'\n')
f.write('E(HF/TZ-CORE) = '+str(E_CORE_HF)+'\n')
f.write('E(DLPNO-CCSD(T)/TZ-CORE) = '+str(E_CORE_CCSDT)+'\n')
f.write('E(HF/TZ-FCCORE) = '+str(E_CORE_HF0)+'\n')
f.write('E(DLPNO-CCSD(T)/TZ-FCCORE) = '+str(E_CORE_CCSDT0)+'\n')
f.write('E(HF/TZ-IT) = '+str(E_IT_HF)+'\n')
f.write('E(DLPNO-CCSD(T)/TZ-IT) = '+str(E_IT_CCSDT)+'\n')
f.write('T1 (CC-PVQZ)= '+str(T1_QZ)+'\n')
f.write('T2 (CC-PVQZ)= '+str(T2_QZ)+'\n')
f.write('E(HF/CBS) = '+str(HF_CBS)+'\n')
f.write('E(DLPNO-CCSD(T)/CBS) = '+str(CCSDT_CBS)+'\n')
f.write('E(CV correction (TZ)) = '+str(E_CORE_CCSDT-E_CORE_CCSDT0)+'\n')
f.write('E(HF/TZ-DKH) = '+str(HF_TZ_DKH)+'\n')
f.write('E(DLPNO-CCSDT/TZ-DKH) = '+str(CCSDT_TZ_DKH)+'\n')
#f.write('E(DKH correction) = '+str(0)+'\n')
f.write('E(DKH correction) = '+str(CCSDT_TZ_DKH-CCSDT_TZ)+'\n')
f.write('\n')
f.write('\n')
f.close()




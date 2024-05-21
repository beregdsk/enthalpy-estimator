# from ATcT ver. 1.130, Sep 2023
reference = {
#	 'm1_00_H2_': (0, 0.00001, -0.00001), # ATcT, Dihydrogen
	 'm1_00_74-82-80_CH4_': (-17.810, 0.011, -0.011), # ATcT, Methane
#	 'm1_00_74-86-20_C2H2_': (54.570, 0.029, -0.029), # ATcT, acetylene
#	 'm1_00_2143-69-30_C2H2_': (98.504, 0.072, -0.072), # ATcT, Vinylidene
	 'm1_00_74-85-10_C2H4_': (12.519, 0.026, -0.026), # ATcT, Ethylene
	 'm1_00_4218-50-22_C2H4_': (87.565, 0.139, -0.139), # ATcT Ethylidene
	 'm1_00_74-84-00_C2H6_': (-20.079, 0.029, -0.029), # ATcT, Ethane
	 'm1_00_463-49-00_C3H4_': (45.394, 0.055, -0.055), # ATcT, Allene
	 'm1_00_2781-85-30_C3H4_': (67.801, 0.103, -0.103), # ATcT, Cyclopropene
	 'm1_00_74-99-70_C3H4_': (44.338, 0.050, -0.050), # ATcT, propyne
	 'm1_00_75-19-40_C3H6_': (12.882, 0.076, -0.076), # ATcT, Cyclopropane
	 'm1_00_115-07-10_C3H6_': (4.785, 0.043, -0.043), # ATcT, Propene
	 'm1_00_74-98-60_C3H8_': (-25.093, 0.038, -0.038), # ATcT, propane
	 'm1_00_460-12-80_C4H2_': (109.950, 0.134, -0.134), # ATcT, 1,3-Butadiyne
	 'm1_00_689-97-40_C4H4_': (69.187, 0.134, -0.134), # ATcT, Vinylacetylene
	 'm1_00_106-99-00_C4H6_': (26.544, 0.074, -0.074),  # ATcT, 1,3-Butadiene
	 'm1_00_107-00-60_C4H6_': (39.854, 0.131, -0.131), # ATcT 1-Butyne
	 'm1_00_503-17-30_C4H6_': (35.000, 0.110, -0.110), # ATcT 2-Butyne
	 'm1_00_822-35-50_C4H6_': (38.466, 0.143, -0.143), # ATcT Cyclobutene
	 'm1_00_106-98-90_C4H8_': (0.045, 0.081, -0.081), # ATcT, 1-Butene
	 'm1_00_115-11-70_C4H8_': (-4.039, 0.088, -0.088), # ATcT, isobutene
	 'm1_00_590-18-10_C4H8_': (-1.663, 0.093, -0.093), # ATcT, cis-2-Butene
	 'm1_00_287-23-00_C4H8_': (6.632, 0.088, -0.088), # ATcT, Cyclobutane
	 'm1_00_594-11-60_C4H8_': (5.880, 0.311, -0.311), # ATcT, Methylcyclopropane
	 'm1_00_624-64-60_C4H8_': (-2.658, 0.088, -0.088), # ATcT, trans-2-Butene
	 'm1_00_106-97-80_C4H10_': (-30.033, 0.055, -0.055), # ATcT Butane
	 'm1_00_75-28-50_C4H10_': (-32.146, 0.067, -0.067), # ATcT, iso-butane
	 'm1_00_542-92-70_C5H6_': (32.101, 0.143, -0.143), # ATcT, Cyclopentadiene
	 'm1_00_78-79-50_C5H8_': (18.095, 0.158, -0.158), # ATcT, Isoprene
	 'm1_00_142-29-00_C5H8_': (8.442, 0.110, -0.110), # ATcT, Cyclopentene
	 'm1_00_78-78-40_C5H12_': (-36.563, 0.093, -0.093), # ATcT, iso-Pentane
	 'm1_00_109-66-00_C5H12_': (-34.912, 0.069, -0.069), # ATcT, n-Pentane
	 'm1_00_463-82-10_C5H12_': (-39.945, 0.091, -0.091), # ATcT, neo-Pentane
#	 'm1_00_462-80-60_C6H4_': (109.763, 0.206, -0.206), # ATcT, o-Benzyne
#	 'm1_00_1828-89-32_C6H4_': (123.924, 0.287, -0.287), # ATcT, m-Benzyne
#	 'm1_00_3355-34-80_C6H4_': (138.050, 0.287, -0.287), # ATcT, p-Benzyne
	 'm1_00_C6H6_': (19.885, 0.050, -0.050),  # ATcT, Benzene
	 'm1_00_96-38-80_C6H8_': (26.482, 0.335, -0.335), # ATcT, 5-Methyl-1,3-cyclopentadiene
	 'm1_00_110-83-80_C6H10_': (-1.023, 0.076, -0.076), # ATcT, Cyclohexene
	 'm1_00_110-82-70_C6H12_': (-29.348, 0.069, -0.069), # ATcT, Cyclohexane
	 'm1_00_108-88-30_C7H8_': (11.962, 0.074, -0.074), # ATcT, toluene
	 'm1_00_536-74-30_C8H6_': (75.937, 0.170, -0.170), # ATcT Phenylacetylene
	 'm1_00_100-42-50_C8H8_': (35.488, 0.127, -0.127), # ATcT, Phenylethene
	 'm1_00_100-41-40_C8H10_': (7.144, 0.127, -0.127),  # ATcT Ethylbenzene
#	 'm1_00_91-20-3_C10H8_': (35.268, 0.134, -0.134), # ATcT, Naphthalene
#	 'm1_00_259-79-0_C12H8_': (??, ??, ??), # Biphenylene
#	 'm1_00_83-32-9_C12H10_': (??, ??, ??), # Acenaphthene
#	 'm1_00_92-52-4_C12H10_': (42.734, 0.263, -0.263), # ATcT, Biphenyl
#	 'm1_00_569-41-5_C12H12_': (??, ??, ??), # 1,8-Dimethylnaphthalene
#	 'm1_00_581-40-8_C12H12_': (??, ??, ??), # 2,3-Dimethylnaphthalene
#	 'm1_00_581-42-0_C12H12_': (??, ??, ??), # 2,6-Dimethylnaphthalene
#	 'm1_00_582-16-1_C12H12_': (??, ??, ??), # 2,7-Dimethylnaphthalene
#	 'm1_00_120-12-7_C14H10_': (54.204, 0.227, -0.227), # ATcT, Anthracene
#	 'm1_00_85-01-8_C14H10_': (48.528, 0.184, -0.184), # ATcT, Phenanthrene
#	 'm1_00_501-65-50_C14H10_': (97.347, 0.287, -0.287), # ATcT, Diphenylacetylene
#	 'm1_00_103-29-70_C14H14_': (34.011, 0.182, -0.182), # ATcT, 1,2-Diphenylethane
#	 'm1_00_103-29-70_C14H14_1_': (34.011, 0.182, -0.182), # ATcT, 1,2-Diphenylethane
#	 'm1_00_2717-39-7_C14H16_': (??, ??, ??), # 1,4,5,8-Tetramethylnaphthalene
#	 'm1_00_129-00-0_C16H10_': (??, ??, ??), # Pyrene
#	 'm1_00_206-44-0_C16H10_': (??, ??, ??), # Fluoranthene
#	 'm1_00_604-83-1_C16H14_': (??, ??, ??), # 9,10-Dimethylphenanthrene
#	 'm1_00_7396-38-5_C18H18_': (??, ??, ??), # 2,4,5,7-Tetramethylphenanthrene
#	 'm1_00_477-75-8_C20H14_': (??, ??, ??), # Triptycene
#	 'm1_00_53-70-3_C22H14_': (??, ??, ??), # Dibenz[a,h]anthracene
#	 'm1_00_215-58-7_C22H14_': (??, ??, ??), # Dibenz[a,c]anthracene
#	 'm1_00_191-07-1_C24H12_': (??, ??, ??), # Coronene
}


# rerefence heats of formation in kcal/mol from ATcT


# here all double bonds and aromatic bonds are treated in the same way
hybridization_1 = { # (nsp, nsp2, naromatic, nsp3)
	'm1_00_EL-': (0,0,0,0), # example
}

hybridization = { # (nsp, nsp2, naromatic)
	'm1_00_EL-': (0,0,0), # example
}

name = {
	 'm1_00_H2_': 'H2', # ATcT, H2
	 'm1_00_74-82-80_CH4_': 'Methane', # ATcT, Methane
	 'm1_00_74-86-20_C2H2_': 'Acetylene', # ATcT, acetylene
	 'm1_00_2143-69-30_C2H2_': 'Vinylidene', # ATcT, Vinylidene
	 'm1_00_74-85-10_C2H4_': 'Ethylene', # ATcT, Ethylene
	 'm1_00_4218-50-22_C2H4_': 'Ethylidene', # ATcT Ethylidene
	 'm1_00_74-84-00_C2H6_': 'Ethane', # ATcT, Ethane
	 'm1_00_463-49-00_C3H4_': 'Allene', # ATcT, Allene
	 'm1_00_2781-85-30_C3H4_': 'Cyclopropene', # ATcT, Cyclopropene
	 'm1_00_74-99-70_C3H4_': 'Propyne', # ATcT, propyne
	 'm1_00_75-19-40_C3H6_': 'Cyclopropane', # ATcT, Cyclopropane
	 'm1_00_115-07-10_C3H6_': 'Propene', # ATcT, Propene
	 'm1_00_74-98-60_C3H8_': 'Propane', # ATcT, propane
	 'm1_00_460-12-80_C4H2_': '1,3-Butadiyne', # ATcT, 1,3-Butadiyne
	 'm1_00_689-97-40_C4H4_': 'Vinylacetylene', # ATcT, Vinylacetylene
	 'm1_00_106-99-00_C4H6_': '1,3-Butadiene',  # ATcT, 1,3-Butadiene
	 'm1_00_107-00-60_C4H6_': '1-Butyne', # ATcT 1-Butyne
	 'm1_00_503-17-30_C4H6_': '2-Butyne', # ATcT 2-Butyne
	 'm1_00_822-35-50_C4H6_': 'Cyclobutene', # ATcT Cyclobutene
	 'm1_00_106-98-90_C4H8_': '1-Butene', # ATcT, 1-Butene
	 'm1_00_115-11-70_C4H8_': 'Isobutene', # ATcT, isobutene
	 'm1_00_590-18-10_C4H8_': 'cis-2-Butene', # ATcT, cis-2-Butene
	 'm1_00_287-23-00_C4H8_': 'Cyclobutane', # ATcT, Cyclobutane
	 'm1_00_594-11-60_C4H8_': 'Methylcyclopropane', # ATcT, Methylcyclopropane
	 'm1_00_624-64-60_C4H8_': 'trans-2-Butene', # ATcT, trans-2-Butene
	 'm1_00_106-97-80_C4H10_': 'Butane', # ATcT Butane
	 'm1_00_75-28-50_C4H10_': 'iso-Butane', # ATcT, iso-butane
	 'm1_00_542-92-70_C5H6_': 'Cyclopentadiene', # ATcT, Cyclopentadiene
	 'm1_00_78-79-50_C5H8_': 'Isoprene', # ATcT, Isoprene
	 'm1_00_142-29-00_C5H8_': 'Cyclopentene', # ATcT, Cyclopentene
	 'm1_00_78-78-40_C5H12_': 'iso-Pentane', # ATcT, iso-Pentane
	 'm1_00_109-66-00_C5H12_': 'n-Pentane', # ATcT, n-Pentane
	 'm1_00_463-82-10_C5H12_': 'neo-Pentane', # ATcT, neo-Pentane
	 'm1_00_462-80-60_C6H4_': 'o-Benzyne', # ATcT, o-Benzyne
	 'm1_00_1828-89-32_C6H4_': 'm-Benzyne', # ATcT, m-Benzyne
	 'm1_00_3355-34-80_C6H4_': 'p-Benzyne', # ATcT, m-Benzyne
	 'm1_00_C6H6_': 'Benzene',  # ATcT, Benzene
	 'm1_00_96-38-80_C6H8_': '5-Methyl-1,3-cyclopentadiene', # ATcT, 5-Methyl-1,3-cyclopentadiene
	 'm1_00_110-83-80_C6H10_': 'Cyclohexene', # ATcT, Cyclohexene
	 'm1_00_110-82-70_C6H12_': 'Cyclohexane', # ATcT, Cyclohexane
	 'm1_00_108-88-30_C7H8_': 'Toluene', # ATcT, toluene
	 'm1_00_536-74-30_C8H6_': 'Phenylacetylene', # ATcT Phenylacetylene
	 'm1_00_100-42-50_C8H8_': 'Phenylethene', # ATcT, Phenylethene
	 'm1_00_100-41-40_C8H10_': 'Ethylbenzene',  # ATcT Ethylbenzene
	 'm1_00_91-20-3_C10H8_': 'Naphthalene', # ATcT, Naphthalene
	 'm1_00_259-79-0_C12H8_': 'Biphenylene', # Biphenylene
	 'm1_00_83-32-9_C12H10_': 'Acenaphthene', # Acenaphthene
	 'm1_00_92-52-4_C12H10_': 'Biphenyl', # ATcT, Biphenyl
	 'm1_00_569-41-5_C12H12_': '1,8-Dimethylnaphthalene', # 1,8-Dimethylnaphthalene
	 'm1_00_581-40-8_C12H12_': '2,3-Dimethylnaphthalene', # 2,3-Dimethylnaphthalene
	 'm1_00_581-42-0_C12H12_': '2,6-Dimethylnaphthalene', # 2,6-Dimethylnaphthalene
	 'm1_00_582-16-1_C12H12_': '2,7-Dimethylnaphthalene', # 2,7-Dimethylnaphthalene
	 'm1_00_120-12-7_C14H10_': 'Anthracene', # ATcT, Anthracene
	 'm1_00_85-01-8_C14H10_': 'Phenanthrene', # ATcT, Phenanthrene
	 'm1_00_501-65-50_C14H10_': 'Diphenylacetylene', # ATcT, Diphenylacetylene
	 'm1_00_103-29-70_C14H14_': '1,2-Diphenylethane', # ATcT, 1,2-Diphenylethane
	 'm1_00_103-29-70_C14H14_1_': '1,2-Diphenylethane', # ATcT, 1,2-Diphenylethane
	 'm1_00_2717-39-7_C14H16_': '1,4,5,8-Tetramethylnaphthalene', # 1,4,5,8-Tetramethylnaphthalene
	 'm1_00_129-00-0_C16H10_': 'Pyrene', # Pyrene
	 'm1_00_206-44-0_C16H10_': 'Fluoranthene', # Fluoranthene
	 'm1_00_604-83-1_C16H14_': '9,10-Dimethylphenanthrene', # 9,10-Dimethylphenanthrene
	 'm1_00_7396-38-5_C18H18_': '2,4,5,7-Tetramethylphenanthrene', # 2,4,5,7-Tetramethylphenanthrene
	 'm1_00_477-75-8_C20H14_': 'Triptycene', # Triptycene
	 'm1_00_53-70-3_C22H14_': 'Dibenz[a,h]anthracene', # Dibenz[a,h]anthracene
	 'm1_00_215-58-7_C22H14_': 'Dibenz[a,c]anthracene', # Dibenz[a,c]anthracene
	 'm1_00_191-07-1_C24H12_': 'Coronene', # Coronene
}

smiles = {
	 'm1_00_H2_': '[H][H]',
	 'm1_00_74-82-80_CH4_': 'C',
	 'm1_00_74-86-20_C2H2_': 'C#C',
	 'm1_00_2143-69-30_C2H2_': '[C]=C',
	 'm1_00_74-85-10_C2H4_': 'C=C',
	 'm1_00_4218-50-22_C2H4_': '[CH]C',
	 'm1_00_74-84-00_C2H6_': 'CC',
	 'm1_00_463-49-00_C3H4_': 'C=C=C',
	 'm1_00_2781-85-30_C3H4_': 'C1C=C1',
	 'm1_00_74-99-70_C3H4_': 'CC#C',
	 'm1_00_75-19-40_C3H6_': 'C1CC1',
	 'm1_00_115-07-10_C3H6_': 'CC=C',
	 'm1_00_74-98-60_C3H8_': 'CCC',
	 'm1_00_460-12-80_C4H2_': 'C#CC#C',
	 'm1_00_689-97-40_C4H4_': 'C=CC#C',
	 'm1_00_106-99-00_C4H6_': 'C=CC=C',
	 'm1_00_107-00-60_C4H6_': 'CCC#C',
	 'm1_00_503-17-30_C4H6_': 'CC#CC',
	 'm1_00_822-35-50_C4H6_': 'C1CC=C1',
	 'm1_00_106-98-90_C4H8_': 'CCC=C',
	 'm1_00_115-11-70_C4H8_': 'CC(=C)C',
	 'm1_00_590-18-10_C4H8_': 'C/C=C\\C',
	 'm1_00_287-23-00_C4H8_': 'C1CCC1',
	 'm1_00_594-11-60_C4H8_': 'CC1CC1',
	 'm1_00_624-64-60_C4H8_': 'C/C=C/C',
	 'm1_00_106-97-80_C4H10_': 'CCCC',
	 'm1_00_75-28-50_C4H10_': 'CC(C)C',
	 'm1_00_542-92-70_C5H6_': 'C1C=CC=C1',
	 'm1_00_78-79-50_C5H8_': 'CC(=C)C=C',
	 'm1_00_142-29-00_C5H8_': 'C1CC=CC1',
	 'm1_00_78-78-40_C5H12_': 'CCC(C)C',
	 'm1_00_109-66-00_C5H12_': 'CCCCC',
	 'm1_00_463-82-10_C5H12_': 'CC(C)(C)C',
	 'm1_00_462-80-60_C6H4_': 'C1=CC#CC=C1',
	 'm1_00_1828-89-32_C6H4_': 'c1[c]ccc[c]1',
	 'm1_00_3355-34-80_C6H4_': 'c1c[c]cc[c]1',
	 'm1_00_C6H6_': 'c1ccccc1',
	 'm1_00_96-38-80_C6H8_': 'CC1C=CC=C1',
	 'm1_00_110-83-80_C6H10_': 'C1CCC=CC1',
	 'm1_00_110-82-70_C6H12_': 'C1CCCCC1',
	 'm1_00_108-88-30_C7H8_': 'c1ccc(cc1)C',
	 'm1_00_536-74-30_C8H6_': 'c1ccc(cc1)C#C',
	 'm1_00_100-42-50_C8H8_': 'c1ccc(cc1)C=C',
	 'm1_00_100-41-40_C8H10_': 'c1ccc(cc1)CC',
	 'm1_00_91-20-3_C10H8_': 'c1c2ccccc2ccc1',
	 'm1_00_259-79-0_C12H8_': '',
	 'm1_00_83-32-9_C12H10_': '',
	 'm1_00_92-52-4_C12H10_': 'c1ccccc1-c2ccccc2',
	 'm1_00_569-41-5_C12H12_': '',
	 'm1_00_581-40-8_C12H12_': '',
	 'm1_00_581-42-0_C12H12_': '',
	 'm1_00_582-16-1_C12H12_': '',
	 'm1_00_120-12-7_C14H10_': 'c1ccc2cc3ccccc3cc2c1',
	 'm1_00_85-01-8_C14H10_': 'c1ccc2c(c1)ccc3ccccc23',
	 'm1_00_501-65-50_C14H10_': 'c1ccc(cc1)C#Cc2ccccc2',
	 'm1_00_103-29-70_C14H14_': 'c1ccccc1CCc2ccccc2',
	 'm1_00_103-29-70_C14H14_1_': '',
	 'm1_00_2717-39-7_C14H16_': '',
	 'm1_00_129-00-0_C16H10_': '',
	 'm1_00_206-44-0_C16H10_': '',
	 'm1_00_604-83-1_C16H14_': '',
	 'm1_00_7396-38-5_C18H18_': '',
	 'm1_00_477-75-8_C20H14_': '',
	 'm1_00_53-70-3_C22H14_': '',
	 'm1_00_215-58-7_C22H14_': '',
	 'm1_00_191-07-1_C24H12_': ''
}
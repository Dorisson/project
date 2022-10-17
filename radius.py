#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 23:17:21 2022

radius

@author: doris
"""
'''
print("Let's prepare your PDB file for EXAFS modeling")
print("Type in a 4-character PDB code: ")
your_code=input()
'''
from biopandas.pdb import PandasPdb
#p_1 = fetch_pdb(your_code)

p_1 = PandasPdb().read_pdb('{1oco}.pdb')  

import pandas as pd


reference_point = (63.19, 308.39, 191.35)  
distances_atm = p_1.distance(xyz=reference_point, records=('ATOM',))
distances_hetatm = p_1.distance(xyz=reference_point, records=('HETATM',))



all_within_7A_atm = p_1.df['ATOM'][distances_atm < 7.0]  
all_within_7A_hetatm = p_1.df['HETATM'][distances_hetatm < 7.0]


all_within_7A = pd.concat([all_within_7A_atm, all_within_7A_hetatm], axis=0)
print(all_within_7A)


all_within_7A.to_csv('raw_data.csv', index=True)

import csv
with open('raw_data.csv', 'r') as original_coo:
    reader= csv.reader(original_coo)
    next(reader)
    with open('7A_transposed.csv', 'w') as transpose:
        writer=csv.writer(transpose, delimiter=' ')
        for row in reader:
            row [12] = round((round(float(row[12]), 3)-63.19),2)
            row [13] = round((round(float(row[13]), 3)-308.39),2)
            row[14] = round((round(float(row[14]), 3)-191.35),2)
            writer.writerow(row)





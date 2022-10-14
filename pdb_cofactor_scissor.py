#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:01:18 2022

@author: doris

pdb-cofactor-scissor

This program extrapolates co-ordinates of atoms in relation to a metal co-factor
and generates a new pdb file containing the environment in the selected radius.


"""
# Tell the user what the program does
# Ask for input in a form of a 4-character code
print("Hi, this is pdb-cofactor-scissor! I help you study the metal co-factors in your protein structure")
print("Type in a 4-character PDB code: ")
your_code=input()


# Import PandasPdb designed for manipulating PDB files as dataframes
from biopandas.pdb import PandasPdb

# Initialize a new PandasPdb object
# Fetch the PDB file from rcsb.org
ppdb = PandasPdb().fetch_pdb(your_code)
ppdb.to_pdb(path=f'{your_code}.pdb') 


# Read and print some attributes from the file header
print('PDB Code: %s' % ppdb.code)
print('PDB Header Line: %s' % ppdb.header)
print('\nRaw PDB file contents:\n\n%s\n...' % ppdb.pdb_text[:1000])


# Define co-factors as a list
cofactors={'FE', 'CU', 'MO', 'MN', 'CO', 'ZN'}   
print('''
The most common co-factors found in human proteins are: 
 iron, magnesium, manganese, cobalt, copper, zinc, and molybdenum.
 
 
''')
print('''
      Finding cofactors...
      ''')


# This is something I want to introduce and condition the rest of the script
#print('The co-factors are listed bellow. If the protein does not contain any, the program will close.')


# Extract the dataframe containing element symbols of heteroatoms
hetatms=ppdb.df['HETATM']['element_symbol']
'''
Why?
In PDB files, atoms that are not part of the main protein chain, but instead are ligands and likely
inorganic elements, are grouped together under HETATM (meaning heteroatom) identifier.

'''

# Iterate through every atom in heteroatoms and check if it is a co-factor element
# If heteroatom is a co-factor, get its atom number, residue name, chain ID, and xyz co-ordinates
# Introducing variables n and m ensures that the list of co-factors is printed only once
n=0
m = 1
for i in hetatms:
    if i in cofactors : 
        
        atm_no=ppdb.df['HETATM'][ppdb.df['HETATM']['element_symbol'] == i]['atom_number']
        res=ppdb.df['HETATM'][ppdb.df['HETATM']['element_symbol'] == i]['residue_name']
        chain=ppdb.df['HETATM'][ppdb.df['HETATM']['element_symbol'] == i]['chain_id']
        x_co=ppdb.df['HETATM'][ppdb.df['HETATM']['element_symbol'] == i]['x_coord']
        y_co=ppdb.df['HETATM'][ppdb.df['HETATM']['element_symbol'] == i]['y_coord']
        z_co=ppdb.df['HETATM'][ppdb.df['HETATM']['element_symbol'] == i]['z_coord']
        print(m, i, atm_no[n], res[n], chain[n], x_co[n], y_co[n], z_co[n])
        n=n+1
        m=m+1 

# Print the output that is to be analyzed by user
# User chooses the co-factor by specifying co-ordinates from the table
# Define xyz coordinates as variables 
# xyz coordinates are needed to set the reference point in the next step
print('''
      Last three columns represent the xyz coordinates. Make sure that you copy these EXACT values in the next step!
      ''')
print('Specify the co-ordinates of the desired co-factor!')
print('x-coordinates: ')
x=input()
print('y-coordinates: ')
y=input()
print('z-coordinates: ')
z=input()


# Set a reference point using coordinates variables
# Note: value of each coordinate variable has to be a number so convert it to float
reference_point = (float(x), float(y), float(z))  

# Extract distance of atoms and heteroatoms from the reference point
distances_atm = ppdb.distance(xyz=reference_point, records=('ATOM',))
distances_hetatm = ppdb.distance(xyz=reference_point, records=('HETATM',))

# Ask the user to define the radius of co-factor environment
print('Select the radius of the co-factor environment in Ångstroms (note: only number values are accepted!): ')
A=input()

# Apply the radius cutoff by comparing distances of atoms and heteroatoms to the user input
# Note: radius has to be a number so convert it to float
# Extract dataframes containing atoms and heteroatoms within the desred radius
all_within_A_atm = ppdb.df['ATOM'][distances_atm < float(A)]  
all_within_A_hetatm = ppdb.df['HETATM'][distances_hetatm < float(A)]

# Import pandas to access the concatenate tool which merges dataframes
import pandas as pd

# Merge the dataframes containing atoms and heteroatoms
# Print the output for the user
all_within_A = pd.concat([all_within_A_atm, all_within_A_hetatm], axis=0)
print(all_within_A)

# Ask the user if they want to generate a csv file with transposed co-ordinates
print('Would you like to generate a csv table with transposed co-ordinates (set center to x,y,z = 0,0,0)?: y/n')
answ=input()

'''
Why?
To run FEFF calculations required for EXAFS modelling, the program needs input coordinates where 
the absorbing metal atom is in the center defined by x,y,z=0,0,0
'''

# Save the dataframe to csv file
if answ == 'y':
    all_within_A.to_csv(f'{your_code}_{A}Å_radius_ref_point_{x}_{y}_{z}.csv', index=True)
    
    # Import csv
    # Read in the file containing original coordinates
    import csv
    with open(f'{your_code}_{A}Å_radius_ref_point_{x}_{y}_{z}.csv', 'r') as original_coo:
        reader= csv.reader(original_coo)
        #Skip the first row as it contains strings with the index info
        next(reader)
        # Create a new csv file that will contain transposed coordnates
        with open(f'{your_code}_{A}Å_radius_ref_point_0_0_0.csv', 'w') as transpose:
            writer=csv.writer(transpose, delimiter=' ')
            
            # Coordinates are contained in columns 13, 14 and 15
            # Note: counting starts from 0, so it will be 12, 13 and 14
            # Transpose coordinates by subtracting the value of reference point coordinates
            for row in reader:
                row [12] = round((round(float(row[12]), 3)-float(x)),2)
                row [13] = round((round(float(row[13]), 3)-float(y)),2)
                row[14] = round((round(float(row[14]), 3)-float(z)),2)
                #Write the new coordinates
                writer.writerow(row)
                
    # Inform the user that the CSV file is created and display the file name
    print(f'Saving CSV table as: {your_code}_{A}Å_radius_ref_point_0_0_0.csv')
    
else:
    # If CSV table is not needed
    print('OK, then we will just save your new PDB!')
    
# OBS! This part doesn not seem to create the cutoff as it should!
# Writing the new PDB containing atoms within the desired radius
ppdb.to_pdb(path=f'{your_code}_{A}Å_radius_ref_point_{x}_{y}_{z}.pdb', records=None, 
            gz=False, 
            append_newline=True)

#Inform the user that the PDB is created and display the file name
print(f'Your new PDB file is saved in your current directory as: {your_code}_{A}Å_radius_ref_point_{x}_{y}_{z}.pdb ')

       



                             


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 16:47:56 2022

@author: doris
"""


from Bio import PDB
import numpy as np


parser = PDB.PDBParser()
io = PDB.PDBIO()

struct = parser.get_structure('1oco','1oco.pdb')
rotation_matrix = PDB.rotmat(PDB.Vector([0,0,0]), PDB.Vector([0,0,0]))


for atom in struct.get_atoms():
        atom_C1 = atom.coord.copy()
        break

        
for model in struct:
    for chain in model:
        for residue in chain:
            for atom in residue:
                atom.transform(rotation_matrix, -atom_C1)

io.set_structure(struct)
io.save('1oco_coord.pdb')

#this code is actually writing out a pdb
#but you need heteroatom and other stuff, it is incomplete
#i tried to put iron in the center but i am not suceeding

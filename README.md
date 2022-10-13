# PDB Cut and Transpose
This program extrapolates co-ordinates of atoms in relation to a metal co-factor
and generates a new PDB file containing the environment in the radius selected by the user. 

## What is a pdb file?
The Protein Data Bank (pdb) file format is a textual file format describing the three-dimensional structures of molecules held in the Protein Data Bank. Structural biologists use methods such as X-ray crystallography, NMR spectroscopy, and cryo-electron microscopy to determine the location of each atom relative to each other in the molecule, and then deposit this information, which becomes publically available. The pdb format accordingly provides for description and annotation of protein and nucleic acid structures including atomic coordinates, secondary structure assignments, as well as atomic connectivity. 

## How is pdb file structured?
A pdb file usually contains:
### HEADER, TITLE and AUTHOR records
provide information about the researchers who defined the structure; numerous other types of records are available to provide other types of information.
### REMARK records
can contain free-form annotation, but they also accommodate standardized information
### SEQRES records
give the sequences of the three peptide chains (named A, B and C), which are very short in this example but usually span multiple lines.
### ATOM records
describe the coordinates of the atoms that are part of the protein. For example, the first ATOM line above describes the alpha-N atom of the first residue of peptide chain A, which is a proline residue; the first three floating point numbers are its x, y and z coordinates and are in units of Ångströms.The next three columns are the occupancy, temperature factor, and the element name, respectively.
### HETATM records
describe coordinates of hetero-atoms, that is those atoms which are not part of the protein molecule, for example, atoms of ligands and metal co-factors.


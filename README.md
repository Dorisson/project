# PDB Cut and Transpose
This program extrapolates co-ordinates of atoms in relation to a metal co-factor
and generates a new PDB file containing the environment in the radius selected by the user. 

## What is a pdb file?
The Protein Data Bank (pdb) file format is a textual file format describing the three-dimensional structures of molecules held in the Protein Data Bank. Structural biologists use methods such as X-ray crystallography, NMR spectroscopy, and cryo-electron microscopy to determine the location of each atom relative to each other in the molecule, and then deposit this information, which becomes publically available. The pdb format accordingly provides for description and annotation of protein and nucleic acid structures including atomic coordinates, secondary structure assignments, as well as atomic connectivity. 

### What is the format of a pdb file?
A pdb file usually contains:
#### HEADER, TITLE and AUTHOR records
provide information about the researchers who defined the structure; numerous other types of records are available to provide other types of information.
#### REMARK records
can contain free-form annotation, but they also accommodate standardized information.
#### SEQRES records
give the sequences of the three peptide chains (named A, B and C).
#### ATOM records
describe the coordinates of the atoms that are part of the protein, as well as the occupancy, temperature factor, and the element name, respectively.
#### HETATM records
describe coordinates of hetero-atoms, that is those atoms which are not part of the protein molecule, for example, atoms of ligands or metal co-factors.

This program particularly focuses on ATOM and HETATM records. 

## Working with pdb structures
In a typical entry, you will find a diverse mixture of biological molecules, small molecules, ions, and water. Often, you can use the names and chain IDs to help sort these out. However, pdb files can contain up to 80 columns and thousands of lines of categorized structural information, hence extracting desired information manually can be a tideous process. For most applications, PDB files can be accessed via visualization tools, which read in the PDB file and display the protein structure. These programs also include analysis tools that allow you to measure distances and bond angles, and identify interesting structural features. 
Some applications require the access to a larger block of structural information, often related to atomic records and containing some number values, which need to be extracted and/or modified. Whether that involves simple appending/deleting of information, or maybe various mathematical operations, a little knowledge in coding can go a long way in helping you deal with pdb files. 

### Available tools for Python programming languag
Did you know that: Python is frequently used to manipulate pdb files? In fact, over time, the users have developed series of modules, along with the pipelines and tutorials for most common operations. Some of the most commonly used tools to handle pdb files are ** PDB ** (from ** Bio ** module), ** PandasPDB ** (from **Biopandas** ), and `pdb-tools` (available at ** PyPi ** 
### Why use PDB Cut and Transpose?

## How does it work?
divide code in significant blocks and describe what each of them does
give some examples from the code
note important details of the user input
explain the output

## Errors and debugging

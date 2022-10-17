# pdb_cofactor_scissor
This program extrapolates co-ordinates of atoms in relation to a metal co-factor
and generates a new PDB file containing the environment in the radius selected by the user. 

## Before you start:
Make sure you have all the modules needed to run the scripts in Python.
You will need to instal `biopandas`.

BioPandas requires the following software and packages:

Python >= 3.7
NumPy >= 1.11.2
SciPy >= 0.18.1
Pandas >= 0.19.1
PyPI

You can install the latest stable release of biopandas directly from Python's package index via pip by executing the following code from your command line:

`pip install biopandas`
  
Versions of biopandas are now also available via conda-forge; you can install it via

`conda install biopandas -c conda-forge`

or simply

`conda install biopandas`

if you have conda-forge already added to your channels.

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

### Available tools in Python
Did you know that: Python is frequently used to manipulate pdb files? In fact, over time, the users have developed series of modules, along with the pipelines and tutorials for most common operations. Some of the most commonly used tools to handle pdb files are `PDB` (from `Bio` module),`PandasPdb` (from `Biopandas` ), and `pdb-tools` (available at `PyPi` ), but if you understand the format of the pdb files, you can get creative and combine these modules with some generic Python tools. For example, you can covert and handle the pdb as a number array using `numpy`, or treat them as lists using `csv`. 

### Why use pdb_cofactor_scissor?
`pdb_cofactor_scissor` is designed to help you extract the information about the co-factor(s) present in your protein structure without the need to manually handle a huge amount of structural information contained in pdb files. It can be used in applications where you are interested in treating the co-factor as a center of your biomolecule, and/or studying a very narrow environment surrounding the co-factor, which is likely ranging from 2 to 10 Å. The idea for this program came from the pipeline for EXAFS modeling, which involves placing the absorbing metal in the center (xyz = 0, 0, 0) and calculating the scattering wave functions of the elements in the vicinity of the metal which will be use for fitting of the original data, with the highest fidelity for distances within 5 Å.

## How does it work?

Start the program by calling the script using `python`:

```
$ python pdb_cofactor_scissor.py 
```
Type in the 4-character PDB code under which the protein structure is deposed in the Protein Data Bank:

```
Hi, this is pdb-cofactor-scissor! I help you study the metal co-factors in your protein structure!
Type in a 4-character PDB code: 
1odo
```
The program returns some information about the pdb file and its contents:

```
PDB Code: 
PDB Header Line: 

Raw PDB file contents:

HEADER    OXIDOREDUCTASE                          19-FEB-03   1ODO              
TITLE     1.85 A STRUCTURE OF CYP154A1 FROM STREPTOMYCES COELICOLOR             
TITLE    2 A3(2)                                                                
COMPND    MOL_ID: 1;                                                            
COMPND   2 MOLECULE: PUTATIVE CYTOCHROME P450 154A1;                            
COMPND   3 CHAIN: A;                                                            
COMPND   4 SYNONYM: CYP154A1, SCO2884, SCE6.21;                                 
COMPND   5 ENGINEERED: YES;                                                     
COMPND   6 OTHER_DETAILS: HEME CONTAINING PROTEIN                               
SOURCE    MOL_ID: 1;                                                            
SOURCE   2 ORGANISM_SCIENTIFIC: STREPTOMYCES COELICOLOR;                        
SOURCE   3 ORGANISM_TAXID: 100226;                                              
SOURCE   4 STRAIN: A3(2);   
...
```
The program starts searching for co-factors and it writes them out as a table: 

```
The most common co-factors found in human proteins are: 
 iron, magnesium, manganese, cobalt, copper, zinc, and molybdenum.

Finding cofactors...

1 FE 3062 HEM A -6.173 -9.655 -1.561

Last three columns represent the xyz coordinates. Make sure that you copy these EXACT values in the next step!
```
The user needs to type in the exact coordinates (because the table main contain more than one cofactor):

```
Specify the co-ordinates of the desired co-factor!
x-coordinates: 
-6.173
y-coordinates: 
-9.655
z-coordinates: 
-1.561
```
Next thing to do is to select the radius by entering a number value:

```
Select the radius of the co-factor environment in Ångstroms (note: only number values are accepted!): 
3
```
The program returns the output containing atoms and heteroatoms within the selected radius:

```
     record_name  atom_number blank_1 atom_name alt_loc residue_name blank_2 chain_id  residue_number  ... y_coord z_coord  occupancy  b_factor  blank_4  segment_id  element_symbol charge line_idx
2663        ATOM         2664                SG                  CYS                A             354  ... -10.780   0.166        1.0     11.74                                    S    NaN     3080
0         HETATM         3062                FE                  HEM                A            1407  ...  -9.655  -1.561        1.0     11.03                                   FE    NaN     3478
5         HETATM         3067                NA                  HEM                A            1407  ... -10.255  -3.043        1.0     11.11                                    N    NaN     3483
16        HETATM         3078                NB                  HEM                A            1407  ...  -8.155  -1.070        1.0     10.62                                    N    NaN     3494
24        HETATM         3086                NC                  HEM                A            1407  ...  -9.045  -0.102        1.0     10.01                                    N    NaN     3502
32        HETATM         3094                ND                  HEM                A            1407  ... -11.085  -2.049        1.0     11.20                                    N    NaN     3510
45        HETATM         3107                N3                  PIM                A            1408  ...  -8.239  -3.025        1.0     14.45                                    N    NaN     3523

[7 rows x 21 columns]
```
To transpose the coordinates and save the output to a .csv file, the user needs to enter 'y':

```
Would you like to generate a csv table with transposed co-ordinates (set center to x,y,z = 0,0,0)?: y/n
y
Saving CSV table as: 1odo_3Å_radius_ref_point_0_0_0.csv
```
Finally, the new PDB file containing only structural informations of elements within the selected radius is created:

```
Your new PDB file is saved in your current directory as: 1odo_3Å_radius_ref_point_-6.173_-9.655_-1.561.pdb
```

## Errors and debugging
The current program version is not applying the radius cutoff when saving a new pdb file. I am developing a side code that would approach this problem in a better way and avoid dealing with the dataframe but instead use `set-structure` from `Bio` module. Other possible alterations and upgrades are indicated in the script. Also, for some reason, the program simply fails when entering some valid PDB codes. To test the program, try using codes '1odo' and '1kzy'.


## Update
The code is now applying the radius cutoff when saving the pdb file.

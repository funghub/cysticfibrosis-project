'''
According to the textbook:
Find the most  common alteration in the sequence of this gene: 
a 3 bp deletion, deleting the residue 508Phe from the protein'''

# open file of the wildtype protein sequence and save into variable protein_seq
with open("protein_mut\wt_protein_seq.txt", "r") as file:
    protein_seq = "".join(line.strip() for line in file)

print(protein_seq[507])  # confirm in fact at 508 there is Phe, it should return F


### find the exact line for this deletion in the excel file
import pandas as pd
import re

# Load sorted raw file into pd
sorted_xl = pd.read_excel("datasets/output_CFTR-Fr.xlsx")

phe_del = sorted_xl.loc[sorted_xl['nom_prot'] == 'p.(Phe508del)'].iloc[0]

print(phe_del)

phe_del_sequence = protein_seq[:507] + protein_seq[508:]

print(phe_del_sequence)  
# here is your mutated protein sequence that can be entered into alphafold

with open("protein_mut/phe508.txt", "w") as mut_protein:
    mut_protein.write(phe_del_sequence)
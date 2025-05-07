'''
This protein should take what kind of protein mutation and output the associated protein mutatated sequence
'''

# open file of the wildtype protein sequence and save into variable protein_seq
with open("protein_mut\wt_protein_seq.txt", "r") as file:
    protein_seq = "".join(line.strip() for line in file)


# print(protein_seq[507])  # confirm in fact at 508 there is Phe, it should return F


## this will ask user to input required information to create protein sequence
while True:
    print(f"Original sequence:\n{protein_seq}\n\n")
    print("Please open the datasets\AllVariantsCFTR-France_03-09-2024.xlsx and reference column labeled type_prot and nom_prot")
    type_prot = (input("Assistance with reading notation can be found here: https://www.hgvs.org/mutnomen/recs-prot.html#indelp \n\nWhat is type_prot (the type of mutation: frameshift, missense, inframe, stop codon)? : ")).lower()
    if type_prot == "frameshift":
        first_aa = int(input("What is the location of the first amino acid? ex: Thr ### Glnfs*3 : "))
        aa_replaced = (input("What is the amino acid replaced at that position? Please enter as a letter : ")).upper()
        termination = int(input("What is the location of the early termination? ex: Thr388Glnfs* ## : "))
        print(f"Here is a test to see if position {first_aa} is indeed your first aa:  {protein_seq[first_aa-1]}\n")
        mut_protein = protein_seq[:first_aa-1] + aa_replaced + f" + {termination-1} more amino acids afterwards"

    elif type_prot == "inframe":
        dup_del = input("Is this a duplication or deletion or both?: ")
        first_aa = int(input("What is the location of the first amino acid? ex: p.(Leu ### _Asp1305delinsVal) : "))
        second_aa = int(input("What is the location of the second amino acid? PUT \"0\" if no 2nd amino acid ex: p.(Leu1304_Asp ### delinsVal) : "))
        if dup_del == "duplication":
            print(f"test: duplicate {protein_seq[first_aa-1:second_aa]}\n\n")
            # mut_protein = protein_seq[:second_aa] + protein_seq[first_aa-1:second_aa] + " +++++ " + protein_seq[second_aa:] # test sequence
            mut_protein = protein_seq[:second_aa] + protein_seq[first_aa-1:second_aa]+ protein_seq[second_aa:]
        elif dup_del == "deletion":
            if second_aa > 0:
                print(f"test: delete {protein_seq[first_aa-1:second_aa]}\n\n")
                # mut_protein = protein_seq[:first_aa-1] + " +++++ "  + protein_seq[second_aa:] # test sequence
                mut_protein = protein_seq[:first_aa-1] + protein_seq[second_aa:]
            else:
                print(f"test: delete {protein_seq[first_aa-1]}\n\n")
                # mut_protein = protein_seq[:first_aa-1] + " +++++ "  + protein_seq[first_aa:] # test sequence
                mut_protein = protein_seq[:first_aa-1] + protein_seq[first_aa:]
        elif dup_del == "both":
            print(f"test: delete {protein_seq[first_aa-1:second_aa]}\n\n")
            ins_aa = input("What amino acid to insert?: ").upper()
            # mut_protein = protein_seq[:first_aa-1] + " +++++ " + ins_aa + " +++++ " + protein_seq[second_aa:] # test sequence
            mut_protein = protein_seq[:first_aa-1] + ins_aa + protein_seq[second_aa:]

    elif type_prot == "missense":
        loc_aa = int(input("What is the location of the amino acid? ex: Thr ### Gln : "))
        aa_replaced = (input("What is the amino acid replaced at that position? Please enter as a letter : ")).upper()
        print(f"Here is a test to see if position {loc_aa} is indeed your first aa:  {protein_seq[loc_aa-1]}\n")
        
        # mut_protein = protein_seq[:loc_aa-1] + " +++++ " + aa_replaced + " +++++ " + protein_seq[loc_aa:] # test sequence
        mut_protein = protein_seq[:loc_aa-1] + aa_replaced + protein_seq[loc_aa:]

    elif type_prot == "stop codon":
        loc_aa = int(input("What is the location of the amino acid? ex: Thr ### * : "))
        print(f"Here is a test to see if position {loc_aa} is indeed your first aa:  {protein_seq[loc_aa-1]}\n")
        # mut_protein = protein_seq[:loc_aa-1] + " ****** " + protein_seq[loc_aa:] # test sequence
        mut_protein = protein_seq[:loc_aa-1] + "*"

    print(f"\nYour mutated protein sequence:\n{mut_protein}\n\n")

'''        
According to the textbook:
Find the most  common alteration in the sequence of this gene: 
a 3 bp deletion, deleting the residue 508Phe from the protein'''
def write_phe508():
    ### find the exact line for this deletion in the excel file
    import pandas as pd
    import re

    # Load sorted raw file into pd
    sorted_xl = pd.read_excel("datasets/output_CFTR-Fr.xlsx")

    phe_del = sorted_xl.loc[sorted_xl['nom_prot'] == 'p.(Phe508del)'].iloc[0]

    print(phe_del)

    phe_del_sequence = protein_seq[:507] +  protein_seq[508:]

    print(phe_del_sequence)  
    # here is your mutated protein sequence that can be entered into alphafold

    with open("protein_mut/test_phe508.txt", "w") as mut_protein:
        mut_protein.write(phe_del_sequence)
# write_phe508()  # this will print out the amino acid sequence for phe508 deletion
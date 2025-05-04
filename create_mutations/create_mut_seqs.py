'''
The goal of this program is to create a new column in the xlsx file with the mutated sequence
'''

import pandas as pd
import re

# Load sorted raw file into pd
sorted_xl = pd.read_excel("datasets/output_CFTR-Fr.xlsx")

# open file of the edited sequence and save into variable hgvs_seq
with open("sequences/edited_seq.txt", "r") as file_seq:
    hgvs_seq = file_seq.read()
# print(hgvs_seq)

'''
CDS is in 133..4575 (taken from https://www.ncbi.nlm.nih.gov/nuccore/NM_000492.3/)
for example: c. 1000C>T (133 + 1000 - 1 - 1 = actual position of C) or (132 + 999 to account for HGVS notation 0-exclusive)
'''

# Set CDS start position and regex search
codon_start = 133
sub_pattern = re.compile(r"c\.(\d+)([ATGC])>([ATGC])")  # groups: (\d+),([ATGC]),([ATGC])
del_pattern = re.compile(r"c\.(\d+)(?:_(\d+))?(?:\+(\d+))?del$") # groups:(\d+),(?:_(\d+)),(\d+)

# extract coordinates
def search_location(location):
        # print(location)
        if ">" in location:  # find substitutions
            match = sub_pattern.search(location)
            sub_location = match.group(1)
            sub_nucleotide = match.group(3)
            return pd.Series([sub_location, sub_nucleotide])
        elif "del" in location:  # find deletions
            match = del_pattern.search(location)
            del_location1 = match.group(1)
            del_location2 = match.group(2)
            del_location3 = match.group(3)
            if del_location2 == None:
                return pd.Series([del_location1,None])
            else:
                if del_location3 != None:
                    del_location2 = int(del_location2) + int(del_location3)
                return pd.Series([f"{del_location1}-{del_location2}", None])

sorted_xl[["mut_location","sub_nucleotide"]] = sorted_xl["HGVS name (NM_000492.3)"].apply(search_location)

'''
Use these to validate
print(sorted_xl)
print(sorted_xl["sub_nucleotide"].value_counts())
'''

# create column in dataframe with the mutated sequence hgvs_seq
def mut_seq(row):  # row passes the dataframe from sorted_xl.apply()
    # print(row["mut_location"])
    if row["DNA type"] == "subs":
        index = 133 + int(row["mut_location"]) - 2
        mut_sequence = hgvs_seq[:index] + row["sub_nucleotide"] + hgvs_seq[index+1:]
        return mut_sequence
    elif row["DNA type"] == "del":
        match_del = re.search(r"(\d+)(?:-(\d+))?", row["mut_location"])
        del_loc1 = match_del.group(1)
        del_loc2 = match_del.group(2)

        del_loc1 = int(del_loc1) + 133 - 2

        if del_loc2 != None:
            del_loc2 = int(del_loc2) + 133 - 2
            mut_sequence = hgvs_seq[:del_loc1] + hgvs_seq[del_loc2+1:]
        else:
            mut_sequence = hgvs_seq[:del_loc1] + hgvs_seq[del_loc1+1:]
        return mut_sequence

# apply function to each line to get the new column with the sequences
sorted_xl["mut_DNA"] = sorted_xl.apply(mut_seq, axis=1)

# create csv file with the new sequences in a column
sorted_xl.set_index("HGVS name (NM_000492.3)").to_csv("create_mutations/output_mut_seqs.csv")  # mutated sequences in mut_DNA



## isolate the HGVS name and the sequence
just_sequences = sorted_xl[["HGVS name (NM_000492.3)","mut_DNA"]]






# create shorter sequences for Alphafold
def cut_seq(row):
    sequence_cut = row["mut_DNA"][:5000]
    return sequence_cut

just_sequences["mut_DNA_cut"]= just_sequences.apply(cut_seq, axis = 1)

# create csv file shorter sequences in a column
cut_sequences = just_sequences.drop(columns=["mut_DNA"])
cut_sequences.set_index("HGVS name (NM_000492.3)").to_csv("create_mutations/output_shorter_seqs.csv")  # mutated sequences in mut_DNA and shorter ones to work in alphafold



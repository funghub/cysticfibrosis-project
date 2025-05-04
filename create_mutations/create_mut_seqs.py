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
sub_pattern = re.compile(r"c\.(\d+)([ATGC])>([ATGC])")
del_pattern = re.compile(r"c\.(\d+)(?:_(\d+))?(?:\+(\d+))?del$")

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
print(sorted_xl)

print(sorted_xl["sub_nucleotide"].value_counts())



# # Apply mutations to sequence
# mutated_sequence = list(sequence)

# for _, row in filtered_df.iterrows():
#     parsed = row['parsed']
#     if not parsed:
#         continue
#     if parsed[0] == "substitution":
#         _, pos, ref, alt = parsed
#         idx = pos - genomic_start
#         if 0 <= idx < len(mutated_sequence) and sequence[idx] == ref:
#             mutated_sequence[idx] = alt
#     elif parsed[0] == "deletion":
#         _, start, end, _ = parsed
#         idx_start = start - genomic_start
#         idx_end = end - genomic_start + 1
#         if 0 <= idx_start < len(mutated_sequence):
#             del mutated_sequence[idx_start:idx_end]

# # Save mutated sequence
# with open("mutated_sequence.txt", "w") as f:
#     f.write(">Mutated CFTR sequence\n")
#     for i in range(0, len(mutated_sequence), 70):
#         f.write(''.join(mutated_sequence[i:i+70]) + "\n")
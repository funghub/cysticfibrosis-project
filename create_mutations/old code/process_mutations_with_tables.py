# plese do not use this

import pandas as pd
import re

# Load input files
xls = pd.ExcelFile("datasets/AllVariantsCFTR-France_03-09-2024.xlsx")
df = xls.parse('AllVariants_03092024')

with open("raw_sequence.txt", "r") as file:
    lines = file.readlines()
sequence = ''.join([line.strip() for line in lines if not line.startswith(">")])

# Set genomic reference start position
genomic_start = 117199644

# Define regex patterns
substitution_pattern = re.compile(r"g\.(\d+)([ACGT])>([ACGT])")
deletion_pattern = re.compile(r"g\.(\d+)(?:_(\d+))?del")

# Function to extract mutation details
def extract_mutation_details(hgvs):
    if isinstance(hgvs, str):
        if match := substitution_pattern.match(hgvs):
            pos, ref, alt = match.groups()
            return ("substitution", int(pos), ref, alt)
        elif match := deletion_pattern.match(hgvs):
            start = int(match.group(1))
            end = int(match.group(2)) if match.group(2) else start
            return ("deletion", start, end, None)
    return None

# Extract and classify mutations
df['mutation_type'] = df['Genomic position (NC_000007.13, hg19)'].apply(
    lambda x: extract_mutation_details(x)[0] if extract_mutation_details(x) else None
)
filtered_df = df[df['mutation_type'].isin(['substitution', 'deletion'])].copy()
filtered_df['parsed'] = filtered_df['Genomic position (NC_000007.13, hg19)'].apply(extract_mutation_details)

# Prepare summary tables
substitutions = []
deletions = []
mutated_sequence = list(sequence)

for _, row in filtered_df.iterrows():
    parsed = row['parsed']
    if not parsed:
        continue

    if parsed[0] == "substitution":
        _, pos, ref, alt = parsed
        idx = pos - genomic_start
        actual_base = sequence[idx] if 0 <= idx < len(sequence) else None
        substitutions.append({
            "genomic_pos": pos,
            "ref_base": ref,
            "actual_base": actual_base,
            "alt_base": alt,
            "match": ref == actual_base
        })
        if 0 <= idx < len(mutated_sequence) and actual_base == ref:
            mutated_sequence[idx] = alt

    elif parsed[0] == "deletion":
        _, start, end, _ = parsed
        idx_start = start - genomic_start
        idx_end = end - genomic_start + 1
        deleted_seq = sequence[idx_start:idx_end] if 0 <= idx_start < len(sequence) else None
        deletions.append({
            "start": start,
            "end": end,
            "deleted_seq": deleted_seq
        })
        if 0 <= idx_start < len(mutated_sequence):
            del mutated_sequence[idx_start:idx_end]

# Save mutated sequence
with open("mutated_sequence.txt", "w") as f:
    f.write(">Mutated CFTR sequence\n")
    for i in range(0, len(mutated_sequence), 70):
        f.write(''.join(mutated_sequence[i:i+70]) + "\n")

# Save summary tables
pd.DataFrame(substitutions).to_csv("substitution_summary.csv", index=False)
pd.DataFrame(deletions).to_csv("deletion_summary.csv", index=False)

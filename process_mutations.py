
import pandas as pd
import re

# Load input files
xls = pd.ExcelFile("AllVariantsCFTR-France_03-09-2024 (1).xlsx")
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

# Apply mutations to sequence
mutated_sequence = list(sequence)

for _, row in filtered_df.iterrows():
    parsed = row['parsed']
    if not parsed:
        continue
    if parsed[0] == "substitution":
        _, pos, ref, alt = parsed
        idx = pos - genomic_start
        if 0 <= idx < len(mutated_sequence) and sequence[idx] == ref:
            mutated_sequence[idx] = alt
    elif parsed[0] == "deletion":
        _, start, end, _ = parsed
        idx_start = start - genomic_start
        idx_end = end - genomic_start + 1
        if 0 <= idx_start < len(mutated_sequence):
            del mutated_sequence[idx_start:idx_end]

# Save mutated sequence
with open("mutated_sequence.txt", "w") as f:
    f.write(">Mutated CFTR sequence\n")
    for i in range(0, len(mutated_sequence), 70):
        f.write(''.join(mutated_sequence[i:i+70]) + "\n")

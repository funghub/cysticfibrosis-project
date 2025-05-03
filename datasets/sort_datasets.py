import pandas as pd

# import the excel file as pd
raw_exc = pd.read_excel("datasets/AllVariantsCFTR-France_03-09-2024.xlsx")
# print(raw_exc.columns)

# take out useless columns
del_col = raw_exc.drop(columns = ['Legacy name','Genomic position (NC_000007.13, hg19)'])
# print(del_col.columns)

# print(del_col["subclass"].value_counts()) # this is to test whether filtering works

# take out VUS1 and VUS2 because they are unlikely to be pathogenic
filtered_exc = del_col[(del_col['type segment'] == "exon") & (del_col['DNA type'].isin(['subs','del']) & (~del_col['subclass'].isin(['NULL', 'undefined','non-CF','VUS1', 'VUS2'])))]
# print(filtered_exc.head(10))
# print(filtered_exc["subclass"].value_counts())
listed = ['HGVS name (NM_000492.3)', 'type segment', 'num segment', 'DNA type','nom_prot', 'type_prot', 'class', 'subclass', 'CFTR2']
# print(list(map(lambda x: filtered_exc[x].value_counts(), listed))) # print out counts of each column

# output the sorted file with the index set as the below without axis numbering
filtered_exc.set_index("HGVS name (NM_000492.3)").to_excel("datasets/output_CFTR-Fr.xlsx")
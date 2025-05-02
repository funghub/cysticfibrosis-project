with open("sequences/edited_seq.txt") as string_seq:
    line = string_seq.readline()
    # print(line) # this is to print the entire sequence

# CDS is in 133..4575 (taken from https://www.ncbi.nlm.nih.gov/nuccore/NM_000492.3/)
print(line[132:141]) # make sure that this CDS starts with codons matching MQR ...

# we subtract 2 here because we need to account for CDS start is at 1 and not 0 like python, same for c.DNA position here
print(line[133 + 1000 - 2]) #c. 1000C>T (133 + 1000 - 1 - 1) or (132 + 999 to account for HGVS 0-exclusive)
print(line[133 + 1039 - 2]) #c. 1039C>T
print(line[133 + 1135 - 2]) #c. 1135G>A
print(line[133 + 1116 - 2]) #c. 1116G>A
print(line[133 + 1135 - 2]) #c. 1135G>A
# open the raw dequence file
with open("sequences/wt_dna_sequence.txt", "r") as file:
    next(file)
    sequence = file.read()

# write the sequence from the raw file as just a uninterrupted string
with open("sequences/edited_seq.txt", "w") as just_sequence:
    for line in sequence:
        just_sequence.write(line.strip()) # remove all white space characters
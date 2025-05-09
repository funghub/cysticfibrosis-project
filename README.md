## Project Proposal: Visualizing Mutations in the Cystic Fibrosis Gene with AlphaFold

# Input Data Files
The input data files are 
* **datasets/AllVariantsCFTR-France_03-09-2024.xlsx**
* **sequence/wt_dna_sequence.txt**
* **protein_mut/wt_protein_seq.txt**

Process to Run Source Code: 
(step 1 and 2 are the most important to generate the required files for 3 and 4)
1. datasets/sort_datasets.py
2. sequences/create-edited_seq.py
3. create_mutations/create_mut_seqs.py
4. protein_mut/create_protein_mut.py

# Introduction

Cystic fibrosis is a known genetic disease that affects one in every 2500 in American and European countries. Interestingly, the protein that is responsible for the uptake of Salmonella typhi causing typhoid fever is also the protein made defective in cystic fibrosis. In cystic fibrosis, the defective protein leads to increased resistance to typhoid fever in heterozygotes who are carriers of the mutation [1]. What mutations lead to cystic fibrosis and to the improper function of the protein responsible for the disease? Cystic fibrosis transmembrane conductance regulator (CFTR) gene, in chromosome 7, codes for ion-channel proteins that are responsible for transporting chloride ions [4]. The healthy transport of chloride ions inside and outside of the cell allows for water movement that hydrates the mucus in the airways. Patients with cystic fibrosis have a mutation in the CFTR gene coding for a faulty protein channel that causes thick mucus in the lungs leading to symptoms like repeat lung infections [2], [3]. With more than 2,500 mutations in the CFTR gene discovered that cause cystic fibrosis [4], what are the conserved sequences in the CFTR gene that allow for the protein to function correctly? What crucial regions in the CFTR protein, in relation to the conserved sequences, allow for the proper transport of chloride ions?

# Our Project
Through CFTR-Fr datasets, we seek to visualize the list of mutations on AlphaFold by inputting the DNA sequences and protein sequences created from the HGVS nomenclature and reference gene on NCBI. We investigate how mutations in those regions of the gene affect the final shape and function of the CFTR protein, specifically the crucial parts of the protein, such as Phe508del in 90% of cystic fibrosis patients.


# What Dataset we use
https://cftr.chu-montpellier.fr/cgi-bin/variant_list.cgi?&
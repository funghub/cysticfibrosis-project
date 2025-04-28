## Project Proposal: Mutations in the Cystic Fibrosis Gene

# Introduction

Cystic fibrosis is a known genetic disease that affects one in every 2500 in American and European countries. Interestingly, the protein that is responsible for the uptake of Salmonella typhi causing typhoid fever is also the protein made defective in cystic fibrosis. In cystic fibrosis, the defective protein leads to increased resistance to typhoid fever in heterozygotes who are carriers of the mutation [1]. What mutations lead to cystic fibrosis and to the improper function of the protein responsible for the disease? Cystic fibrosis transmembrane conductance regulator (CFTR) gene, in chromosome 7, codes for ion-channel proteins that are responsible for transporting chloride ions [4]. The healthy transport of chloride ions inside and outside of the cell allows for water movement that hydrates the mucus in the airways. Patients with cystic fibrosis have a mutation in the CFTR gene coding for a faulty protein channel that causes thick mucus in the lungs leading to symptoms like repeat lung infections [2], [3]. With more than 2,500 mutations in the CFTR gene discovered that cause cystic fibrosis [4], what are the conserved sequences in the CFTR gene that allow for the protein to function correctly? What crucial regions in the CFTR protein, in relation to the conserved sequences, allow for the proper transport of chloride ions?

Through publicly available data, our project aims to identify the conserved regions of the CFTR gene by comparing sequences with and without cystic fibrosis. From the identified conserved regions, we will investigate how mutations in those regions of the gene affect the final shape and function of the CFTR protein, specifically the crucial parts of the protein.

# Methods

In order to find the mutation that causes cystic fibrosis, we will build a Python-based program that will identify the CFTR gene through multiple sequence alignment. Our program will align multiple CFTR gene variants from cystic fibrosis databases, such as CFTR-France [5] and CFTR2 [6], in order to identify the conserved regions and potential mutations. It will be able to identify the mutation type in each sequence and its location on the sequence, as well as translate them to the resulting amino acid sequence. Current programs exist, like ones found on Jupyter Notebook [7], will be used as assistance to our code.

Once the mutation is identified, we will utilize AlphaFold [8] to generate predicted 3D protein structures for wildtype and the mutated proteins from our study. By comparing these visualizations, we can infer the impact of the CFTR mutation on the protein’s folding and functions. To further test the validity of our project, we will compare our generated AlphaFold proteins to the existing sources. 

# Possible results and their implications

If successful, our project will pinpoint conserved regions in the CFTR gene that are critical to its function. By comparing sequences from individuals with and without cystic fibrosis, we hope to find the impact of the CFTR mutation of the protein’s foldings and functions through a Python based program that will easily help us identify the mutation type in each sequence. 
 A positive outcome could lead to better understanding of which mutations are most detrimental and why. A good result would also be showing sequences with mutations put into alpha fold would show an alarming difference in the protein structure from the original wild type [8].  

On the flip side would be if the alpha folds do not align with our predictions of mutations in the conserved sequences then showing similar properties and functions to the non mutated sequences, which would mean that our analysis and code failed [8]. Additionally, data gaps of the mutations  can be present and might be coming from the CFTR2 and CFTR-France datasets as they only have about 1000 mutations listed, while more than 2500 mutations in the CFTR have been discovered, which then lead to cystic fibrosis [4].


# References

[1]	A. M. Lesk, “Genome Organization and Evolution,” in Introduction to Bioinformatics, 
4th ed. Oxford, United Kingdom: Oxford University Press, 2014, ch. 2, pp. 93–94
[2]	“Basics of the CFTR protein,” Cystic Fibrosis Foundation, 
https://www.cff.org/research-clinical-trials/basics-cftr-protein (accessed Apr. 9, 2025).
[3]	“Cystic fibrosis,” Mayo Clinic, 
https://www.mayoclinic.org/diseases-conditions/cystic-fibrosis/symptoms-causes/syc-20353700 (accessed Apr. 9, 2025).
[4]	“CFTR,” Johns Hopkins Cystic Fibrosis Center, https://hopkinscf.org/knowledge/cftr/ 
(accessed Apr. 9, 2025).
[5]	Claustres M, Theze C, des Georges M, et al. CFTR-France, a national relational 
patient-database for sharing genetic and phenotypic data associated with rare CFTR 
variants. Human Mutation. 2017; 38: 1297–1315. https://doi.org/10.1002/humu.23276
[6]	The Clinical and Functional TRanslation of CFTR (CFTR2); available at http://cftr2.org.
[7]	Jupyter nbviewer, 
https://nbviewer.org/github/NBISweden/workshop-python/blob/ht18/assignment/Solutions_project.ipynb 
[8]	Google Deepmind AlphaFold, https://deepmind.google/technologies/alphafold/

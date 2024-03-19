#!/bin/bash

#creating networks 1.1 for 10 different threshholds on the test roary out of 31 strepto strains
# for i in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
# do
#     python src/create_gene_network.py test/roary/gene_presence_absence.csv 13 $i data/graphs/1.1_gene-gene_presence_${i}_strepto_31.gml
# done

#retriving data from patric
bash src/data_Extraction/PATRIC_extract_data.sh

#running roary to construct pangenome of each species
bash src/create_pangenome.sh data/genomes/Acinetobacter_baumannii/ Acinetobacter data/pangenomes/Acinetobacter_baumannii #running
bash src/create_pangenome.sh data/genomes/Campylobacter_coli/ Campylobacter data/pangenomes/Campylobacter_coli
bash src/create_pangenome.sh data/genomes/Campylobacter_jejuni/ Campylobacter data/pangenomes/Campylobacter_jejuni
bash src/create_pangenome.sh data/genomes/Enterobacter_cloacae/ Enterobacter data/pangenomes/Enterobacter_cloacae
bash src/create_pangenome.sh data/genomes/Enterococcus_faecium/ Enterococcus data/pangenomes/Enterococcus_faecium

bash src/create_pangenome.sh data/genomes/Pseudomonas_aeruginosa/ Pseudomonas data/pangenomes/Pseudomonas_aeruginosa
#!/bin/bash

#creating networks 1.1 for 10 different threshholds on the test roary out of 31 strepto strains
for i in 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
do
    python src/create_gene_network.py test/roary/gene_presence_absence.csv 13 $i data/graphs/1.1_gene-gene_presence_${i}_strepto_31.gml
done
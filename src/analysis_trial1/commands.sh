#!/bin/bash

# * streptomycin
# * sulfamethoxazole
# * tetracycline
# * cefalothin
# * trimethoprim
# * amoxicillin
# * ampicillin
# * levofloxacin
# * ciprofloxacin

# -- cpying the tetracycline analysis notebook and replacing the antibiotic name
for antibiotic in streptomycin sulfamethoxazole cefalothin trimethoprim amoxicillin ampicillin levofloxacin ciprofloxacin; do
    cp Escherichia_coli_tetracycline_analysis.ipynb Escherichia_coli_${antibiotic}_analysis.ipynb
    sed -i "s/tetracycline/${antibiotic}/g" Escherichia_coli_${antibiotic}_analysis.ipynb
done

# -- rm if needed to cp again
for antibiotic in streptomycin sulfamethoxazole cefalothin trimethoprim amoxicillin ampicillin levofloxacin ciprofloxacin; do
    rm Escherichia_coli_${antibiotic}_analysis.ipynb
done
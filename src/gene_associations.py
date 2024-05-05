'''
This module is to compute different statistical measures to associate genes with the phenotype.  
important considerations: setting a species and a drug of interest.

The main statistical associations will be:  
- Mutual Information
- Chi-Square test
- ANOVA test

The main ML models to infer feature importance will be:
- SVM ensemble

Attributes
-----------
- species: the species name
- drug: the drug of interest

Derived attributes:
--------------------
- presence_path: the path to the presence matrix
- pheno_path: the path to the phenotype file

- presence_matrix: the presence matrix of the species
- labeled_matrix: the labeled matrix of the species (maybe create a function for that)


'''
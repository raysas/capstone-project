# Capstone Project

## Organization

* 🗂️src:
  * 📁analysis:

    * 📄 phenotype.ipynb: exploring and manipulating all the pheno data
    * 📄 memoizing_dataframes.ipynb
    * 📄{species}_{drug}_analysis.ipynb: Jupyter notebook with analysis when labels are taken for this {drug}. Analysis consists of:
      * Extracting the labeled matrix for this drug & species
      * Performing statistical associations between the features and the labels
      * Performing feature selection 
      * Computing co-occurence LOR
      * Constructing network
      * Network analysis
  * 📄gene_associations.py
  * 📄network_analysis.py
  * 📄network_construction.py
  * 📄cluster_analysis.py
  * 📄data_analysis.py
* 🗂️data:
  * 📁phenotypes:
    * 📄{species}_{drug}.csv: Phenotypes for this drug and species (SIR readings) extracted from xlsx
  * 📁processed_phenotypes:
    * 📄{species}_{drug}.csv: Processed phenotypes for this drug and species
  * 📁genomes:
    * 📁{species}: pan genome analysis pipeline output (w\o eggnog)
  * 📁processed_matrices:
    * 📄{species}_{drug}.csv: Labeled matrix for this drug and species (concatenated X and y)
  * 📁presence_matrices:
    * 📄{species}.csv: Presence matrix for this species
  * 📄DatasetS1.json
  * 📄SIR_readings.xlsx
* 🗂️results:
  * 📁{species}_{drug}:
    * 📄{association_type}_top_100.csv
    * 📄{species}_{drug}_network.graphml
    * 📄annotated_{species}_{drug}_network.graphml
* 🗂️figures
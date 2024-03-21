## Data collection

- [X] collect fasta genomes rom PATRIC:
    - [X] Acinetobacter baumannii - deleted
    - [X] Campylobacter coli - deleted
    - [X] Campylobacter jejuni - deleted
    - [X] Enterobacter cloacae - deleted
    - [X] Enterrococcus faecium - deleted
    - [X] Escherichia coli - deleted
    - [X] Klebsiella pneumoniae
    - [X] Neisseria gonorrhoeae
    - [X] Pseudomonas aeruginosa
    - [X] Salmonella enterica
    - [X] Staphylococcus aureus
    - [X] Streptococcus pneumoniae
- [ ] annotate genomes with prokka
    - [X] Acinetobacter baumannii
    - [X] Campylobacter coli
    - [X] Campylobacter jejuni 
    - [X] Enterobacter cloacae
    - [X] Enterrococcus faecium
    - [ ] Escherichia coli - INTERRUPTED
    - [ ] Klebsiella pneumoniae
    - [ ] Neisseria gonorrhoeae
    - [ ] Pseudomonas aeruginosa
    - [ ] Salmonella enterica
    - [ ] Staphylococcus aureus
    - [ ] Streptococcus pneumoniae
- created pangenomes from roary
    - [ ] Acinetobacter baumannii _interrupted_
    - [X] Campylobacter coli
    - [ ] Campylobacter jejuni 
    - [ ] Enterobacter cloacae
    - [ ] Enterrococcus faecium
    - [ ] Escherichia coli
    - [ ] Klebsiella pneumoniae
    - [ ] Neisseria gonorrhoeae
    - [ ] Pseudomonas aeruginosa
    - [ ] Salmonella enterica
    - [ ] Staphylococcus aureus
    - [ ] Streptococcus pneumoniae

## Tasks:

- [X] create script to extract phenotypes and save each species-drug comb in a csv file in data/phenotypes
- [ ] fix branches in the workflow
- [ ] create a script that calculates gene properties:
    - [X] compute log odds resistance
    - [X] make a script for nodes_features or gene_features to import in network analysis
- [X] figure out inteactions between genes: corr


## Bugs

- [ ] roary exit status 1 - killing the workflow
- [ ] pangenome pipeline is giving errors
# Pangenomics Analysis Pipeline

This repository contains an automated pangenomics analysis pipeline. 

## Table of Contents
- [Getting Started](#getting-started)
  - [Installing Dependencies](#installing-dependencies)
  - [Running the Pipeline](#running-the-pipeline)
- [Accepted Files](#accepted-input-files)

## Getting Started

### Installing Dependencies

Before running the pipeline, you need to ensure that the following dependencies are installed:

- **Python 3**: Python 3 is a fundamental requirement for the pipeline. You can download and install Python 3 from the [official Python website](https://www.python.org/downloads/).

- **BV-BRC CLI**: BV-BRC CLI is a command-line tool from the Biocomputing and Visualization Resource Center. You can install it using pip:

       pip install bv-brc
    
    Alternatively, you can install it using conda:
    
        conda install -c bioconda bv-brc-cli

    
    For installation from source, please visit the [BV-BRC CLI GitHub page](https://github.com/bv-brc/bv-brc-cli) for detailed instructions.
  
- **CD-HIT**: CD-HIT is a sequence clustering program. You can download and install it by following the instructions on the [CD-HIT GitHub page](https://github.com/weizhongli/cdhit).

- **EggNOG-mapper**: EggNOG-mapper is used for functional annotation of genes. You can install it by following the instructions on the [EggNOG-mapper GitHub page](https://github.com/eggnogdb/eggnog-mapper).

Make sure to install these dependencies before running the pipeline.

### Running the Pipeline

To start the pangenomics analysis pipeline, you should run the `workflow.sh` script located in the "codes" directory. 

Follow these steps to run the pipeline:

1. Open your command-line interface (terminal).

2. Navigate to the directory where the repository is cloned:
   ```bash
   cd /path/to/your/repository

3. Execute the workflow.sh script:
    ```bash
    bash codes/workflow.sh

The script will prompt you to enter the path to the directory containing the genome IDs file(s). Please provide the full path to the directory as instructed. Make sure the files containing the genome IDs in the repository have the correct format and content as mentioned in [Accepted Input Files](#accepted-input-files). 

The pipeline will then start processing the data and generate the results.

Make sure you have all the dependencies installed, as mentioned in the [Installing Dependencies](#installing-dependencies), before running the pipeline. If you encounter any issues or have questions during the process, feel free to create an issue on the GitHub repository for assistance.

## Accepted Genome ID(s) Files

To use the pangenomics analysis pipeline, ensure that your input files meet the following requirements:

- **File Format**: Your file(s) should be in CSV format.
- **Column with Genome IDs**: The first column of each input file must contain all the genome IDs of a species. This column is essential for the pipeline to identify and process the genomes.

Make sure your input files adhere to these specifications to successfully run the pipeline.

Please refer to the [Running the Pipeline](#running-the-pipeline) section for instructions on running the pipeline after ensuring your files meet the criteria.

## Questions or Issues

If you have any questions or encounter issues while using the pipeline, please create an issue on the GitHub repository for assistance.



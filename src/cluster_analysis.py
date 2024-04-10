#!/bin/env/python

'''
This script contains contains scripts to parse the pangenome pipleine output files and get information about clusters
'''

import requests
import pandas as pd
import re

def get_cluster_representatives(clstr_path:str, save_csv:bool=False)->pd.DataFrame:
    '''
    Take a CD-HIT clstr output file and return a dictionary with cluster number as key and representative sequence as value.
    Optionally saves the dictionary as a csv file.

    parameters:
    ----------
    clstr_path: str, path to CD-HIT clstr file
    save_csv: bool, if True saves the dictionary as a csv file (optional)

    return:
    -------
    df: pd.DataFrame, data frame with cluster number as key and representative sequence as value

    description:
    ------------

    CD-HIT cluster file parser:
        .clstr file format is:

        >Cluster 489
        0	552aa, >fig|195.2069.peg.1050... *
        >Cluster 490
        0	551aa, >fig|195.2045.peg.1513... *
        1	530aa, >fig|195.2053.peg.1024... at 84.34%
        2	536aa, >fig|195.2186.peg.1791... at 94.40%
        3	541aa, >fig|195.2242.peg.678... at 94.82%
        >Cluster 491
        0	501aa, >fig|195.2049.peg.1588... at 99.80%
        1	551aa, >fig|195.2166.peg.1287... *
        2	453aa, >fig|195.2206.peg.1626... at 99.56%
        3	453aa, >fig|195.2226.peg.1423... at 99.78%

        Each cluster has a number, here representing a CDS; each entry starts with a >Cluster line followed by the cluster number
        Under each cluster there are all entries for that cluster in each sample genome, based on a sequence identity (here 80% from pipeline)
        One entry under a cluster is the representative sequence, marked with an asterisk (*), this is the entry we want to get its gene name from PATRIC 
        p.s., 195.2029.peg.1780 is the gene name for cluster 0

        The cluster parser aims to match each cluster number to its representative sequence and get the gene name from PATRIC using api requests
    '''
    with open(clstr_path, 'r') as clstr_file:

        found_representative=False #flag to know if we found a representative for the clstr number
        cluster='' #initialize cluster number

        cluster_dict={} #initialize dictionary to store cluster number and representative sequence

        for line in clstr_file:

            if line.startswith(">"): #if its a cluster number file, save the cluster number for the next iteration
                cluster=line[1:].strip()
                found_representative=False #reset to false in order to find rep

            elif not found_representative:
                if "*" in line:
                    found_representative=True
                    representative=line.split(",")[1].replace('... *', '').strip()[1:]
                    representative=representative.split("|")[1]
                    # print(representative)
                    cluster_dict[cluster]=representative

            else:
                continue

    if save_csv:
        cluster_df=pd.DataFrame(cluster_dict.items(), columns=['cluster', 'gene_representative'])

        clstr_basename=clstr_path.split("/")[-1].split(".")[0]
        cluster_df.to_csv(f'{clstr_basename}.csv', index=False)

    df=pd.DataFrame(cluster_dict.items(), columns=['cluster', 'gene_representative'])

    return df

def get_representative_products(clstr_fasta_path:str)->pd.DataFrame:
    '''
    Takes a CD-HIT fasta output and returns a dataframe that matches each CDS PATRIC ID with its product name

    the fasta output is of this form:

    >fig|195.2024.peg.83 Putative oxidoreductase ferredoxin-type protein, clusters with CPO
    MNFSQISDACVKCGKCIPVCTIHEVNRDETTSPRGFLDLLAAYKEEKLELDKEAKKIFES
    CFLCTNCVEVCPSKLRVDNVIEEVRYDIAKKFGIAWYKKIIFFFLRRRKILDLVAKLGYV
    FQSCAFKIQSQDQNVGMKAKFSMPFVKKGRLLTSFNKKSFLNSNPDFIDNGGEKTVGFFV
    GCLANYFYIDTANAVLKIAKEVKINVDLMKEQVCCGAPQFFTGDFKSVEILAKKNIEYFE
    KKLEKLDAIIIPEATCSAMLKIDLEHFFNMQNEPEWAKRAQKISSRIYMASEYFYKFTNL
    KELLESKKKLNYSITYHDPCHARKMQGVFKEPRELLKANYHFVEMSNPNACCGFGGVSMQ
    TDYYDRALSVGLKKASMIDESKACVVSAECSACRMQISNALEQNSSKAIFASPLELIAKA
    L
    >fig|195.2024.peg.542 Septum-associated rare lipoprotein A
    MKPYTINGKTYYPTVVSVGETADGIASWYGPGFHGKKTSNGETYNQNGLTAAHKTLPMNT
    ILKVTNLNNNRQVTVRVNDRGPFVNNRIIDLSKGAASQIDMIAAGTAPVRLEVIGFGSAN
    SGNNVVHSNINYGASGGIANNGQIYEGGNFMVQIGAFKNPSGAQTIASRYKTYRTYSSTI
    RKSSVDGLSRVFLTGFRSEEEARDFAASGAFAGAFVVRE

    The aim is to match 195.2024.peg.542 with Septum-associated rare lipoprotein A in teh dataframe

    param:
    ------
    - clstr_fasta_path: str, path of the fasta output

    return:
    -------
    - df: pd.DataFrame, df of columns gene_representative and product_name
    '''

    dict={}

    with open(clstr_fasta_path,'r') as f:
        for line in f.readlines():
            if line.startswith(">"):
                pattern=">fig.(\d{3}\.\d{4}.peg.\d+) (.+)"
                gene_representative=re.match(string=line, pattern=pattern).group(1)
                product_name=re.match(string=line, pattern=pattern).group(2)
                dict[gene_representative]=product_name
    

    df = pd.DataFrame(dict.items(), columns=['gene_representative', 'product_name'])
    return df

def combine_cluster_product(clstr_rep_df:pd.DataFrame, rep_prod_df:pd.DataFrame)->pd.DataFrame:
    '''
    Combines the cluster representative dataframe with the product name dataframe

    param:
    ------
    - clstr_rep_df: pd.DataFrame, dataframe with cluster number and gene representative (get_cluster_representatives() output)
    - rep_prod_df: pd.DataFrame, dataframe with gene representative and product name (get_representative_products() output)

    return:
    -------
    - df: pd.DataFrame, dataframe with cluster number, gene representative and product name
    '''

    df=pd.merge(clstr_rep_df, rep_prod_df, on='gene_representative', how='left')
    df.drop(columns='gene_representative', inplace=True)
    return df

def get_cluster_pan_gene_class(pan_annot_path:str)->pd.DataFrame:
    '''
    Takes a pangenome annotation file and returns a dataframe with cluster number and gene class
    This annotation file is a <species>_pangenome.csv file output from the pangenome analysis pipeline

    param:
    ------
    - pan_annot_path: str, path to the pangenome annotation file

    return:
    -------
    - pan_df: pd.DataFrame, dataframe with cluster number and gene class
    '''
    with open(pan_annot_path, 'r') as f:
        pan_df=pd.read_csv(f, index_col=0)
        pan_df.drop(pan_df.columns[[1]], axis=1, inplace=True)
    return pan_df


def main():
    clstr_path="../pangenome-repo/Pangenome-Analysis-Workflow/codes/Campylobacter_coli/cdhit_test.fatsa.clstr"
    freq_path="../pangenome-repo/Pangenome-Analysis-Workflow/codes/Campylobacter_coli/Campylobacter_coli_cluster_frequencies.csv"
    pan_annot_path='../pangenome-repo/Pangenome-Analysis-Workflow/codes/Campylobacter_coli/Campylobacter_coli_pangenome.csv'
    clstr_fasta_path='../pangenome-repo/Pangenome-Analysis-Workflow/codes/Campylobacter_coli/Campylobacter_coli.fasta'

    #saving df as csv in data/cluster_descriptions/
    df=get_cluster_representatives(clstr_path)
    df.to_csv("../data/cluster_descriptions/Campylobacter_coli_cluster_representatives.csv", index=False)

    df=get_representative_products(clstr_fasta_path)
    df.to_csv("../data/cluster_descriptions/Campylobacter_coli_representatives_products.csv", index=False)

    df=combine_cluster_product(get_cluster_representatives(clstr_path), get_representative_products(clstr_fasta_path))
    df.to_csv("../data/cluster_descriptions/Campylobacter_coli_cluster_products.csv", index=False)

    df=get_cluster_pan_gene_class(pan_annot_path)
    df.to_csv("../data/cluster_descriptions/Campylobacter_coli_cluster_pan_gene_class.csv", index=False)
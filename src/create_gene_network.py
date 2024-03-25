#!/bin/env/python

import pandas as pd 
import networkx as nx
from typing import Tuple
import os
import sys

def read_df(file_path: str) -> pd.DataFrame:
    '''this function reads a csv file and returns a dataframe
    input:
        - file_path: (str) path to the csv file
    output:
        - df: (pd.DataFrame) dataframe read from the csv file
    '''

    if not os.path.exists(file_path):
        print(f'file {file_path} does not exist')
        return None
    df = pd.read_csv(file_path)
    return df

def collect_data(df: pd.DataFrame, sample_col: int=13, threshold: float = 0.5) -> Tuple[pd.DataFrame, pd.DataFrame]:
    '''this function takes a raw dataframe and returns only the genes as rows and samples as columns in a binary matrix
    - saves all the info in a seperate metadata dataframe
    - removes all the genes that are not present in mroe than a threshhold percentage of samples
    - returns the binary matrix and the metadata dataframe

    input:
        - df: (pd.DataFrame) raw dataframe read from csv
        - sample_col: (int) the col number whre samples start
        - threshold: (float) the percentage of samples a gene needs to be present in to be kept
        
    output:
        - df: (pd.DataFrame) binary matrix of genes and samples
        - metadata_df: (pd.DataFrame) metadata dataframe with all the info from the raw dataframe
    
    '''
    df.set_index(df.columns[0], inplace=True)
    SAMPLE_NO = df.shape[1] - sample_col

    df = df[df['No. isolates'] > (threshold * SAMPLE_NO)]

    metadata_df = df.iloc[:, 0:sample_col]
    df=df.drop(df.columns[0:sample_col], axis=1)
    df = df.fillna(0)
    df= df.where(df == 0, 1)

    return df, metadata_df


def create_adj_matrix(df: pd.DataFrame, edge_treshhold=0, samples=31) -> pd.DataFrame:
    '''this function takes a binary matrix of genes and samples
    gets an adj matrix of genes x genes where
    Aij= number of samples where gene i and gene j are both present
    (can be performed by matrix multiplication - trace on paper to understand why this works)

    input:
        - df: (pd.DataFrame) binary matrix of genes and samples
    output:
        - G: (nx.Graph) network of gene-gene presence
    '''

    adj_matrix = df.dot(df.T)
    adj_matrix = adj_matrix.astype(int)

    G = nx.from_pandas_adjacency(adj_matrix)
    G.remove_edges_from(nx.selfloop_edges(G))

    for edge in list(G.edges):
        print(f"weight: {G.get_edge_data(*edge)['weight']}, edge_treshhold: {edge_treshhold * samples}")
        if G.get_edge_data(*edge)['weight'] < edge_treshhold * samples:
            G.remove_edge(*edge)

    #removing nodes that have no edges (since already removed edges and self loops)
    G.remove_nodes_from(list(nx.isolates(G)))

    return G

create_gml = lambda G, file_path: nx.write_gml(G, file_path)

def workflow(file_path: str, sample_col: int, node_threshold: float, edge_threshold:float, gml_file_path: str) -> None:
    '''this function is the main workflow for the gene presence network
    input:
        - file_path: (str) path to the csv file
        - sample_col: (int) the col number whre samples start
        - node_threshold: (float) the percentage of samples a gene needs to be present in to be kept
        - edge_threshold: (float) the minimum weight to consider an edge
        - gml_file_path: (str) path to save the gml file
    output:
        - None
    '''
    df = read_df(file_path)
    if df is None:
        print('Workflow failed at step 1/4')
        return
    df, metadata_df = collect_data(df, sample_col, node_threshold)
    G = create_adj_matrix(df, edge_threshold)
    create_gml(G, gml_file_path)

def main():

    if len(sys.argv) != 6:
        print('Usage: python create_gene_network.py <file_path> <sample_col> <node_threshold> <edge_threshold> <gml_file_path>')
        return
    
    file_path = sys.argv[1]
    sample_col = int(sys.argv[2])
    node = float(sys.argv[3])
    edge = float(sys.argv[4])
    gml_file_path = sys.argv[5]
    workflow(file_path, sample_col, node, edge, gml_file_path)


if __name__==main():
    main()
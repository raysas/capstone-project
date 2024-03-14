'''
This script is intended to compute correlations, associations and other metrics for network features
'''

import os
import sys
import pandas as pd
import networkx as nx
import numpy as np

def _log_odds(df: pd.DataFrame) -> float:
    '''
    This helper function takes a 2x2 contingency table and returns the log odds ratio.
    The contingency matrix is of this form: #make for gene absence/precense and resistant/susceptible
    |           | gene absent | gene present |
    |-----------|-------------|--------------|
    |resistant  |    a        |     b        |
    |susceptible|    c        |     d        |

    the log odds ratio is calculated as:
        $log(a*d/b*c)$
        which is the log of the odds of the gene being present in resistant samples over the gene being present in susceptible samples
    
    param:
        - df: (pd.DataFrame) 2x2 contingency table
    output:
        - log_odds: (float) log odds ratio
    '''
    a = df.iloc[0,0]
    b = df.iloc[0,1]
    c = df.iloc[1,0]
    d = df.iloc[1,1]
    # if any of the values is 0, add 0.5 to all values to avoid division by 0 or getting a log of 0
    if a*d == 0 or b*c == 0:
        a+=0.5; b+=0.5; c+=0.5; d+=0.5
    log_odds = np.log((a*d)/(b*c))
    return log_odds

def _label_samples(pheno_df: pd.DataFrame) -> :
    return ([],[])

def _count_presence_matrix(df: pd.DataFrame) -> int:
    return
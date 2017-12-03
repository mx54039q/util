#coding:utf-8
import numpy as np

"""
    Linear Regression Analysis.   
"""

def lra(feature_matrix):
    """
    Parameters
    ----------
    feature_matrix : (N, M) array
        M dimensions features for N identities  
    
    Returns
    -------
    output : (M, N) array
        relection matrix.
    """
    W = np.linalg.pinv(feature_matrix)
    return W

#coding:utf-8
import cv2
import numpy as np
from skimage.feature import local_binary_pattern as lbp

"""
   High Dimension Local Binary Pattern.   
"""

def hdlbp(img,P,R,cell_size,fmt='default'):
    """
    Parameters
    ----------
    img : (N, M) array
        Graylevel image.
    P : int
        Number of circularly symmetric neighbour set points (quantization of
        the angular space).
    R : float
        Radius of circle (spatial resolution of the operator).
    cell_size : int
        block size of lbp cell
    fmt : {'default', 'ror', 'uniform', 'var'}
        Method to determine the pattern.
        * 'default': original local binary pattern which is gray scale but not
            rotation invariant.
        * 'ror': extension of default implementation which is gray scale and
            rotation invariant.
        * 'uniform': improved rotation invariance with uniform patterns and
            finer quantization of the angular space which is gray scale and
            rotation invariant.
        * 'nri_uniform': non rotation-invariant uniform patterns variant
            which is only gray scale invariant [2].
        * 'var': rotation invariant variance measures of the contrast of local
            image texture which is rotation but not gray scale invariant.
    
    Returns
    -------
    output : 1-D array
        HDLBP feature.
        
    References
    ----------
    .. [1] Multiresolution Gray-Scale and Rotation Invariant Texture
           Classification with Local Binary Patterns.
           Timo Ojala, Matti Pietikainen, Topi Maenpaa.
           http://www.rafbis.it/biplab15/images/stories/docenti/Danielriccio/\
           Articoliriferimento/LBP.pdf, 2002.
    .. [2] Face recognition with local binary patterns.
           Timo Ahonen, Abdenour Hadid, Matti Pietikainen,
           http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.214.6851,
           2004.
    """
    
    lbpTrain = calHistogram(lbp(img,P,R),cell_size)
    #lbpTrain_2 = np.array([calHistogram(lbp(img,8,2),19,16) for img in trainimg1])
    #lbpTrain_3 = np.array([calHistogram(lbp(img,8,2),14,12) for img in trainimg1])
    #lbpTrain = np.hstack((lbpTrain_1,lbpTrain_2,lbpTrain_3))
    
    return lbpTrain
    
    
def calHistogram(img, cell_size=4):
    """
    Parameters
    ----------
    img : (N, M) array
        lbp result image.
    cell_size : int
        block size of lbp cell
    
    Returns
    -------
    output : 1-D array
        HDLBP feature.
    """
    
    H,W = img.shape[0]/cell_size , img.shape[1]/cell_size
    img = img.astype('float32')
    Histogram = np.zeros((H*W,128))
    for i in range(H):
        for j in range(W):       
            mask = img[i*cell_size: (i+1)*cell_size,j*cell_size :(j+1)*cell_size]
            hist = cv2.calcHist([mask],[0],None,[128],[0.,255.])
            Histogram[i*W+j,:] = hist.flatten()
    return Histogram.flatten()
    
    
    
    
    
    
    
    
    

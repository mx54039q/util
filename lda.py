#coding:utf-8
import numpy as np

def LDA(x,y,dimension):
    """
    x:m*n matrix, m for feature number, n for feature size
    y:n vector, label for x
    dimension: new feature dimension
    """
    d = x.shape[1]
    Sw = np.zeros((d, d), dtype=np.float32)
    Sb = np.zeros((d, d), dtype=np.float32)
    c = len(np.unique(y))
    if dimension > (c-1):
        dimension = c-1
    elif dimension <= 0:
        dimension = c-1
    meanTotal = x.mean(axis=0).reshape(1,-1)
    for i in range(0,c):
        Xi = x[np.where(y==i)[0],:]
        meanClass = np.mean(Xi, axis = 0).reshape(1,-1)
        Sw = Sw + np.dot((Xi-meanClass), (Xi-meanClass).T)
        Sb = Sb + Xi.shape[0] * np.dot((meanClass - meanTotal), (meanClass - meanTotal).T)
    eigenvalues, eigenvectors = np.linalg.eig(np.linalg.pinv(Sw)*Sb)
    idx = np.argsort(-eigenvalues.real)
    eigenvalues, eigenvectors = eigenvalues[idx], eigenvectors[:,idx]
    eigenvalues = np.array(eigenvalues[0:num_components].real, dtype=np.float32, copy=True)
    eigenvectors = np.matrix(eigenvectors[0:,0:num_components].real, dtype=np.float32, copy=True)
    features = []
    for x in X:
        xp = self.project(x.reshape(-1,1))
        features.append(xp)
    

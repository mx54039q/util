#coding:utf-8
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# 先用PCA进行降维, 再使用t-sne
data_pca = PCA(n_components=50).fit_transform(data)
data_pca_tsne = TSNE(n_components=2).fit_transform(data_pca)

# 根据类别显示
label = range(7)*80 # 每个remote code一个颜色
plt.figure()
plt.scatter(data_pca_tsne[:, 0],data_pca_tsne[:, 1],s=55, c=label, marker='o')
plt.show()

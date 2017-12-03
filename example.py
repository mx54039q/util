#coding:utf-8
import numpy as np
import lra
import hdlbp
import cv2

gallery = np.loadtxt('gallery.txt', dtype = 'string', delimeter = ',')
probe = np.loadtxt('probe.txt', dtype = 'string', delimeter = ',')

#Construct gallry_feature:m dimensions features for n identities 
gallery_feature = np.zeros((n, m))
for i in range(gallery.shape[0]):
    img = cv2.imread(gallery[i],0)
    gallery_feature[i] = hdlbp(img, P=8, R=2, cell_size=4)
    
#Construct reflection matrix
W = lra(gallery_feature)
    
#Predict Probe
for i in range(probe.shape[0]):
    img = cv2.imread(probe[i],0)
    ifeature = np.dot(hdlbp(img, P=8, R=2, cell_size=4), W)
    ilabel = np.argmax(ifeature)
    print('Predict Label: %d' % (ilabel))

#coding:utf-8
import cv2
import numpy as np
import pandas as pd

def get_label(feat,ides):
    bf = cv2.BFMatcher()
    label = []
    for i in range(149):
        des = feat[i]
        count = 0
        matches = bf.knnMatch(des, ides, k=2)
        count = 0
        for m, n in matches:  
            if m.distance < 0.75 * n.distance:  
                count += 1
        label.append(count)
    return np.argmax(label)
    
def sift_classifier():
    gallery = np.loadtxt('gallery.txt',dtype='string',delimiter=' ')
    probe = np.loadtxt('probe.txt',dtype='string',delimiter=' ')
    probe = pd.DataFrame(probe,columns=['path','ori_pose','ori_ill'])
    probe_pose = probe[probe.ori_pose=='050'].values
    label = range(149)*19
    feat_gallery = []
    sift = cv2.SIFT()
    for i in range(149):
        name = 'ccbr_gallery/'+gallery[i,0][3:-3]+'jpg'
        img = cv2.imread(name,0)
        k , des = sift.detectAndCompute(img,None)
        feat_gallery.append(des)
    count = 0
    for i in range(probe_pose.shape[0]):
        if(iset == 'ccbr'):name = 'ccbr_probe/'+probe_pose[i,0][:-3]+'jpg'
        else:name = 'cpf_probe/'+probe_pose[i,0][:-3]+'bmp'
        img = cv2.imread(name,0)
        ik , ides = sift.detectAndCompute(img,None)
        ilabel = get_label(feat_gallery,ides)
        if(ilabel == label[i]): count += 1
        print('Acc: %d / %d' % (count,i+1))

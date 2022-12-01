# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 10:07:06 2021

@author: Andy C
"""


import cv2 as cv
import os
import pydicom
import numpy as np


def convert_opt(img, target_type_min, target_type_max, target_type):
    imin = img.min()
    imax = img.max()
    
    a = (target_type_max - target_type_min) / (imax - imin)
    b = target_type_max - a * imax
    new_img = (a * img + b).astype(target_type)
    return new_img


inputdir = 'D:\\exp_folder\\brain_1\\canny - Copy\\'
outdir = 'D:\\exp_folder\\brain_1\\cannycont\\'

test_list = [ f for f in  os.listdir(inputdir)]

for f in test_list[:10]:   # remove "[:10]" to convert all images 
    ds = cv.imread(inputdir + f) # read dicom image
    gray=cv.cvtColor(ds,cv.COLOR_BGR2GRAY)
    c=cv.resize(gray,(260,320),interpolation=1)
    cv.imwrite(outdir + f.replace('.png','.png'),c) # write png image
    
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 11:33:59 2021

@author: Andy C
"""
import numpy as np


class merging:
    def merg_seg(mag,azi,pol):#if not equal then return false message
        mag=merging.convert(mag,0,255,np.uint8)
        azi=merging.convert(azi,0,255,np.uint8)
        pol=merging.convert(pol,0,255,np.uint8)
        if mag.shape!= azi.shape or mag.shape != pol.shape or azi.shape != pol.shape:
            return -1
        else:
            merged_ar=np.zeros(mag.shape)
            i=0
            while(i<merged_ar.shape[0]):#slide
                j=0
                while(j<merged_ar.shape[1]):#row
                    k=0
                    while(k<merged_ar.shape[2]):#colum
                        if azi[i][j][k]<=30:
                            merged_volume=azi[i][j][k]
                        else:                                
                            mag_v=mag[i][j][k]*0.4
                            pol_v=pol[i][j][k]*0.6
                            merged_volume=(mag_v+pol_v).astype(np.uint8)
                        merged_ar[i][j][k]=merged_volume
                        
                        k+=1
                    j+=1
                i+=1
            return merged_ar
            
    def convert(img, target_type_min, target_type_max, target_type):
        imin = img.min()
        imax = img.max()
    
        a = (target_type_max - target_type_min) / (imax - imin)
        b = target_type_max - a * imax
        new_img = (a * img + b).astype(target_type)
        return new_img
        
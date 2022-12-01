# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 19:21:12 2021

@author: Andy C
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 18:32:21 2021

@author: Andy C
"""
import math
import numpy as np
from scipy import signal as sci
import scipy.linalg as la
import cv2 as cv
from derichefilter_modified import derichefilter_modified

class heissian_der:
    def gaussianblur1(data,sigma,dims):
        xx, yy, zz = np.meshgrid(dims,dims,dims)
        kernel = np.exp(-(xx**2 + yy**2 + zz**2)/(2*sigma**2))
        sum1  = sum(kernel.flatten())
        kernel = kernel/sum1
        
        # apply to sample data
        data = np.random.randint(0,255,[59,95,71],dtype='uint8')
        filtered = sci.convolve(data, kernel, mode="same")
        img = filtered.astype(np.uint8)
        return img
    
    def subtract(list1,list2):
        ans=[]
        if len(list1)!=len(list2):
            return -1
        else:
            idx=0
            i=0
            while(i<len(list1)):
                num1=list1[i]
                num2=list2[i]
                num3=num1-num2
                ans.append(num3)
                i+=1
            return ans
    
    def Hessian_Deriche_3D(rawimage, win_radius, alpha, mappingpower, nullCT):#parameter[0]=winradius,1=alpha,2=nullCT,3=mappingpower
        rsz = np.shape(rawimage)
        dim = len(rsz)
        if dim!=3:
            lambda_mag=[]
            lambda_azimuth=[]
            lambda_polarangle=[]
            lambda_sum=[]
            lambda_product=[]
            return -1
        
        rm=rsz[1]
        rn=rsz[2]
        rq=rsz[0]
                
        lambda_mag=np.ones([rq,rm,rn])*nullCT
        lambda_mag=np.ones([rq,rm,rn])*nullCT
        lambda_azimuth=np.ones([rq,rm,rn])*nullCT
        lambda_polarangle=np.ones([rq,rm,rn])*nullCT
        lambda_sum=np.ones([rq,rm,rn])*nullCT
        lambda_product=np.ones([rq,rm,rn])*nullCT
        
        #grawimage = heissian_der.gaussianblur1(rawimage,1,2*win_radius+1)
        grawimage=rawimage
        
        filters = derichefilter_modified.derichefilter_modified(alpha,win_radius,dim)
        fxx=filters[4]
        fyy=filters[5]
        fzz=filters[6]
        fxy=filters[7]
        fxz=filters[8]
        fyz=filters[9]
        
        
        ixx=sci.convolve(grawimage,fxx,mode='same')
        ixy=sci.convolve(grawimage,fxy,mode='same')
        ixz=sci.convolve(grawimage,fxz,mode='same')
        iyy=sci.convolve(grawimage,fyy,mode='same')
        iyz=sci.convolve(grawimage,fyz,mode='same')
        izz=sci.convolve(grawimage,fzz,mode='same')
        
        for z in range(0,rq):
            for x in range(0,rm):
                for y in range(0,rn):
                    cixx=ixx[z][x][y]
                    cixy=ixy[z][x][y]
                    cixz=ixz[z][x][y]
                    ciyy=iyy[z][x][y]
                    ciyz=iyz[z][x][y]
                    cizz=izz[z][x][y]
                    curh=np.array([[cixx,cixy,cixz],[cixy,ciyy,ciyz],[cixz,ciyz,cizz]])
        
                    cd, cv = la.eig(curh)
                    cd=np.sort(cd)
                    
                    curmag = (cd[0]*cd[0]+cd[1]*cd[1]+cd[2]*cd[2])**0.5
                    lambda_mag[z][x][y] = heissian_der.metricmapping(curmag,mappingpower)
                    curvec = np.array([cd[0],cd[1],cd[2]])
                    
                    cur_lbaz,cur_lbpolar = heissian_der.angle(curvec)
                    lambda_azimuth[z][x][y]=cur_lbaz
                    lambda_polarangle[z][x][y]=cur_lbpolar
                    
                    lambda_sum[z][x][y] = heissian_der.metricmapping(abs(cixx+ciyy+cizz),mappingpower)
                    lambda_product[z][x][y] = heissian_der.metricmapping(abs(np.linalg.det(curh)),mappingpower)
                    
        return [lambda_mag, lambda_azimuth, lambda_polarangle, lambda_sum, lambda_product]
    
    def metricmapping(mval,mappingpower):
        if mval>=0:
            val=math.pow(mval,1/mappingpower)
        else:
            val=-(math.pow(mval,1/mappingpower))
        return val
    
    def angle(v):
        
        azimuth=0
        polarangle=0
        if len(v)==0:
            return -1
        
        len_1=len(v)
        if len_1!=3:
            return -1
        
        x=v[0]
        y=v[1]
        z=v[2]
        
        theta = math.atan(y/(x+0.0000000001))        
        
        
        if abs(x)<=0.0000000001 and abs(y)<=0.0000000001:
            azimuth = 0
        else:
            if x>=0 and y>=0:
                azimuth = theta
            else:
                if x<0 and y>=0:
                    azimuth = math.pi-theta
                else:
                    if x<0 and y<0:
                        azimuth = math.pi+theta
                    else:
                        azimuth = 2*math.pi-abs(theta)
                    
        
        if abs(x)<=0.0000000001 and abs(y)<=0.0000000001 and abs(z)<=0.0000000001:
            polarangle=0
        else:
            phi=math.atan(z/math.sqrt(x**2 + y**2 + 0.0000000001)+math.pi/2)
            polarangle=phi
        return azimuth,polarangle

img=cv.imread("D:\\brain.png");
heissian_der.Hessian_Deriche_3D(img,1,1,1,1);

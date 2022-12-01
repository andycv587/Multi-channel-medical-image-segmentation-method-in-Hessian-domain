# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:46:11 2021

@author: Andy C
"""
import math
import numpy as np
import cv2 as cv

class derichefilter_modified:
    def f0(x,a,c0):
        F0=c0*(1+a*abs(x))*math.exp(-1*a*abs(x))
        return [F0]
    
    def f1(x,a,c1):
        F0=-c1*x*a**2*math.exp(-1*a*abs(x));
        return [F0]
        
    def f2(x,a,c2,c3):
        F0=c2*(1-c3*a*abs(x))*math.exp(-1*a*abs(x))
        return [F0]
    
    def filter_dim_1_0th_order(a,c0,radius):
        filter_1=[]
        if radius<=0:
            return -1
        rad=abs(radius)
        filter0=np.zeros([2*rad+1])
        for x in range(-rad,rad+1):
            v=derichefilter_modified.f0(x,a,c0)
            idx=x+rad
            filter0[idx]=v[0]
        filter_1.append(filter0)
        return filter_1
    
    def filter_dim_1_1st_order(a,c1,radius):
        filter_1=[]
        if radius<=0:
            return -1
        rad=abs(radius)
        filter0=np.zeros([2*rad+1])
        for x in range(-rad, rad+1):
            v=derichefilter_modified.f1(x,a,c1)
            idx=x+rad
            filter0[idx]=v[0]
        filter_1.append(filter0)
        return filter_1
    
    def filter_dim_1_2nd_order(a,c2,c3,radius):
        filter_1=[]
        if radius<=0:
            return -1
        
        rad=abs(radius)
        filter0=np.zeros([2*rad+1])
        for x in range(-rad,rad+1):
            v=derichefilter_modified.f2(x,a,c2,c3)
            idx=x+rad
            filter0[idx]=v[0]
        filter_1.append(filter0)
        return filter_1
        
    def filter_dim_2_0th_order(a,c0,radius):
        filter_1=[]
        if radius<=0:
            return -1

        rad=abs(radius)
        filter0=np.zeros([2*rad+1,2*rad+1])
        for x in range(-rad, rad+1):
            vx = np.array(derichefilter_modified.f0(x,a,c0))
            idx = x+rad
            for y in range(-rad,rad+1):
                vy=np.array(derichefilter_modified.f0(y,a,c0))
                v=vx*vy
                idy=y+rad
                filter0[idx][idy]=v
        filter_1.append(filter0)
        
        
        
        return filter_1
        
    def filter_dim_2_1st_order(a,c0,c1,radius):
        filter_1=[]
        if radius<=0:
            return -1
        
        rad=abs(radius)
        len_1=2*rad+1
        filterx=np.zeros([len_1,len_1])
        filtery=np.zeros([len_1,len_1])
        for row in range(-rad, rad+1):
            vy0=np.array(derichefilter_modified.f0(row,a,c0))
            vy1=np.array(derichefilter_modified.f1(row,a,c1))
            idy=row+rad
            for col in range(-rad,rad+1):
                vx0=np.array(derichefilter_modified.f0(col,a,c0))
                vx1=np.array(derichefilter_modified.f1(col,a,c1))
                idx = col+rad
                vx1y0 = vx1*vy0
                vx0y1 = vx0*vy1
                filterx[idy][idx]=vx1y0
                filtery[idy][idx]=vx0y1
        filter_1.append(filterx)
        filter_1.append(filtery)
        
        return filter_1
        
    def filter_dim_2_2nd_order(a,c0,c1,c2,c3,radius):
        filter_1=[]
        if radius<=0:
            return -1
        
        rad=abs(radius)
        len_1 = 2*rad+1
        filterxx=np.zeros([len_1,len_1])
        filteryy=np.zeros([len_1,len_1])
        filterxy=np.zeros([len_1,len_1])
        for row in range(-rad,rad+1):
            vy0 = np.array(derichefilter_modified.f0(row,a,c0))
            vy1 = np.array(derichefilter_modified.f1(row,a,c1))
            vy2 = np.array(derichefilter_modified.f2(row,a,c2,c3))
            idy = row+rad
            for col in range(-rad,rad+1):
                vx0 = np.array(derichefilter_modified.f0(col,a,c0))
                vx1 = np.array(derichefilter_modified.f1(col,a,c1))
                vx2 = np.array(derichefilter_modified.f2(col,a,c2,c3))
                idx = col+rad
                
                vx2y0 = vx2*vy0
                vx0y2 = vx0*vy2
                vx1y1 = vx1*vy1
                
                filterxx[idy][idx] = vx2y0
                filteryy[idy][idx] = vx0y2
                filterxy[idy][idx] = vx1y1
        
        filter_1.append(filterxx)
        filter_1.append(filteryy)
        filter_1.append(filterxy)
        
        return filter_1
        
    def filter_dim_3_0th_order(a,c0,radius):
        filter_1=[]
        if radius<=0:
            return -1
        
        rad=abs(radius)
        len_1=2*rad+1
        filter0=np.zeros([len_1,len_1,len_1])
        
        for slice_1 in range(-rad, rad+1):
            vz0=np.array(derichefilter_modified.f0(slice_1,a,c0))
            idz=slice_1+rad
            for row in range(-rad,rad+1):
                vy0=np.array(derichefilter_modified.f0(row,a,c0))
                idy=row+rad
                for col in range(-rad,rad+1):
                    vx0=np.array(derichefilter_modified.f0(col,a,c0))
                    idx=col+rad
                    vx0y0z0=vx0*vy0*vz0
                    filter0[idz][idy][idx]=vx0y0z0
        filter_1.append(filter0)
        return filter_1
        
    def filter_dim_3_1st_order(a,c0,c1,radius):
        filter_1=[]
        if radius<=0:
            return -1
        
        rad=abs(radius)
        len_1=2*rad+1
        filterx=np.zeros([len_1,len_1,len_1])
        filtery=np.zeros([len_1,len_1,len_1])
        filterz=np.zeros([len_1,len_1,len_1])
        
        for slice_1 in range(-rad,rad+1):
            vz0=np.array(derichefilter_modified.f0(slice_1,a,c0))
            vz1=np.array(derichefilter_modified.f1(slice_1,a,c1))
            idz=slice_1+rad
            
            for row in range(-rad,rad+1):
                vy0=np.array(derichefilter_modified.f0(row,a,c0))
                vy1=np.array(derichefilter_modified.f1(row,a,c1))
                idy=row+rad
                
                for col in range(-rad,rad+1):
                    vx0=np.array(derichefilter_modified.f0(col,a,c0))
                    vx1=np.array(derichefilter_modified.f1(col,a,c1))
                    idx=col+rad
                    
                    vx1y0z0 = vx1*vy0*vz0
                    vx0y1z0 = vx0*vy1*vz0
                    vx0y0z1 = vx0*vy0*vz1
                    
                    filterx[idz][idy][idx]=vx1y0z0
                    filtery[idz][idy][idx]=vx0y1z0
                    filterz[idz][idy][idx]=vx0y0z1
        
        
        filter_1.append(filterx)
        filter_1.append(filtery)
        filter_1.append(filterz)
        
        return filter_1
        
    def filter_dim_3_2nd_order(a,c0,c1,c2,c3,radius):
        filter_1=[]
        if radius<=0:
            return -1
        
        rad=abs(radius)
        len_1=2*rad+1
        filterxx=np.zeros([len_1,len_1,len_1])
        filteryy=np.zeros([len_1,len_1,len_1])
        filterzz=np.zeros([len_1,len_1,len_1])
        filterxy=np.zeros([len_1,len_1,len_1])
        filterxz=np.zeros([len_1,len_1,len_1])
        filteryz=np.zeros([len_1,len_1,len_1])
        
        for slice_1 in range(-rad,rad+1):
            vz0=np.array(derichefilter_modified.f0(slice_1,a,c0))
            vz1=np.array(derichefilter_modified.f1(slice_1,a,c1))
            vz2=np.array(derichefilter_modified.f2(slice_1,a,c2,c3))
            idz=slice_1+rad
            
            for row in range(-rad,rad+1):
                vy0=np.array(derichefilter_modified.f0(row,a,c0))
                vy1=np.array(derichefilter_modified.f1(row,a,c1))
                vy2=np.array(derichefilter_modified.f2(row,a,c2,c3))
                idy=row+rad
            
                for col in range(-rad,rad+1):
                    vx0=np.array(derichefilter_modified.f0(col,a,c0))
                    vx1=np.array(derichefilter_modified.f1(col,a,c1))
                    vx2=np.array(derichefilter_modified.f2(col,a,c2,c3))
                    idx=col+rad
                    
                    vx2y0z0=vx2*vy0*vz0
                    vx0y2z0=vx0*vy2*vz0
                    vx0y0z2=vx0*vy0*vz2
                    
                    vx1y1z0=vx1*vy1*vz0
                    vx1y0z1=vx1*vy0*vz1
                    vx0y1z1=vx0*vy1*vz1
                    
                    filterxx[idz][idy][idx]=vx2y0z0
                    filteryy[idz][idy][idx]=vx0y2z0
                    filterzz[idz][idy][idx]=vx0y0z2
                    
                    filterxy[idz][idy][idx]=vx1y1z0
                    filterxz[idz][idy][idx]=vx1y0z1
                    filteryz[idz][idy][idx]=vx0y1z1
                    
        filter_1.append(filterxx)           
        filter_1.append(filteryy)           
        filter_1.append(filterzz)           
        filter_1.append(filterxy)           
        filter_1.append(filterxz)           
        filter_1.append(filteryz)
        
        return filter_1
        
    def derichefilter_modified(alpha,radius,dim):
        if radius==0:
            filters=[]
            return -1
        if dim<=0 or dim>3:
            filters=[]
            return -1
        
        c0=(1-math.exp(-alpha))**2/(1+2*alpha*math.exp(-alpha)-math.exp(-2*alpha))
        c1=-(1-math.exp(-alpha))**3/(2*alpha**2*math.exp(-alpha)*(1+math.exp(-alpha)))
        c2=-2*(1-math.exp(-alpha))**4/(1+2*math.exp(-alpha)-2*math.exp(-3*alpha)-math.exp(-4*alpha))
        c3=(1-math.exp(-2*alpha))/(2*alpha*math.exp(-alpha))
        filters=[]
        
        if dim==1:
            filter10=np.array(derichefilter_modified.filter_dim_1_0th_order(alpha,c0,radius))
            filter11=np.array(derichefilter_modified.filter_dim_1_1st_order(alpha,c1,radius))
            filter12=np.array(derichefilter_modified.filter_dim_1_2nd_order(alpha,c2,c3,radius))
            filters.append(filter10[0])
            filters.append(filter11[0])
            filters.append(filter12[0])
            
        elif dim==2:
            filter20=np.array(derichefilter_modified.filter_dim_2_0th_order(alpha,c0,radius))
            filter21=np.array(derichefilter_modified.filter_dim_2_1st_order(alpha,c0,c1,radius))
            filter22=np.array(derichefilter_modified.filter_dim_2_2nd_order(alpha,c0,c1,c2,c3,radius))
            filters.append(filter20[0])
            filters.append(filter21[0])
            filters.append(filter21[1])
            filters.append(filter22[0])
            filters.append(filter22[1])
            filters.append(filter22[2])
            
        elif dim==3:
            filter30=np.array(derichefilter_modified.filter_dim_3_0th_order(alpha,c0,radius))
            filter31=np.array(derichefilter_modified.filter_dim_3_1st_order(alpha,c0,c1,radius))
            filter32=np.array(derichefilter_modified.filter_dim_3_2nd_order(alpha,c0,c1,c2,c3,radius))
            filters.append(filter30[0])
            filters.append(filter31[0])
            filters.append(filter31[1])
            filters.append(filter31[2])
            filters.append(filter32[0])
            filters.append(filter32[1])
            filters.append(filter32[2])
            filters.append(filter32[3])
            filters.append(filter32[4])
            filters.append(filter32[5])
            
        else:
            print('!!!!! An exception happended, check please !!!!!');
        return filters
print(derichefilter_modified.derichefilter_modified(5,5,2))
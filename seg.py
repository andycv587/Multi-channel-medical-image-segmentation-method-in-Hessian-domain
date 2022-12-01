# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 23:53:35 2021

@author: Andy C
"""
import numpy as np
import cv2 as cv

def segpic(pic,segtime=8,retreatratio=0.25,length=512,ltv=130,htv=255,enablesmoth=False):
    img=255-cv.imread(pic)
    if enablesmoth==True:
        img = cv.GaussianBlur(img,(5,5),0)
        
    gray=cv.cvtColor(img,cv.COLOR_RGB2GRAY)#convert to gray
    blank = np.zeros(gray.shape,dtype='uint8')
    looptimes=int((length-(length/segtime))/((length/segtime)-(length/segtime)*retreatratio)+1)
    croplen=int(length/segtime)
    for i in range(0,looptimes):
        lastime_i=i
        for j in range(0,looptimes):
            lastime_j=j
            if i==0 and j==0:#if its on top right cornor
                cropsl=get_part(gray,0,croplen,0,croplen,croplen,True) 
                ret, thresh = cv.threshold(cropsl,ltv,htv,cv.THRESH_BINARY)
                canny = cv.Canny(thresh,40,90)
                blank=plugin(canny,blank,0,croplen,0,croplen)
                
            else:
                startpos_i=int(lastime_i*croplen-lastime_i*(croplen*retreatratio))
                endpos_i=int(croplen+(lastime_i*(croplen-(croplen*retreatratio))))
                startpos_j=int(lastime_j*croplen-lastime_j*(croplen*retreatratio))
                endpos_j=int(croplen+(lastime_j*(croplen-(croplen*retreatratio))))
                cropsl=get_part(gray,startpos_i,endpos_i,startpos_j,endpos_j,croplen,False)
                #ret, thresh = cv.threshold(cropsl,137,255,cv.THRESH_BINARY)
                ret, thresh = cv.threshold(cropsl,ltv,htv,cv.THRESH_BINARY)
                canny = cv.Canny(thresh,40,90)
                blank=plugin(canny,blank,startpos_i,endpos_i,startpos_j,endpos_j)
    return blank

def get_part(img,start_sid_i,end_sid_i,start_sid_j,end_sid_j,lenth,first):
    res=np.zeros([lenth,lenth],dtype='uint8')
    for i in range(int(start_sid_i),int(end_sid_i)):
        for j in range(int(start_sid_j),int(end_sid_j)):
            if first==True:
                res[i][j]=img[i][j]
            else:
                res[i-start_sid_i][j-start_sid_j]=img[i][j]
    return res
    
def plugin(part,target,istart,iend,jstart,jend):
    for i in range(int(istart),int(iend)):
        for j in range(int(jstart),int(jend)):
            if target[i][j]!=255:
                target[i][j]=part[i-istart][j-jstart]
    return target


def enhence(img):
    out = 2.0 * img
     # the value greater than 255 is truncated to 255
    out[out > 255] = 255
     # 
    out = np.around(out)
    out = out.astype(np.uint8)
    return out
    
for i in range(70,255,3):
    pic='D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\resh_sum\\sum_11_0.png'
    segtime=256
    retreatratio=0.5
    length=512
    ltv=i
    htv=255
    enablesmoth=True
    print('i={}'.format(i))
    bew=segpic(pic,segtime,retreatratio,length,ltv,htv,enablesmoth)
    cv.imwrite('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\sig11o\\sum_11_0_{}.png'.format(ltv),bew)
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:15:25 2021

@author: Andy C
"""
import cv2 as cv
import numpy as np

def findconection(filepath):
    im=cv.cvtColor(255-cv.imread(filepath),cv.COLOR_BGR2GRAY)
    
    if np.size(im) == 0:
        bset=[]
        return bset

    imsz=im.shape
    mark=np.ones(imsz).tolist()
    
    bset=[]
    
    for i in range(0,imsz[0]):
        for j in range(0,imsz[1]):
            pij=[i,j]
            if im[i][j]!=0 or mark[i][j]==0:
                continue
            print('i={},j={}'.format(i,j))
            bsetij,mark = findsubconnection(im,np.array(mark),pij)
            
            if np.size(bsetij)!=0:
                bset.append(bsetij)
    
    return bset
    
def findsubconnection(im,mark,point):
    imsz=im.shape
    mksz=np.array(mark).shape
    if imsz!=mksz:
        bset=[]
        newmark=mark
        return bset, newmark
    
    bset=[]
    q_1=[]
    q_1=push(q_1,point)
    mark[point[0]][point[1]]=0
    n=0
    head=np.array([])
    while(np.array(q_1).size!=0):
        n+=1
        #if n==121338:
        print(n)
        head,q_1=pop(q_1)
        head=list(map(int, head))
        bset.append([head])
        print('head={},imsz={}'.format(head,imsz))
        id_1=positionid(head,imsz)
        p1=[]
        p2=[]
        p3=[]
        p4=[]
        p5=[]
        p6=[]
        p7=[]
        p8=[]
        
    
        if id_1==1: #top left point
            p4=[head[0],head[1]+1]
            if im[p4[0]][p4[1]]==0 and mark[p4[0]][p4[1]]==1:
                q_1=push(q_1,p4) 
                mark[p4[0]][p4[1]]=0
                  
            p5=[head[0]+1,head[1]+1] 
            if im[p5[0]][p5[1]]==0 and mark[p5[0]][p5[1]]==1:
                q_1=push(q_1,p5) 
                mark[p5[0]][p5[1]]=0
                 
            p6=[head[0]+1,head[1]] 
            if im[p6[0]][p6[1]]==0 and mark[p6[0]][p6[1]]==1:
                q_1=push(q_1,p6) 
                mark[p6[0]][p6[1]]=0
                 
                     
        elif  id_1==2: #top right point
            p6=[head[0]+1,head[1]] 
            if im[p6[0]][p6[1]]==0 and mark[p6[0]][p6[1]]==1:
                q_1=push(q_1,p6)
                mark[p6[0]][p6[1]]=0
                 
            p7=[head[0]+1,head[1]-1] 
            if im[p7[0]][p7[1]]==0 and mark[p7[0]][p7[1]]==1:
                q_1=push(q_1,p7) 
                mark[p7[0]][p7[1]]=0
                 
            p8=[head[0],head[1]-1] 
            if im[p8[0]][p8[1]]==0 and mark[p8[0]][p8[1]]==1:
                q_1=push(q_1,p8) 
                mark[p8[0]][p8[1]]=0
                 
                    
        elif  id_1==3: #bottom left point
            p1=[head[0]-1,head[1]-1] 
            if im[p1[0]][p1[1]]==0 and mark[p1[0]][p1[1]]==1:
                q_1=push(q_1,p1) 
                mark[p1[0]][p1[1]]=0
                 
            p2=[head[0]-1,head[1]] 
            if im[p2[0]][p2[1]]==0 and mark[p2[0]][p2[1]]==1:
                q_1=push(q_1,p2) 
                mark[p2[0]][p2[1]]=0
                 
            p8=[head[0],head[1]-1] 
            if im[p8[0]][p8[1]]==0 and mark[p8[0]][p8[1]]==1:
                q_1=push(q_1,p8) 
                mark[p8[0]][p8[1]]=0
                 
                     
        elif  id_1==4: # #bottom right point
            p2=[head[0]-1,head[1]] 
            if im[p2[0]][p2[1]]==0 and mark[p2[0]][p2[1]]==1:
                q_1=push(q_1,p2)
                mark[p2[0]][p2[1]]=0
                 
                     
            p3=[head[0]-1,head[1]+1] 
            if im[p3[0]][p3[1]]==0 and mark[p3[0]][p3[1]]==1:
                q_1=push(q_1,p3) 
                mark[p3[0]][p3[1]]=0   
                 
                     
            p4=[head[0],head[1]+1] 
            if im[p4[0]][p4[1]]==0 and mark[p4[0]][p4[1]]==1:
                q_1=push(q_1,p4) 
                mark[p4[0]][p4[1]]=0
                  
                     
        elif  id_1==5: # # left
            p2=[head[0]-1,head[1]] 
            if im[p2[0]][p2[1]]==0 and mark[p2[0]][p2[1]]==1:
                q_1=push(q_1,p2) 
                mark[p2[0]][p2[1]]=0
                 
                     
            p3=[head[0]-1,head[1]+1] 
            if im[p3[0]][p3[1]]==0 and mark[p3[0]][p3[1]]==1:
                q_1=push(q_1,p3)
                mark[p3[0]][p3[1]]=0
                 
                     
            p4=[head[0],head[1]+1] 
            if im[p4[0]][p4[1]]==0 and mark[p4[0]][p4[1]]==1:
                q_1=push(q_1,p4)
                mark[p4[0]][p4[1]]=0
                   
                     
            p5=[head[0]+1,head[1]+1] 
            if im[p5[0]][p5[1]]==0 and mark[p5[0]][p5[1]]==1:
                q_1=push(q_1,p5) 
                mark[p5[0]][p5[1]]=0
                 
                     
            p6=[head[0]+1,head[1]] 
            if im[p6[0]][p6[1]]==0 and mark[p6[0]][p6[1]]==1:
                q_1=push(q_1,p6) 
                mark[p6[0]][p6[1]]=0
                 
                     
        elif  id_1==6: # # top
            p4=[head[0],head[1]+1] 
            if im[p4[0]][p4[1]]==0 and mark[p4[0]][p4[1]]==1:
                q_1=push(q_1,p4) 
                mark[p4[0]][p4[1]]=0
                  
                     
            p5=[head[0]+1,head[1]+1] 
            if im[p5[0]][p5[1]]==0 and mark[p5[0]][p5[1]]==1:
                q_1=push(q_1,p5)
                mark[p5[0]][p5[1]]=0
                 
                    
            p6=[head[0]+1,head[1]] 
            if im[p6[0]][p6[1]]==0 and mark[p6[0]][p6[1]]==1:
                q_1=push(q_1,p6) 
                mark[p6[0]][p6[1]]=0
                 
                     
            p7=[head[0]+1,head[1]-1] 
            if im[p7[0]][p7[1]]==0 and mark[p7[0]][p7[1]]==1:
                q_1=push(q_1,p7)
                mark[p7[0]][p7[1]]=0
                 
                     
            p8=[head[0],head[1]-1] 
            if im[p8[0]][p8[1]]==0 and mark[p8[0]][p8[1]]==1:
                q_1=push(q_1,p8) 
                mark[p8[0]][p8[1]]=0
                  
				    
        elif  id_1==7: # # right
            p1=[head[0]-1,head[1]-1] 
            if im[p1[0]][p1[1]]==0 and mark[p1[0]][p1[1]]==1:
                q_1=push(q_1,p1)
                mark[p1[0]][p1[1]]=0
                 
                
            p2=[head[0]-1,head[1]] 
            if im[p2[0]][p2[1]]==0 and mark[p2[0]][p2[1]]==1:
                q_1=push(q_1,p2)
                mark[p2[0]][p2[1]]=0
                 
                 
            p6=[head[0]+1,head[1]] 
            if im[p6[0]][p6[1]]==0 and mark[p6[0]][p6[1]]==1:
                q_1=push(q_1,p6)
                mark[p6[0]][p6[1]]=0
                 
                 
            p7=[head[0]+1,head[1]-1] 
            if im[p7[0]][p7[1]]==0 and mark[p7[0]][p7[1]]==1:
                q_1=push(q_1,p7)
                mark[p7[0]][p7[1]]=0
                 
                     
            p8=[head[0],head[1]-1] 
            if im[p8[0]][p8[1]]==0 and mark[p8[0]][p8[1]]==1:
                q_1=push(q_1,p8)
                mark[p8[0]][p8[1]]=0
                  
                    
        elif  id_1==8: #bottom
            p1=[head[0],head[1]-1] 
            if im[p1[0]][p1[1]]==0 and mark[p1[0]][p1[1]]==1:
                q_1=push(q_1,p1)
                mark[p1[0]][p1[1]]=0
                 
                   
            p2=[head[0]-1,head[1]] 
            if im[p2[0]][p2[1]]==0 and mark[p2[0]][p2[1]]==1:
                q_1=push(q_1,p2)
                mark[p2[0]][p2[1]]=0
                 
                    
            p3=[head[0]-1,head[1]+1] 
            if im[p3[0]][p3[1]]==0 and mark[p3[0]][p3[1]]==1:
                q_1=push(q_1,p3)
                mark[p3[0]][p3[1]]=0
                  
                     
            p4=[head[0],head[1]+1] 
            if im[p4[0]][p4[1]]==0 and mark[p4[0]][p4[1]]==1:
                q_1=push(q_1,p4)
                mark[p4[0]][p4[1]]=0
                
                     
            p8=[head[0],head[1]-1] 
            if im[p8[0]][p8[1]]==0 and mark[p8[0]][p8[1]]==1:
                q_1=push(q_1,p8)
                mark[p8[0]][p8[1]]=0
                 
                     
        else: #others
            p1=[head[0]-1,head[1]-1] 
            if im[p1[0]][p1[1]]==0 and mark[p1[0]][p1[1]]==1:
                q_1=push(q_1,p1)
                mark[p1[0]][p1[1]]=0
                 
                     
            p2=[head[0]-1,head[1]] 
            if im[p2[0]][p2[1]]==0 and mark[p2[0]][p2[1]]==1:
                q_1=push(q_1,p2)
                mark[p2[0]][p2[1]]=0
                 
                     
            p3=[head[0]-1,head[1]+1] 
            if im[p3[0]][p3[1]]==0 and mark[p3[0]][p3[1]]==1:
                q_1=push(q_1,p3)
                mark[p3[0]][p3[1]]=0
                 
                                     
            p4=[head[0],head[1]+1] 
            if im[p4[0]][p4[1]]==0 and mark[p4[0]][p4[1]]==1:
                q_1=push(q_1,p4)
                mark[p4[0]][p4[1]]=0
                  
                     
            p5=[head[0]+1,head[1]+1] 
            if im[p5[0]][p5[1]]==0 and mark[p5[0]][p5[1]]==1:
                q_1=push(q_1,p5)
                mark[p5[0]][p5[1]]=0
                 
                     
            p6=[head[0]+1,head[1]] 
            if im[p6[0]][p6[1]]==0 and mark[p6[0]][p6[1]]==1:
                q_1=push(q_1,p6)
                mark[p6[0]][p6[1]]=0
                 
                     
            p7=[head[0]+1,head[1]-1] 
            if im[p7[0]][p7[1]]==0 and mark[p7[0]][p7[1]]==1:
                q_1=push(q_1,p7)
                mark[p7[0]][p7[1]]=0
                 
                     
            p8=[head[0],head[1]-1] 
            if im[p8[0]][p8[1]]==0 and mark[p8[0]][p8[1]]==1:
                q_1=push(q_1,p8)
                mark[p8[0]][p8[1]]=0
                 
                   
    #switch
    #while
    newmark=mark 
    
    
    return bset,newmark

def push(q_1,point):
    q_1.append(np.array(point))
    que=q_1
    return que
    
def pop(q_1):
    if np.size(q_1)==0:
        head=[]
        que=[]
        return head,que

    head=q_1[0]
    q_1.remove(q_1[0])
    que=q_1
    return head,que

def positionid(point,imsize):
    print('point0={},point1={}'.format(point[0],point[1]))
    if point[0]==0 and point[1]==0:
        posid=1
    else:
        if point[0]==0 and point[1]==imsize[1]-1:
            posid=2
        else:
            if point[0]==imsize[0]-1 and point[1]==imsize[1]-1:
                posid=3  
            else:
                if point[0]==imsize[0]-1 and point[1]==0:
                    posid=4  
                else:
                    if (point[0]!=0 and point[0]!=imsize[0]-1) and point[1]==0:
                        posid=5  
                    else:
                        if point[0]==0 and (point[1]!=0 and point[1]!=imsize[1]-1):
                            posid=6  
                        else:
                            if (point[0]!=0 and point[0]!=imsize[0]-1) and point[1]==imsize[1]-1:
                                posid=7  
                            else:
                                if point[0]==imsize[0]-1 and (point[1]!=0 and point[1]!=imsize[1]-1):
                                    posid=8  
                                else:
                                    posid=9  
    return posid

def filter4(ary,threshold):
    #Step1 filted
    newary=[]
    for i in ary:
        if np.array(i).size/2 > threshold:
            newary.append(i)
    return newary

def contours(ary):
    
    #plug into blank
    x=[]
    y=[]
    for i in ary:
        num_x=[]
        num_y=[]
        for j in i:
            for k in j:
                num_x.append(k[0])   
                num_y.append(k[1])      
        x.append(num_x) 
        y.append(num_y)
        
    alll=[]
    for c in range(0,np.array(x).shape[0]):
        if np.array(x).shape[0]!=np.array(y).shape[0]:
            return -1
            break
        
        i=x[c]
        j=y[c]
        mxx=np.amax(i)
        mnx=np.amin(i)
        mxy=np.amax(j)
        mny=np.amin(j)
        xls=mxx-mnx+3
        yls=mxy-mny+3
        blank=np.zeros([xls,yls])
        
        curary=[]
        for a in ary[c]:
            for b in a:
                curary.append([b[0]-mnx+1,b[1]-mny+1])
                    
        for a in curary:
            blank[a[0]][a[1]]=1
        
        bondar=[]
        a=0
        while(a<xls):
            b=0
            while(b<yls):
                curent=[]
                #if it is one then detect
                if blank[a][b]==1:
                    #then detect around:
                    if blank[a-1][b]==0 or blank[a][b-1]==0 or blank[a][b+1]==0 or blank[a+1][b]==0:
                        curent.append([a+mnx-1,b+mny-1])
                    
                b+=1
                if np.size(curent)!=0:
                    bondar.append(curent)
            a+=1
        alll.append(bondar)
        
    return alll

def drawcont(img,ary,color):#img=image not the address
    newim=img 
    
    if color=='r':
        color=[0,0,255]
    elif color=='g':
        color=[0,255,0]
    elif color=='b':
        color=[255,0,0]
    elif color=='w':
        color=[255,255,255]
    elif color=='w':
        color=[0,0,0]
    else:
        color=color
    
    for i in ary:#first cycle
        for j in i:
            for k in j:
                newim[k[0]][k[1]]=color
            
    return newim

def convert(img, target_type_min, target_type_max, target_type):
    imin = img.min()
    imax = img.max()
    
    a = (target_type_max - target_type_min) / (imax - imin)
    b = target_type_max - a * imax
    new_img = (a * img + b).astype(target_type)
    return new_img

# def detmerg(img_ary):
#     ary=img_ary
#     res_lst=[]
#     i=0
#     A=0
#     while(i<np.size(img_ary)):
#         if i!=np.size(img_ary)-1:
#             reptime,iseq,comm=isequ(img_ary[i],img_ary[i+1])
#             newcod=[]
#             if reptime>=2 and iseq==True:
#                 j=0
#                 while(j<np.shape(img_ary[i])[0]):
#                     if img_ary[i][j] not in comm:
#                         newcod.append(img_ary[i][j])
#                     j+=1
#             if(newcod==[]):
#                 res_lst.append(img_ary[i])
#             else:
#                 lstcod=newcod+img_ary[i+1]
#                 res_lst.append(lstcod)
#         i+=1
#     return res_lst
             
        
def isequ(img_ary_0,img_ary_1):
    rpttimes=0
    iseeq=False
    pub_elemt=[]
    for i in img_ary_0:
        if i in img_ary_1:
            pub_elemt.append(i)
            iseeq=True
            rpttimes+=1
    return rpttimes,iseeq,pub_elemt

def fun():
    imm_1='D:\\programming\\exp_folder\\brain_1\\canny\\sum_2_a.png'
    ary=findconection(imm_1)
    #newary=detmerg(ary)
    filted_1=filter4(ary,100)
    cur_1=contours(filted_1)
    
    #imgg_1='D:\\290px-MRI_Head_Brain_Normal.jpg'
    #blank=np.zeros(cv.imread(imgg_1).shape)
    #ary_1=findconection(imgg_1)
    #filted_2=filter4(ary_1,100)
    #cur_2=contours(filted_2)
    
    
    #pic_1=drawcont(blank,cur_2,'w')
    #pic_2=drawcont(pic_1,cur_1,'w')
    
    #cv.imwrite('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\sig11o\\sum_11_threall.png',pic_2)
    
def fun_1():
    imm_1='D:\\programming\\exp_folder\\brain_1\\canny\\sum_2_a.png'
    imgg_1=cv.imread('D:\\programming\\exp_folder\\brain_1\\canny\\sum_2_a.png')
    ary=findconection(imm_1)
    filted_1=filter4(ary,100)
    cur_1=contours(filted_1)
    pic_1=drawcont(imgg_1,cur_1,'g')
    cv.imwrite('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\sig11o\\sum_1111.png',pic_1)    
    
    
   #String folder path,  
def Hessian(folderpath, )   
fun()
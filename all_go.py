# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 21:32:35 2021

@author: Andy C
"""
import Heissian_Deriche_3D_modified as hd3
import dicomIO as di
import cv2 as cv
import merging as mg
import numpy as np

ratio=0.08

di.dicomIO.set_dicom_folder('D:\\programming\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\original')
str_1=di.dicomIO.get_dicom_folder()
di.dicomIO.loadDicom(str_1)
rawimage=di.dicomIO.dicom
mx=np.amax(rawimage)
mn=np.amin(rawimage)
vrang=mx-mn
noicelev=vrang*ratio
a=rawimage.shape
noise = np.random.normal(0, noicelev, a)
new_signal = rawimage + noise


# di.dicomIO.set_nifti_folder('D:\\SPIE\\la_003.nii')
# str_1=di.dicomIO.get_nifti_folder()
# di.dicomIO.loadNifti(str_1)
# rawimage=di.dicomIO.nifti
lst3d=hd3.heissian_der.Hessian_Deriche_3D(new_signal,2, 1,3,-2000)

mag=255-lst3d[0]
azi=lst3d[1]
pol=255-lst3d[2]
sum_1=lst3d[3]
pdt=255-lst3d[4]

merged=mg.merging.merg_seg(mag,azi,pol)




di.dicomIO.exportAllVolumeSlices('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\mag','mag_08',file=mag)
di.dicomIO.exportAllVolumeSlices('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\azi','azi_08',file=azi)
di.dicomIO.exportAllVolumeSlices('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\pol','pol_08',file=pol)
di.dicomIO.exportAllVolumeSlices('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\merged','merged_08',file=merged)
di.dicomIO.exportAllVolumeSlices('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\sum','sum_08',file=sum_1)
di.dicomIO.exportAllVolumeSlices('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\pdt','pdt_08',file=pdt) 
di.dicomIO.exportAllVolumeSlices('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\sig','sig_08',file=new_signal)
di.dicomIO.exportAllVolumeSlices('D:\\exp_folder\\noise\\Gaussian\\dicexp\\brain\\raw','raw_08',file=rawimage)

# for idx in range(69,70):
#     mag_img=di.dicomIO.getOneSliceFromNifti(idx,file=mag)
#     cv.imwrite('D:\\exp_folder\\heart\\mag\\mag_{}'.format(idx),mag_img)
    
#     azi_img=di.dicomIO.getOneSliceFromNifti(idx,file=azi)
#     cv.imwrite('D:\\exp_folder\\heart\\mag\\azi_{}'.format(idx),azi_img)
    
    
#     pol_img=di.dicomIO.getOneSliceFromNifti(idx,file=pol)
#     cv.imwrite('D:\\exp_folder\\heart\\mag\\pol_{}'.format(idx),pol_img)
    
    
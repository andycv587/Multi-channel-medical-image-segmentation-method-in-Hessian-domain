# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 14:18:19 2022

@author: Andy C
"""


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
newimg=cv.imread('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\water.jpg')


# di.dicomIO.set_nifti_folder('D:\\SPIE\\la_003.nii')
# str_1=di.dicomIO.get_nifti_folder()
# di.dicomIO.loadNifti(str_1)
# rawimage=di.dicomIO.nifti
lst3d=hd3.heissian_der.Hessian_Deriche_3D(newimg,2, 1,3,-2000)

mag=255-lst3d[0]
azi=lst3d[1]
pol=255-lst3d[2]
sum_1=lst3d[3]
pdt=255-lst3d[4]

merged=mg.merging.merg_seg(mag,azi,pol)




di.dicomIO.exportAllVolumeSlices('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\mag','mag_08',file=mag)
di.dicomIO.exportAllVolumeSlices('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\mag\\azi','azi_08',file=azi)
di.dicomIO.exportAllVolumeSlices('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\mag\\pol','pol_08',file=pol)
#di.dicomIO.exportAllVolumeSlices('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\mag\\merged','merged_08',file=merged)
di.dicomIO.exportAllVolumeSlices('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\mag\\sum','sum_08',file=sum_1)
di.dicomIO.exportAllVolumeSlices('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\mag\\pdt','pdt_08',file=pdt) 
#di.dicomIO.exportAllVolumeSlices('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\mag\\sig','sig_08',file=new_signal)
#di.dicomIO.exportAllVolumeSlices('C:\\Users\\Andy C\\Downloads\\pixLab\\pixLab\\images\\mag\\raw','raw_08',file=rawimage)

# for idx in range(69,70):
#     mag_img=di.dicomIO.getOneSliceFromNifti(idx,file=mag)
#     cv.imwrite('D:\\exp_folder\\heart\\mag\\mag_{}'.format(idx),mag_img)
    
#     azi_img=di.dicomIO.getOneSliceFromNifti(idx,file=azi)
#     cv.imwrite('D:\\exp_folder\\heart\\mag\\azi_{}'.format(idx),azi_img)
    
    
#     pol_img=di.dicomIO.getOneSliceFromNifti(idx,file=pol)
#     cv.imwrite('D:\\exp_folder\\heart\\mag\\pol_{}'.format(idx),pol_img)
    
    
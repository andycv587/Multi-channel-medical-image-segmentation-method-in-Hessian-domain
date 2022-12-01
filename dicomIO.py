# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 11:52:01 2021

@author: Andy C
"""
import os,sys
import numpy as np
import pydicom as dcm
import nibabel as nib
import dicom2nifti as d2n
import cv2 as cv 
from skimage import img_as_ubyte

class dicomIO:
    dicom_folder="" # record the folder of the dicom file
    nifti_file_path="" # record the folder of the nifti file
    slice_folder="" # record the folder of the slice file
    volume_folder="" # record the folder of the volume file
        
    dicom=np.array(0) # store the dicom data
    nifti=np.array(0) # store the nifti data
    volume=np.array(0) # store the volume data

    #set the dicom_folder with str
    def set_dicom_folder(str):
        dicomIO.dicom_folder=str
        
    #get the dicom_folder 
    def get_dicom_folder():
        return dicomIO.dicom_folder
    
    #set the nifti_file_path with str
    def set_nifti_folder(str):
        dicomIO.nifti_file_path=str
     
    #get the src_nifti_folder with str
    def get_nifti_folder():
        return dicomIO.nifti_file_path    
    
    #set dst_volume with data where data is a 2D or 3D array
    def setVolume(data):
        dicomIO.volume_folder=data
        img=nib.load(data)
        dicomIO.volume=np.array(img.dataobj)
    
    #get the dst_volume
    def getVolume():
        return dicomIO.volume_folder
   
    #get one slice from Dicom data where idx is the index of the slice
    def getOneSliceFromDicom(idx,file=None):
        if file is not None:
            sz=dicomIO.dicom.shape
            dcm=np.array(dicomIO.dicom)
        else:
            sz=file.shape
            dcm=np.array(file)
        slice_1=sz[2]
        #normalize dicom first
        dcm=dicomIO.convert(dcm,0,255,np.uint8)
        sz=dicomIO.dicom.shape
        if idx<0|idx>=sz[2]:
            return []
        return dicomIO.dicom[:,:,idx]

    #get one slice from nifti data where idx is the index of the slice
    def getOneSliceFromNifti(idx,file=None):
        if file is not None:
            sz=dicomIO.nifti.shape
            dcm=np.array(dicomIO.nifti)
        else:
            sz=file.shape
            dcm=np.array(file)
        slice_1=sz[2]
        #normalize dicom first
        dcm=dicomIO.convert(dcm,0,255,np.uint8)
        sz=dicomIO.nifti.shape
        if idx<0 or idx>=sz[2]:
            return []
        else:
            return dcm[:,:,idx]
    
    #get one slice from Volume data where idx is the index of the slice
    def getOneSliceFromVolume(idx,file=None):
        if file is not None:
            sz=dicomIO.volume.shape
            dcm=np.array(dicomIO.volume)
        else:
            sz=file.shape
            dcm=np.array(file)
        slice_1=sz[2]
        #normalize dicom first
        dcm=dicomIO.convert(dcm,0,255,np.uint8)
        sz=dicomIO.volume.shape
        if idx<0 or idx>=sz[2]:
            return []
        else:
            return dcm[:,:,idx]
    
    #load source dicom data from str which is the source path # code by ethan
    def loadDicom(str):
        dicomIO.set_dicom_folder(str)
        CT_images=os.listdir(str)
        
        slices=[dcm.read_file(dicomIO.dicom_folder+'/'+s,force=True)for s in CT_images] 
        
        slices=sorted(slices, key=lambda x:x.ImagePositionPatient[2])       
        
        pixel_spacing=slices[0].PixelSpacing
        
        slice_thickness=slices[0].SliceThickness 
        
        axial_aspect_ratio=pixel_spacing[1]/pixel_spacing[0]
        sagital_aspect_ratio=pixel_spacing[1]/slice_thickness
        coronal_aspect_ratio=slice_thickness/pixel_spacing[0]
        
        image_shape=list(slices[0].pixel_array.shape)
        image_shape.append(len(slices))
        volume3d=np.zeros(image_shape)
        
        for i,s in enumerate(slices):
            array2d=s.pixel_array
            volume3d[:,:,i]=array2d
        dicomIO.dicom=volume3d
    
    #load source nifiti data from str which is the nifti_folder
    def loadNifti(str):
        dicomIO.set_nifti_folder(str)
        img=nib.load(str)
        dicomIO.nifti=np.array(img.dataobj)
        
    #save the src nifti data to folder which is the nifti_folder
    def saveNifti(filepath):
        if dicomIO.nifti.shape==(0,0,0):
            return -1
        else:
            nimg=nib.Nifti1Image(dicomIO.nifti,affine=np.eye(4))
            nimg.header.get_xyzt_units()
            nib.save(nimg,filepath)
            return 0
        
    def saveVolume(filepath):
        if dicomIO.volume.shape is (0,0,0):
            return -1
        else:
            nimg=nib.Nifti1Image(dicomIO.volume,affine=np.eye(4))
            nimg.header.get_xyzt_units()
            nib.save(nimg,filepath)
            return 0
        
    #convert src_dicom to src_nifti and save nifti data into a folder 
    def dicom2nifti(filepath,targetpath):
        if dicomIO.dicom.shape is (0,0,0):
            return -1
        else:
            CT_images=os.listdir(filepath)
            
            slices=[dcm.read_file(dicomIO.dicom_folder+'/'+s,force=True)for s in CT_images] 
            
            slices=sorted(slices, key=lambda x:x.ImagePositionPatient[2])       
            
            pixel_spacing=slices[0].PixelSpacing
            
            slice_thickness=slices[0].SliceThickness 
            
            axial_aspect_ratio=pixel_spacing[1]/pixel_spacing[0]
            sagital_aspect_ratio=pixel_spacing[1]/slice_thickness
            coronal_aspect_ratio=slice_thickness/pixel_spacing[0]
            
            image_shape=list(slices[0].pixel_array.shape)
            image_shape.append(len(slices))
            volume3d=np.zeros(image_shape)
            
            for i,s in enumerate(slices):
                array2d=s.pixel_array
                volume3d[:,:,i]=array2d
            
            nimg=nib.Nifti1Image(volume3d,affine=np.eye(4))
            nimg.header.get_xyzt_units()
            nib.save(nimg,targetpath)
            return 0
        
    def exportAllDicomSlices(folder,slicename,file=None):
        if file is None:
            sz=dicomIO.dicom.shape
            dcm=dicomIO.dicom
        else:
            sz=file.shape
            dcm=file
        slice_1=sz[2]
        #normalize dicom first
        dcm=dicomIO.convert(dcm,0,255,np.uint8)
        # export the normalized dicom by every slice
        for i in range(0,slice_1):
            islicefile='{}\\{}_{}.png'.format(folder,slicename,i)
            islice=dcm[:,:,i]
            cv.imwrite(islicefile,islice)
        return 0
        
    def exportAllNiftiSlices(folder,slicename,file=None):
        if file is None:
            sz=dicomIO.nifti.shape
            dcm=np.array(dicomIO.nifti)
        else:
            sz=file.shape
            dcm=file
        slice_1=sz[2]
        #normalize dicom first
        dcm=dicomIO.convert(dcm,0,255,np.uint8)
        # export the normalized dicom by every slice
        for i in range(0,slice_1):
            islicefile='{}\\{}_{}.png'.format(folder,slicename,i)
            islice=dcm[:,:,i]
            cv.imwrite(islicefile,islice)
        return 0      

    def exportAllVolumeSlices(folder,slicename,file=None):
        if file is None:
            sz=dicomIO.volume.shape
            dcm=dicomIO.volume
        else:
            sz=file.shape
            dcm=file
        slice_1=sz[2]
        #normalize dicom first
        dcm=dicomIO.convert(dcm,0,255,np.uint8)
        # export the normalized dicom by every slice
        for i in range(0,slice_1):
            islicefile='{}\\{}_{}.png'.format(folder,slicename,i)
            islice=dcm[:,:,i]
            cv.imwrite(islicefile,islice)
        return 0
    
    def convert(img, target_type_min, target_type_max, target_type):
        imin = img.min()
        imax = img.max()
    
        a = (target_type_max - target_type_min) / (imax - imin)
        b = target_type_max - a * imax
        new_img = (a * img + b).astype(target_type)
        return new_img
            
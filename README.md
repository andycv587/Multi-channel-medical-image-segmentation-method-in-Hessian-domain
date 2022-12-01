# Multi-channel-medical-image-segmentation-method-in-Hessian-domain

**Abstract**
Medical image segmentation is an important technique in surgical navigation, tumor quantification, computer-aided diagnosis and detection, etc. To enhance the accuracy of its performance, the image contrast among different tissues in multi-modality plays an important role and is still a great challenge. In this project, we proposed an image segmentation method by merging multi-channels which are defined in Hessian domain. Every domain owns individual properties and is only sensitive to a few specific tissues, which should be an essential complement for other domains. The contrast between two neighboring tissues in their merging results provides more sensitive boundary information than the original images. Moreover, we also notice some weak boundaries are the major barrier in the processing of image segmentation. An unsupervised local segmentation scheme is proposed to combat this challenge by dividing the whole volume into small patches which are overlapped with each other. Our method is testified over five different organs with two major modalities and three noise levels, and yields very promising results. After comparing, our method exhibits its great superiority over slic and level set, two state-of-the-art methods with more accurate contours and boundaries.

**Paper Doi:** https://doi.org/10.1117/12.2612659

**Required Packages:** nibabel, opencv, dicom2nifti, skimage

The functions in dicomIO class are mainly using for extract volumes into jpg format file. There are example in all_go.py file. On the other hand, the use in segmentation could be found in file findconnection.py. The example is shown by method fun() and fun_1().






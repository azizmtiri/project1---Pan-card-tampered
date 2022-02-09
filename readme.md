# PAN CARD TAMPERED
## Introduction
The purpose of this project is to detect tampering of PAN card using computer vision. This project will help different organization in detecting whether the Id i.e. the PAN card provided to them by their employees or customers or anyone is original or not.
## Input
the original image and the user’s image
## Output
the SSIM score and we visualize the differences and similarities between the images using by displaying the images with contours, difference and threshold.  
## Workflow:
1.	Loading original and user provided images.
2.	 Converting the format of  user's image similar to original image.
3.	Converting the size of user's image and original image.
4.	Reading images using opencv.
5.	Converting images into grayscale using opencv. Because in image processing many applications doesn't help us in identifying the important, edges of the coloured images also coloured images are bit complex to understand by machine beacuse they have 3 channel while grayscale has only 1 channel.  
6.	Structural similarity index helps us to determine exactly where in terms of x,y coordinates location, the image differences are. Here, we are trying to find similarities between the original and tampered image. The lower the SSIM score lower is the similarity.
7.	the threshold function of computer vision which applies an adaptive threshold to the image which is stored in the form array. This function transforms the grayscale image into a binary image using a mathematical formula.
8.	Find contours works on binary image and retrive the contours. This contours are a useful tool for shape analysis and recoginition. Grab contours grabs the appropriate value of the contours.
9.	Bounding rectangle helps in finding the ratio of width to height of bounding rectangle of the object. We compute the bounding box of the contour and then draw the bounding box on both input images to represent where the two images are different or not.
10.	Finding out structural similarity of the images helped us in finding the difference or similarity in the shape of the images. Similarly, finding out the threshold and contours based on those threshold for the images converted into grayscale binary also helped us in shape analysis and recognition. 
11.	 Finally we visualized the differences and similarities between the images using by displaying the images with contours, difference and threshold.  




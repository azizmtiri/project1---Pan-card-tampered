import numpy as np
import pandas as pd
from PIL import Image
import cv2
from skimage.metrics import structural_similarity
import requests
import imutils
original = Image.open(requests.get('https://www.culturebanque.com/wp-content/uploads/2019/01/CB-gold-ING.jpg', stream=True).raw)
tampered = Image.open(requests.get('https://assets1.cleartax-cdn.com/s/img/20170526124335/Pan4.png', stream=True).raw) 
print("Original image format : ",original.format) 
print("Tampered image format : ",tampered.format)
print("Original image size : ",original.size) 
print("Tampered image size : ",tampered.size) 
original = original.resize((250, 160))
print(original.size)
original.save('project-1/image/original.png')
tampered = tampered.resize((250,160))
print(tampered.size)
tampered.save('project-1/image/tampered.png')
original = cv2.imread('project-1/image/original.png')
tampered = cv2.imread('project-1/image/tampered.png')
original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
tampered_gray = cv2.cvtColor(tampered, cv2.COLOR_BGR2GRAY)
(score, diff) = structural_similarity(original_gray, tampered_gray, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {} %".format(score*100))
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
for c in cnts:
    # applying contours on image
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(original, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(tampered, (x, y), (x + w, y + h), (0, 0, 255), 2)
print('Original Format Image')
Image.fromarray(original)
print('Tampered Image')
Image.fromarray(tampered)
print('Different Image')
Image.fromarray(diff)
print('Threshold Image')
Image.fromarray(thresh)

# these imports let you use opencv
import cv2 #opencv itself
import common #some useful opencv functions
import numpy as np # matrix manipulations

#the following are to do with this interactive notebook code
from matplotlib import pyplot as plt # this lets you draw inline pictures in the notebooks
import pylab # this allows you to control figure size

img = cv2.imread('face.jpg')

# Load the messi image and create a greyscale copy of it to be used in the classifiers
fig, axs = plt.subplots(1, 1, figsize=(5, 5))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
fig, axs = plt.subplots(1, 1, figsize=(5, 5))
faces = face_cascade.detectMultiScale(grey, 1.3, 5)
for (x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = eye_cascade.detectMultiScale(grey, 1.3, 1)
plt.figure(figsize=(5, 5))
for (x,y,w,h) in eyes:
     cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)

cv2.imshow('Original Image', img)
cv2.imshow('Grey Image', grey)
#cv2.imshow('Image Blur', img_blur)
#cv2.imshow('Image Mask', masked_img)
#cv2.imshow('Edge Detection', img_canny)


cv2.waitKey(0)
cv2.destroyAllWindows()

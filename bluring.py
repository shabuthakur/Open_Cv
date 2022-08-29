import cv2 as cv
img=cv.imread('download.jfif',-1)
cv.imshow('Image for testing',img)

#averaging
average=cv.blur(img,(7,7))
cv.imshow('Average  BLUR',average)

#gaussian bluring
gauss=cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur',gauss)

#Median Blur
median= cv.medianBlur(img,7)
cv.imshow('Median Blur',median)
cv.waitKey(0)


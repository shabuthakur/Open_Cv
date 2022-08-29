import cv2 as cv
import numpy as np
img=cv.imread('download.jfif',-1)
cv.imshow('Image for testing',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blank=np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)
canny=cv.Canny(img,175,125)
cv.imshow('canny',canny)

blur=cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)

#COORDINATES OF LINE
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh) #if threshold is 125 then its black otherwise its white

countours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(countours)},countours found')

#draw the contours in the blank image
cv.drawContours(blank,countours,-1,(0,0,255),1)
cv.imshow('Contours',blank)
cv.waitKey(0)
import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8') #this is blank image
cv.imshow('blank', blank)

#paint the image
blank[200:2300,300:400]=0,0,255
# cv.imshow('Green',blank)
# img=cv.imread('penguin.jpeg')

#draw a rectangle
cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)

#draw circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)

#write text
text=np.zeros((500,500,3), dtype='uint8')
cv.putText(text,'Hello my name is shabu',(0,255),cv.FONT_HERSHEY_COMPLEX,1.0,(255,0,255),2)
cv.imshow('text',text)
cv.waitKey(0)
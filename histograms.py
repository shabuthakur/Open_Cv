import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img=cv.imread('download.jfif',-1)
cv.imshow('Image for testing',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray)

circle=cv.circle(blank,(img.shape[0]//2,img.shape[0]//2),100,255,-1)
# cv.imshow('Circle image',circle)

masked_image=cv.bitwise_and(gray,gray,mask=circle)

#grayscale histogram
gray_hist=cv.calcHist([gray],[0],masked_image,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)

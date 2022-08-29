import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('download.jfif',-1)
cv.imshow('Image for testing',img)
# plt.imshow(img)
# plt.show()
#bgr to gray scale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#bgr to hsv
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#bgr to rgb
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.imshow(rgb)
plt.show()
cv.imshow('RGB',rgb)

#hsv_to_bgr
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV to BGR',hsv_bgr)

cv.waitKey(0)
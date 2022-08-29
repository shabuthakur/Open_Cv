import cv2 as cv
import numpy as np  
img=cv.imread('download.jfif',-1)
cv.imshow('Image for testing',img)

#translations

def translate(img,x,y):
  transNat=np.float32([[1,0,x],[0,1,y]])
  dimensions=(img.shape[1],img.shape[0])
  return cv.warpAffine(img,transNat,dimensions)

# -x ---->left
# -y ---->up
# x ---->right
# y ---->down

translated=translate(img,-40,10)
cv.imshow("translated",translated)
    # x=int(x)
    # y=int(y)
    # return(x,y)

# def rotate(x,y):
#     x=int


#Rotaion
def rotate(img,angle,rotPoint=None):
  (height,width)=img.shape[:2]

  if rotPoint is None:
    rotPoint=(width//2,height//2)

  rotNat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
  dimensions=(width,height)

  return cv.warpAffine(img,rotNat,dimensions)

rotated=rotate(img,-45)
rotated1=rotate(rotated,-45)

cv.imshow("rotated",rotated1)

#flip the image
flip=cv.flip(img,0) #0,1,-1 0 is used for vflip image vertically,1-horizotally
cv.imshow("flipped",flip)
cv.waitKey(0)
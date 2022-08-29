import cv2 as cv
img=cv.imread('download.jfif',-1)
cv.imshow('Image for testing',img)

#converting image to grayscale format
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


#blur image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge Cascade
cany=cv.Canny(blur,125,175)
cv.imshow('cany',cany)


#dilating image
dilated=cv.dilate(cany,(7,7),iterations=3)
cv.imshow('dilate',dilated)

#resize 
resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resize)

#cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)
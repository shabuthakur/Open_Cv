import cv2 as cv
import numpy as np 

blank= np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1) #(30,30) is starting point,(370,370) is area,255 is for color

circle=cv.circle(blank.copy(),(200,200),200, 255,-1)#(200,200) is starting point,200 is radius

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

# bitwise AND 
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise_and',bitwise_and)

# bitwise OR
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)

# bitwise NOT
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('recta_not',bitwise_not)

#bitwise Xor
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise_xor',bitwise_xor)



cv.waitKey(0)
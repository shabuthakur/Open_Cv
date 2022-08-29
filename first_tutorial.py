import cv2 as cv
# img=cv2.imread('download.jfif',-1)
# cv2.imshow('Image for testing',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##reading videos
capture=cv.VideoCapture('file.mp4')

while True:
  isTrue,frame=capture.read()
  cv.imshow('video',frame)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()
   
cv.waitKey(0)
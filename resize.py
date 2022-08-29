import cv2 as cv
# img=cv.imread('download.jfif',-1)
# cv.imshow('Image for testing',img)



def rescaleFrame(frame,scale=0.10):
  #this method is used for video and photos and all
  width=int(frame.shape[1]*scale)
  heigth=int(frame.shape[0]*scale)
  dimensions=(width,heigth)
  return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)
# cv.waitKey(0)
# cv.destroyAllWindows()

#change the resolution of the window
def changeRes(width, height):
  capture.set(3,width) #3 for width
  capture.set(4,height) #4 for height




capture=cv.VideoCapture('file.mp4')

while True:
  isTrue,frame=capture.read()

  frame_resized=rescaleFrame(frame)
  cv.imshow('video',frame)
  cv.imshow('video_resized',frame_resized)

  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()
   
cv.waitKey(0)

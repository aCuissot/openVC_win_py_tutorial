import numpy as np
import cv2 as cv

img = np.zeros((512,512,3), np.uint8)
pts = np.array([[10,5],[50,30],[70,50],[60,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
font = cv.FONT_HERSHEY_DUPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
cv.imshow('poly', img)
cv.waitKey(0)
cv.destroyAllWindows()
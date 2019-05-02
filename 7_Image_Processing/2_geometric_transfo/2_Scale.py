import numpy as np
import cv2 as cv
img = cv.imread('a.jpg')
#cv.INTER_AREA for shrinking and cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming
res = cv.resize(img,None,fx=0.2, fy=0.2, interpolation = cv.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()
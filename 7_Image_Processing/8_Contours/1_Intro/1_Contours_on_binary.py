import numpy as np
import cv2 as cv
im = cv.imread('a.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
_, thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(im, contours, -1, (0, 255, 0), 3)
"""
pour ne dessiner qu'un contour, le 3e par ex:
cv.drawContours(im, contours, 2, (0, 255, 0), 3)
ou
cnt = contours[3]
cv.drawContours(img, [cnt], 0, (0,255,0), 3)
"""

cv.imshow('', im)
cv.waitKey(0)
cv.destroyAllWindows()
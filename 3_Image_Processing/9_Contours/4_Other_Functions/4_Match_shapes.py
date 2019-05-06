import cv2 as cv
import numpy as np

img1 = cv.imread('../../../Data/in/star.jpg', 0)
img2 = cv.imread('../../../Data/in/star2.jpg', 0)
_, thresh = cv.threshold(img1, 127, 255, 0)
_, thresh2 = cv.threshold(img2, 127, 255, 0)
contours, _ = cv.findContours(thresh, 2, 1)
cnt1 = contours[0]
contours, _ = cv.findContours(thresh2, 2, 1)
cnt2 = contours[0]
ret = cv.matchShapes(cnt1, cnt2, 1, 0.0)
print(ret)
# Plus on est proche de 0, plus les formes sont semblables

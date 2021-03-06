import numpy as np
import cv2 as cv

img = cv.imread('../../Data/in/building.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)
img = cv.drawKeypoints(gray, kp, img)
cv.imwrite('../../Data/out/4.3.sift_keypoints.jpg', img)

#TODO, change version to 3.4.2.16 to make this running
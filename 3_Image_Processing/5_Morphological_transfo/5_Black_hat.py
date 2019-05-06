import cv2 as cv
import numpy as np

img = cv.imread('../../Data/in/j.png', 0)
kernel = np.ones((5, 5), np.uint8)
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
cv.imshow('blackhat', blackhat)
if cv.waitKey(0):
    cv.destroyAllWindows()

import cv2 as cv
import numpy as np

img = cv.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv.imshow('gradient', tophat)
if cv.waitKey(0):
    cv.destroyAllWindows()
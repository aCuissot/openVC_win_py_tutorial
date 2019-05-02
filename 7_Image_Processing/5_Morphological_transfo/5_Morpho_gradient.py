import cv2 as cv
import numpy as np

img = cv.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
cv.imshow('gradient', gradient)
if cv.waitKey(0):
    cv.destroyAllWindows()

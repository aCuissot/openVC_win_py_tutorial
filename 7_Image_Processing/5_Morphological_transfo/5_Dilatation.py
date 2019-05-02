import cv2 as cv
import numpy as np

img = cv.imread('j.png', 0)
kernel = np.ones((5, 5), np.uint8)
dilatation = cv.dilate(img, kernel, iterations=1)
cv.imshow('erosion', dilatation)
if cv.waitKey(0):
    cv.destroyAllWindows()
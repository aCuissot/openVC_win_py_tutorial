import cv2 as cv
import numpy as np

img = cv.imread('j_noise.png', 0)
kernel = np.ones((5, 5), np.uint8)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
cv.imshow('opening', opening)
if cv.waitKey(0):
    cv.destroyAllWindows()

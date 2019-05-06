import numpy as np
import cv2 as cv

img = cv.imread('../../Data/in/a.jpg', 0)
rows, cols = img.shape
M = cv.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow('img', dst)
cv.waitKey(0)
cv.destroyAllWindows()

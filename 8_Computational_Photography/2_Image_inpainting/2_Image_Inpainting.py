import numpy as np
import cv2 as cv

img = cv.imread('../../Data/in/old.png')
mask = cv.imread('../../Data/in/mask1.png', 0)
dst = cv.inpaint(img, mask, 3, cv.INPAINT_TELEA)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()

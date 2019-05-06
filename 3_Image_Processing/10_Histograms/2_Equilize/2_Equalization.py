import numpy as np
import cv2 as cv

img = cv.imread('../../../Data/in/vallee.jpg', 0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))  # stacking images side-by-side
cv.imwrite('../../../Data/out/3.10.2.3.12.res.png', res)

# CLAHE is an adaptative equalization

import numpy as np
import cv2 as cv

img = cv.imread('../../../Data/in/statue.png', 0)
# create a CLAHE object (Arguments are optional).
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
cv.imwrite('../../../Data/out/3.10.2.clahe_2.jpg', cl1)

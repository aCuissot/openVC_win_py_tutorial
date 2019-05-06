import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../../Data/in/gradient.png', 0)
_, thresh1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)  # first paramaeter is retVal, but not used in this case
_, thresh2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, thresh3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, thresh4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, thresh5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

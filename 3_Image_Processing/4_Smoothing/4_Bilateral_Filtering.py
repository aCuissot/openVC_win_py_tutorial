import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../../Data/in/texture.png')
blur = cv.bilateralFilter(img, 9, 75, 75)
plt.subplot(121), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()

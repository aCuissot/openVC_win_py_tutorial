import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../../../Data/in/building.jpg', 0)
hist = cv.calcHist([img], [0], None, [256], [0, 256])  # using opencv
plt.subplot(221)
plt.plot(hist)
hist, bins = np.histogram(img.ravel(), 256, [0, 256])  # using numpy
plt.subplot(222)
plt.plot(hist)
"""
color = ('b', 'g', 'r')
plt.subplot(223)
for i, col in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])
plt.show()
"""
plt.show()

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('sudoku.png')
rows, cols, ch = img.shape
pts1 = np.float32([[40, 33], [235, 38], [18, 242], [242, 242]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (300, 300))
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
plt.show()

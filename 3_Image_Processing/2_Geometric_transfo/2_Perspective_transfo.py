import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('../../Data/in/arrivederci.jpg')
rows, cols, ch = img.shape
# pts1 = np.float32([[40, 33], [235, 38], [18, 242], [242, 242]])
# pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
pts1 = np.float32([[1, 1105], [4490, 881], [1, 7289], [4433, 7498]])
pts2 = np.float32([[0, 0], [2100, 0], [0, 2970], [2100, 2970]])
M = cv.getPerspectiveTransform(pts1, pts2)
dst = cv.warpPerspective(img, M, (2100, 2970))
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(dst), plt.title('Output')
cv.imwrite('../../Data/out/3.2.arrivederci.jpg', dst)
plt.show()

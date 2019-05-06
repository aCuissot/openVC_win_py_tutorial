import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../../Data/in/a.jpg')
cv.imshow('image', img)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

k = cv.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv.destroyAllWindows()
elif k == ord('s'):  # wait for 's' key to save and exit
    cv.imwrite('../../Data/out/1.1.aa.png', img)
    cv.destroyAllWindows()

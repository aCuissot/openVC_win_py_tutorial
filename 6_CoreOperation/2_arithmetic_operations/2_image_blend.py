import cv2 as cv

img1 = cv.imread('logo.png')
img2 = cv.imread('robot.png')
print(img1.shape)
print(img2.shape)
dst = cv.addWeighted(img2, 0.7, img1, 0.3, 0)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()

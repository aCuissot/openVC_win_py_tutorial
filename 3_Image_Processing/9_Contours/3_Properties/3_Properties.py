import numpy as np
import cv2 as cv

img = cv.imread('../../../Data/in/map.png', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
x, y, w, h = cv.boundingRect(cnt)
aspect_ratio = float(w) / h
area = cv.contourArea(cnt)
x, y, w, h = cv.boundingRect(cnt)
rect_area = w * h
extent = float(area) / rect_area
area = cv.contourArea(cnt)
hull = cv.convexHull(cnt)
hull_area = cv.contourArea(hull)
solidity = float(area) / hull_area
area = cv.contourArea(cnt)
equi_diameter = np.sqrt(4 * area / np.pi)
(x, y), (MA, ma), angle = cv.fitEllipse(cnt)
imgray = img.copy()

mask = np.zeros(imgray.shape, np.uint8)
cv.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
# pixelpoints = cv.findNonZero(mask)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgray, mask=mask)
mean_val = cv.mean(img, mask=mask)
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
cv.circle(img, leftmost, 10, (0, 0, 255), -1)
cv.circle(img, rightmost, 10, (0, 0, 255), -1)
cv.circle(img, bottommost, 10, (0, 0, 255), -1)
cv.circle(img, topmost, 10, (0, 0, 255), -1)
cv.imshow('', img)
cv.waitKey(0)
cv.destroyAllWindows()

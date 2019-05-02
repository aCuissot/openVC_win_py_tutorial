import numpy as np
import cv2 as cv

img = cv.imread('hand.png', 0)
ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv.moments(cnt)
print(M)
# Centroid:
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])
# Area:
area = cv.contourArea(cnt)
img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)  # if the image is gray
print(img.shape)

# Perimeter:
perimeter = cv.arcLength(cnt, True)
# Contour Approximation:
epsilon = 0.01 * cv.arcLength(cnt, True)
approx = cv.approxPolyDP(cnt, epsilon, True)
print('centroid:' + str(cx) + ' ' + str(cy) + ' area:' + str(area) + ' perimeter:' + str(perimeter))
cv.drawContours(img, approx, -1, (0, 255, 0), 3)
hull = cv.convexHull(cnt)
print('Convex : '+str(cv.isContourConvex(cnt)))
cv.drawContours(img, hull, -1, (255, 0, 0), 3)
cv.imshow('', img)
cv.waitKey(0)
cv.destroyAllWindows()

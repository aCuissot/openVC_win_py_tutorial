import cv2 as cv
import numpy as np,sys
"""
pomme = cv.imread('pomme.png')
orange = cv.imread('orange.png')
pomX, pomY, _ = pomme.shape
demipomme = pomme[:, 0:int(pomY / 2)]
oraX, oraY, _ = orange.shape
demiorange = orange[:, int(oraY / 2):-1]
img = np.zeros((min(pomX, oraX), int(pomY / 2) + int(oraY / 2), 3), np.uint8)
x, y, _ = img.shape
img[:, 0:int(pomY / 2)] = demipomme[0:x, :]
img[:, int(pomY / 2):y] = demiorange[0:x, :]
"""
# cv.imshow('', img)

# Now official code

A = cv.imread('pomme.png')
B = cv.imread('orange.png')

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in range(5, 0, -1):  # images have to have a size in 2^n
    GE = cv.pyrUp(gpA[i])
    L = cv.subtract(gpA[i - 1], GE)
    lpA.append(L)

# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in range(5, 0, -1):
    GE = cv.pyrUp(gpB[i])
    L = cv.subtract(gpB[i - 1], GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:int(cols / 2)], lb[:, int(cols / 2):]))
    LS.append(ls)

# now reconstruct
ls_ = LS[0]
for i in range(1, 6):
    ls_ = cv.pyrUp(ls_)
    ls_ = cv.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:, :int(cols / 2)], B[:, int(cols / 2):]))
cv.imwrite('Pyramid_blending2.jpg', ls_)
cv.imwrite('Direct_blending.jpg', real)


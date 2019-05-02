# ROI = region of interest
import cv2 as cv

img = cv.imread('a.jpg')
ecrit = img[600:699, 300:400]
img[350:449, 300:400]=ecrit

b, g, r = cv.split(img)
# or b=img[:,:,0], g=img[:,:,1], ... less cost than split
img = cv.merge((b, g, r)) # on peut intervertir les r g b  :)
cv.imshow('jeej', img)

k = cv.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv.destroyAllWindows()
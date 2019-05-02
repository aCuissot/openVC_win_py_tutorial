import numpy as np
import cv2 as cv

drawing = False  # true if mouse is pressed
ix, iy = -1, -1
r, g, b = 0, 0, 0


def nothing(x):
    pass


def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, r, g, b
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(img, (x, y), 5, (b, g, r), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img, (x, y), 5, (b, g, r), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.setMouseCallback('image', draw_circle)

while (1):
    cv.imshow('image', img)
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
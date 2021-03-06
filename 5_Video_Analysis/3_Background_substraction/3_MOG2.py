import numpy as np
import cv2 as cv

cap = cv.VideoCapture('../../Data/in/vtest.avi')
fgbg = cv.createBackgroundSubtractorMOG2()
while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv.imshow('frame', fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv.destroyAllWindows()

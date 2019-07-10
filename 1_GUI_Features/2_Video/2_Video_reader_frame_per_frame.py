import numpy as np
import cv2 as cv

cap = cv.VideoCapture('../../Data/in/bowling.mp4')
print(cap.get(cv.CAP_PROP_FPS))
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # cv.imshow('frame', gray)
    cv.imshow('frame', frame)
    if cv.waitKey(0) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

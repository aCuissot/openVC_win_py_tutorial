import numpy as np
import cv2 as cv
# find more xml about face recognition at https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv.CascadeClassifier('../Data/in/haarcascade_frontalface_default.xml')
#eye_cascade = cv.CascadeClassifier('../Data/in/haarcascade_eye.xml')
cap = cv.VideoCapture(0)
while True:
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #roi_gray = gray[y:y + h, x:x + w]
        #roi_color = img[y:y + h, x:x + w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex, ey, ew, eh) in eyes:
        #    cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 255, 0), 2)
    cv.imshow('frame', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()


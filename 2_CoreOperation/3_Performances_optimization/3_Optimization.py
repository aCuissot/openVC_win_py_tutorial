import cv2 as cv

# to measure execution time:
# e1 = cv.getTickCount()
# code
# e2 = cv.getTickCount()
# time = (e2 - e1)/ cv.getTickFrequency()

img1 = cv.imread('../../Data/in/messi.jpg')


cv.setUseOptimized(False)
e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print(t)
cv.setUseOptimized(True)
# t = 0.4225138779430244
e1 = cv.getTickCount()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
e2 = cv.getTickCount()
t = (e2 - e1) / cv.getTickFrequency()
print(t)
# Result I got is t = 0.8611733902878399 seconds, .....

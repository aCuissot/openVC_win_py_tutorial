import cv2 as cv

img = cv.imread('../../Data/in/a.jpg')
px = img[100, 100]
print(px)
blue = img[100, 100, 0]
green = img[100, 100, 1]
print(blue)
print(green)

img[100, 100] = [255, 255, 255]
for i in range(20):
    img[150 + i, 150 + i] = [255, 0, 0]

# better to use (more optimized)
print(img.item(10, 10, 2))
img.itemset((10, 10, 2), 255)

print(img.shape)
print(img.size)
print(img.dtype)

cv.imshow('img', img)
k = cv.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv.destroyAllWindows()

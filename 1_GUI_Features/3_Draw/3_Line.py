import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)
# ligne de (0,0) à (511,511), bleue (car on est en BGR) de 5px d epaisseur
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
cv.imshow("line", img)
k = cv.waitKey(0)
if k == 27:  # wait for ESC key to exit
    cv.destroyAllWindows()

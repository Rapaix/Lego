import cv2 as cv
import numpy as np

img = cv.imread("images/lego.jpg")
img = cv.resize(img, (500, 500))
copy = cv.cvtColor(img.copy(), cv.COLOR_BGR2GRAY)
media = cv.blur(copy, (3, 3))
residual = img[:] - media.astype(np.int16)
sharpen = img + residual
sharpen = cv.convertScaleAbs(sharpen)

cv.imshow("original", img)
cv.imshow("sharpen ", sharpen)

cv.waitKey(0)
cv.destroyAllWindows()

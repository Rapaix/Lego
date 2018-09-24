import cv2 as cv
import numpy as np

image = cv.imread("images/lego.jpg")
image = cv.resize(image,(300, 300))
cv.imshow("original", image)

kernel = np.array([[-1,-1,-1],
                   [-1,9,-1],
                   [-1,-1,-1]])

sharpened = cv.filter2D(image, -1, kernel)
cv.imshow("sharpe", sharpened)

cv.waitKey(0)
cv.destroyAllWindows()
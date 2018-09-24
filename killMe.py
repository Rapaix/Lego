import cv2 as cv
import numpy as np


img = cv.imread('images/lego.jpg')
copy = cv.resize(img.copy(), (300, 300))
cv.imshow("img", copy)
copy = cv.cvtColor(copy, cv.COLOR_BGR2HSV)

kernel = np.zeros((copy.shape[0], copy.shape[1]), np.uint8)

red_lower = np.array([0, 87, 111], np.uint8)
red_upper = np.array([15, 255, 255], np.uint8)

yellow_lower = np.array([20, 60, 200], np.uint8)
yellow_upper = np.array([35, 255, 255], np.uint8)

green_lower = np.array([50,100,0], np.uint8)
green_upper = np.array([80,255,255], np.uint8)

cyan_lower = np.array([89,100,0], np.uint8)
cyan_upper = np.array([110,255,255], np.uint8)

blue_lower = np.array([96,100,0], np.uint8)
blue_upper = np.array([130,255,0], np.uint8)

purple_lower = np.array([118,100,0], np.uint8)
purple_upper = np.array([165,255,255], np.uint8)

magenta_lower = np.array([166,100,100], np.uint8)
magenta_upper = np.array([180,255,255], np.uint8)


mask = cv.inRange(copy, purple_lower, purple_upper)
# mask2 = cv.inRange(copy, magenta_lower, magenta_upper)
maskTotal = cv.add(mask, mask)

cv.imshow("magenta", mask)


img2 = cv.bitwise_and(copy, copy, mask= mask)


cv.imshow("teste", img2)
cv.imshow('', copy)

cv.waitKey(0)
cv.destroyAllWindows()
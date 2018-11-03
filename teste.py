import cv2 as cv
import numpy as np

redColor = (0, 0, 255)
yellowColor = (0, 255, 255)
greenColor = (0, 255, 0)
cyanColor = (255, 255, 0)
blueColor = (255, 0, 0)
purpleColor = (130, 0, 75)
magentaColor = (255, 0, 255)

def boundingColor(img2, maskColor, color):
    (_, cnts, hierarchy) = cv.findContours(maskColor, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for c in cnts:
        area = cv.contourArea(c)
        if area > 300:
            x, y, w, h = cv.boundingRect(c)
            M = cv.moments(c)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            teste = cv.rectangle(img2, (x, y), (x + w, y + h), (color), 2)
            cv.circle(img2, (cX, cY), 1, (color), -1)
            return cv.imshow("teste", teste)


img = cv.imread('images/legos.jpg')
copy = cv.resize(img.copy(), (300, 300))
hsv = cv.cvtColor(copy, cv.COLOR_BGR2HSV)

# canvas de desenho para as mascaras ser desenahadas
blank = np.zeros((hsv.shape[0], hsv.shape[1]), np.uint8)

red_lower = np.array([0, 100, 0], np.uint8)
red_upper = np.array([15, 255, 255], np.uint8)

yellow_lower = np.array([20, 60, 100], np.uint8)
yellow_upper = np.array([35, 255, 255], np.uint8)

green_lower = np.array([25, 60, 0], np.uint8)
green_upper = np.array([75, 255, 255], np.uint8)

cyan_lower = np.array([80, 100, 0], np.uint8)
cyan_upper = np.array([95, 255, 255], np.uint8)

blue_lower = np.array([84, 100, 0], np.uint8)
blue_upper = np.array([125, 255, 255], np.uint8)

purple_lower = np.array([126, 100, 0], np.uint8)
purple_upper = np.array([165, 255, 255], np.uint8)

magenta_lower = np.array([170, 100, 0], np.uint8)
magenta_upper = np.array([180, 255, 255], np.uint8)

white_lower = np.array([[0, 0, 0]])
white_upper = np.array([[10, 255, 255]])

# range of colors


red = cv.inRange(hsv, red_lower, red_upper)
yellow = cv.inRange(hsv, yellow_lower, yellow_upper)
green = cv.inRange(hsv, green_lower, green_upper)
cyan = cv.inRange(hsv, cyan_lower, cyan_upper)
blue = cv.inRange(hsv, blue_lower, blue_upper)
purple = cv.inRange(hsv, purple_lower, purple_upper)
magenta = cv.inRange(hsv, magenta_lower, magenta_upper)

sumRed = red + magenta


# soma de todas as ranges para uma imagem
maskTotal = sumRed + yellow + green + cyan + blue + purple


colors = cv.bitwise_and(copy, copy, mask=maskTotal)
cv.imshow("colors", colors)




#white = cv.inRange(maskTotal, white_lower,white_upper)
cv.imshow("mask.jpg", maskTotal)
edge = cv.Canny(maskTotal, 10 , 200)
#cv.imshow("",edge)


cv.imshow("green", green)
#cv.imshow(" Sumred", red)

# TODO  bounding box para cada cor

cv.imshow("mask", maskTotal)

boundingColor(copy, red, redColor)
boundingColor(copy, yellow, yellowColor)
boundingColor(copy, green, greenColor)
boundingColor(copy, cyan, cyanColor)
boundingColor(copy, purple, purpleColor)
boundingColor(copy, blue, blueColor)
boundingColor(copy, magenta, magentaColor)

cv.waitKey(0)
cv.destroyAllWindows()





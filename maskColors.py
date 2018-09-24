import cv2 as cv
import numpy as np


def main():
    # Aquisição da iamgem
    img = cv.imread('images/lego.jpg')
    copy = cv.resize(img.copy(), (300, 300))
    cv.imshow("img", copy)
    hsv = cv.cvtColor(copy, cv.COLOR_BGR2HSV)

    # canvas de desenho para as mascaras ser desenahadas
    blank = np.zeros((hsv.shape[0], hsv.shape[1]), np.uint8)

    red_lower = np.array([0, 87, 0], np.uint8)
    red_upper = np.array([15, 255, 255], np.uint8)

    yellow_lower = np.array([20, 60, 200], np.uint8)
    yellow_upper = np.array([35, 255, 255], np.uint8)

    green_lower = np.array([50, 100, 0], np.uint8)
    green_upper = np.array([80, 255, 255], np.uint8)

    cyan_lower = np.array([89, 100, 0], np.uint8)
    cyan_upper = np.array([110, 255, 255], np.uint8)

    blue_lower = np.array([96, 100, 0], np.uint8)
    blue_upper = np.array([130, 255, 0], np.uint8)

    purple_lower = np.array([118, 100, 0], np.uint8)
    purple_upper = np.array([165, 255, 255], np.uint8)

    magenta_lower = np.array([166, 100, 100], np.uint8)
    magenta_upper = np.array([180, 255, 255], np.uint8)


    # range of colors

    red = cv.inRange(hsv, red_lower, red_upper)
    yellow = cv.inRange(hsv, yellow_lower, yellow_upper)
    green = cv.inRange(hsv, green_lower, green_upper)
    cyan = cv.inRange(hsv, cyan_lower, cyan_upper)
    blue = cv.inRange(hsv, blue_lower, blue_upper)
    purple = cv.inRange(hsv, purple_lower, purple_upper)
    magenta = cv.inRange(hsv, magenta_lower, magenta_upper)

    # soma de todas as ranges para uma imagem
    maskTotal = red + yellow + green + cyan + blue + purple + magenta
    colors = cv.bitwise_and(copy, copy, mask=maskTotal)

    cv.imshow(" maskara", colors)

#TO DO fazer bounding box para cada cor
    #alterar os parametros para a  deteccao de retangulos
    thresh = cv.adaptiveThreshold(maskTotal, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 3)
    cv.imshow("Gaussian Thresh", thresh)

    (im2,cnts, hier) = cv.findContours(maskTotal, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    #cnts = sorted(cnts, key = cv.contourArea, reverse= True)[:10]

    retas =[]

    for c in cnts:
        peri = cv.arcLength(c, True)
        approx = cv.approxPolyDP(c, 0.1 * peri, True)

        if len(approx) >= 4:
            retas.append(approx)

    cv.drawContours(copy, retas, -1, (0, 0, 255), 3)

    cv.imshow("", copy)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()

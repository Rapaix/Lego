import numpy as np
import cv2 as cv


def sort_contours(cnts, method="left-to-right"):

    reverse = False
    i = 0

    if method == "right-to-left" or method =="botto-to-top":
        reverse = True

    if method == "top-to-bottom" or method =="bottom-to-top":
        i =1
#pesquisar boundingRect()
    boundingBoxes = [cv.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
        key=lambda b:b[1][i], reverse= True))

    return (cnts, boundingBoxes)

def draw_contour(copy, c, i):

    M = cv.moments(c)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])

    cv.putText(copy,"#{}".format(i+1) , (cX - 20, cY), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255,255,255),2)

    return copy

img = cv.imread("images/lego.jpg")
copy = cv.resize(img, (300, 300))
cv.imshow("teste de copia", copy)


copy = cv.medianBlur(copy, 5)
edge = cv.Canny(copy, 50, 200)

cv.imshow("edge", edge)

(_, cnts, _ ) = cv.findContours(edge.copy(), cv.RETR_EXTERNAL,
                             cv.CHAIN_APPROX_SIMPLE)
cnts = sorted(cnts, key=cv.contourArea, reverse=True)[:5]
orig = copy.copy()

# loop over the (unsorted) contours and draw them
for (i, c) in enumerate(cnts):
    orig = draw_contour(orig, c, i)

# show the original, unsorted contour image
orig = cv.resize(orig,(300, 300))
cv.imshow("Unsorted", orig)

# sort the contours according to the provided method
(cnts, boundingBoxes) = sort_contours(cnts, method="bottom-to-top")

# loop over the (now sorted) contours and draw them
for (i, c) in enumerate(cnts):
    draw_contour(copy, c, i)

# show the output image
cv.imshow("Sorted", copy)
cv.waitKey(0)

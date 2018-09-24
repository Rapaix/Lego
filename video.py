import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while True:

    ret, frame = cap.read()
    print(cap.isOpened())

    gray = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    cv.imshow("frame", gray)

    if cv.waitKey(1):
        cv.destroyAllWindows()

cap.release()
cv.destroyAllWindows()
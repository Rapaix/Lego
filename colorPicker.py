import cv2
import numpy as np
import sys
import tkinter as tk
from tkinter import filedialog

image_hsv = None
pixel = (0,0,0) #RANDOM DEFAULT VALUE

ftypes = [
    ('JPG', '*.jpg;*.JPG;*.JPEG'),
    ('PNG', '*.png;*.PNG'),
    ('GIF', '*.gif;*.GIF'),
]

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = image_hsv[y,x]

        #HUE, SATURATION, AND VALUE (BRIGHTNESS) RANGES. TOLERANCE COULD BE ADJUSTED.
        print("upper:" ,pixel)
        upper =  np.array([pixel[0] + 10, pixel[1] + 10, pixel[2] + 40])
        lower =  np.array([pixel[0] - 10, pixel[1] - 10, pixel[2] - 40])
        print(lower, upper)

        #A MONOCHROME MASK FOR GETTING A BETTER VISION OVER THE COLORS
        image_mask = cv2.inRange(image_hsv,lower,upper)
        cv2.imshow("Mask",image_mask)

def main():

    global image_hsv, pixel

    #OPEN DIALOG FOR READING THE IMAGE FILE
    root = tk.Tk()
    root.withdraw() #HIDE THE TKINTER GUI
    file_path = filedialog.askopenfilename(filetypes = ftypes)
    image_src = cv2.imread(file_path)
    image_src = cv2.resize(image_src, (300,300))
    print(image_src.shape)
    cv2.imshow("BGR",image_src)

    #CREATE THE HSV FROM THE BGR IMAGE
    image_hsv = cv2.cvtColor(image_src,cv2.COLOR_BGR2HSV)
    image_hsv = cv2.resize(image_hsv, (300, 300))
    print(image_hsv.shape)
    cv2.imshow("HSV",image_hsv)

    #CALLBACK FUNCTION
    cv2.setMouseCallback("HSV", pick_color)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
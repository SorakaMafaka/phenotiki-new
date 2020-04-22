# import the necessary packages
import imutils
from skimage import exposure
import numpy as np
import argparse
import imutils
import cv2


def contour(image_file, contour_list):

    img = cv2.imread(image_file)
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([30, 100, 30])
    upper_green = np.array([158, 200, 158])
    mask_green = cv2.inRange(imghsv, lower_green, upper_green)
    contours, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    im = np.copy(img)
    cv2.drawContours(im, contours, -1, (128, 0, 128), 3)
    contour_list.append(im)
    return im

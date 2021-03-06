#Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020

import imutils
from skimage import exposure
import numpy as np
import argparse
import imutils
import cv2


# return the image with contour added
def contour(image_file, contour_list):
    img = cv2.imread(image_file)
    imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_green = np.array([30, 100, 30])
    upper_green = np.array([158, 200, 158])
    mask_green = cv2.inRange(imghsv, lower_green, upper_green)
    contours, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    im = np.copy(img)
    cv2.drawContours(im, contours, -1, (138, 43, 226), 3)
    contour_list.append(im)
    return im

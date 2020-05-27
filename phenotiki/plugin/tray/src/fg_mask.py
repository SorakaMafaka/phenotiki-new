#Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020

import numpy as np
import skimage as sk
from cv2 import cv2
from skimage.color import rgb2gray


# FG_Mask segmentation
def fg_mask(image):
    original = cv2.imread(image)

    l_min = 111
    a_min = 49
    b_min = 137
    l_max = 240
    a_max = 114
    b_max = 240

    min_lab = np.array([l_min, a_min, b_min])
    max_lab = np.array([l_max, a_max, b_max])

    # Convert the BGR image to other color spaces
    image_lab = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)

    # Create the mask using the min and max values obtained from trackbar and apply bitwise and operation to get the
    # results
    mask_lab = cv2.inRange(image_lab, min_lab, max_lab)
    result_lab = cv2.bitwise_and(original, original, mask=mask_lab)

    # Apply Masks
    image = rgb2gray(result_lab)

    mask = sk.img_as_float64(image)
    return mask

import cv2, time, argparse, glob
import numpy as np


def do_things(image):
    # load image
    original = cv2.imread(image)
    # Resize the image
    rsize = 600
    original = cv2.resize(original, (rsize, rsize))

    # position on the screen where the windows start
    initial_x = 50
    initial_y = 50

    # creating windows to display images
    cv2.namedWindow('Original', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Segmentation', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Outline', cv2.WINDOW_AUTOSIZE)
    cv2.moveWindow('Original', initial_x, initial_y)
    cv2.moveWindow('Segmentation', initial_x + 1 * (rsize + 5), initial_y)
    cv2.moveWindow('Outline', initial_x + 2 * (rsize + 5), initial_y)

    cv2.imshow('Original', original)
    cv2.imshow('Segmentation', original)
    cv2.imshow('Outline', original)

    i = 0
    while (1):
        k = cv2.waitKey(1) & 0xFF

        # outline plant image
        l_min_out = 111
        a_min_out = 49
        b_min_out = 137
        l_max_out = 174
        a_max_out = 114
        b_max_out = 207

        l_min = 111
        a_min = 49
        b_min = 137
        l_max = 240
        a_max = 114
        b_max = 240

        min_lab = np.array([l_min, a_min, b_min])
        max_lab = np.array([l_max, a_max, b_max])
        min_la_bout = np.array([l_min_out, a_min_out, b_min_out])
        max_la_bout = np.array([l_max_out, a_max_out, b_max_out])

        # Convert the BGR image to other color spaces
        image_lab = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)

        # Create the mask using the min and max values obtained from trackbar and apply bitwise and operation to get the results
        mask_lab = cv2.inRange(image_lab, min_lab, max_lab)
        result_lab = cv2.bitwise_and(original, original, mask=mask_lab)
        mask_la_bout = cv2.inRange(image_lab, min_la_bout, max_la_bout)
        result_la_bout = cv2.bitwise_and(original, original, mask=mask_la_bout)

        # Show the results
        cv2.imshow('Segmentation', result_lab)
        cv2.imshow('Outline', result_la_bout)


do_things("./crop_test.png")

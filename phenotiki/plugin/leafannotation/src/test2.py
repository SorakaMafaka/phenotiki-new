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

        LMin = 111
        AMin = 49
        BMin = 137
        LMax = 240
        AMax = 114
        BMax = 240

        minLAB = np.array([LMin, AMin, BMin])
        maxLAB = np.array([LMax, AMax, BMax])
        minLABout = np.array([l_min_out, a_min_out, b_min_out])
        maxLABout = np.array([l_max_out, a_max_out, b_max_out])

        # Convert the BGR image to other color spaces
        imageLAB = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)

        # Create the mask using the min and max values obtained from trackbar and apply bitwise and operation to get the results
        maskLAB = cv2.inRange(imageLAB, minLAB, maxLAB)
        resultLAB = cv2.bitwise_and(original, original, mask=maskLAB)
        maskLABout = cv2.inRange(imageLAB, minLABout, maxLABout)
        resultLABout = cv2.bitwise_and(original, original, mask=maskLABout)

        # Show the results
        cv2.imshow('Segmentation', resultLAB)
        cv2.imshow('Outline', resultLABout)


do_things('./crop_test.png')

import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb, rgb2gray
import numpy as np


def log(widget, image):
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

    # Create the mask using the min and max values obtained from trackbar and apply bitwise and operation to get the results
    mask_lab = cv2.inRange(image_lab, min_lab, max_lab)
    result_lab = cv2.bitwise_and(original, original, mask=mask_lab)

    # Apply Masks
    image = rgb2gray(result_lab)

    # apply threshold
    thresh = threshold_otsu(image)
    bw = closing(image > thresh, square(3))

    # remove artifacts connected to image border
    cleared = clear_border(bw)

    # label image regions
    label_image = label(cleared)
    image_label_overlay = label2rgb(label_image, image=image, bg_label=0)

    widget.pt_MplWidget.canvas.axes.clear()
   # widget.pt_MplWidget.figure.subplots(figsize=(10, 6))
    widget.pt_MplWidget.canvas.axes.imshow(image_label_overlay)
    #fig, ax = plt.subplots(figsize=(10, 6))
    #ax.imshow(image_label_overlay)
    subjects = []
    area = []
    center = []
    for region in regionprops(label_image):
        # take regions with large enough areas
        if region.area >= 1000:
            # draw rectangle around segmented plants
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=1)

            subjects.append(region.centroid)
            area.append(region.area)
            center.append(region.centroid)
            print("---------UPDATE PROGRESS BAR---------")
            print("region: " + str(len(subjects)) + "\nminr: " + str(minr) + "\nminc: " +
                  str(minc) +"\nmaxr: " + str(maxr) + "\nmaxc: " + str(maxc) + "\ncentroid: " + str(region.centroid)
                  + "\narea: " + str(region.area))
            widget.pt_MplWidget.canvas.axes.add_patch(rect)


    print("number of subjects: " + str(len(subjects)))
    widget.pt_MplWidget.canvas.axes.set_axis_off()
    widget.pt_MplWidget.canvas.figure.tight_layout()
    widget.pt_MplWidget.canvas.draw()

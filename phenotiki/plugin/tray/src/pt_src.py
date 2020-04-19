import re
from datetime import datetime

import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb, rgb2gray
import numpy as np


def log(widget, image, img, plant_dict):
    original = cv2.imread(image)
    # widget.pt_progressBar.progressInit("Mask Extraction")
    widget.pt_progressBar.setEnabled(True)
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
    # fig, ax = plt.subplots(figsize=(10, 6))
    # ax.imshow(image_label_overlay)
    subjects = []
    progUpdate = 100 % len(regionprops(label_image))
    image_list = []
    image_dict = {}
    dataset = {}
    id = 0

    for region in regionprops(label_image):
        # take regions with large enough areas

        if region.area >= 100:
            id += 1
            # draw rectangle around segmented plants
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=1)
            newVal = widget.pt_progressBar.value() + progUpdate
            widget.pt_progressBar.setValue(newVal)
            convex_area = region.convex_area
            filled_area = region.filled_area
            perimeter = (2 * ((maxr - minr) + (maxc - minc)))
            length = maxr - minr
            width = maxc - minc

            if length >= width:
                diameter = length
            else:
                diameter = width

            stockiness = (4 * np.math.pi * filled_area / (perimeter ^ 2))
            compactness = filled_area / convex_area
            hue = None  # needs to be added
            count = None  # needs to be added
            relative_rate_change = None
            absolute_growth_rate = None
            relative_growth_rate = None

            date_match = re.search(r'\d{4}-\d{2}-\d{2}_\d{2}-\d{2}', img)
            date = datetime.strptime(date_match.group(), '%Y-%m-%d_%H-%M').date()
            time = datetime.strptime(date_match.group(), '%Y-%m-%d_%H-%M').time()
            date_time = str(date) + " " + str(time)

            subject_dict = {'Date': date_time, 'ID': str(id), 'ProjectedLeafArea': str(filled_area),
                            'Perimeter': str(perimeter), 'Diameter': str(diameter), 'Stockiness': str(stockiness),
                            'Compactness': str(compactness), 'Hue': str(hue), 'Count': str(count),
                            'RelativeRateChange': str(relative_rate_change), 'AbsoluteGrowthRate': str(absolute_growth_rate),
                            'RelativeGrowthRate': str(relative_growth_rate)}

            image_dict.update({date_time + " " + str(id): subject_dict})
            widget.pt_MplWidget.canvas.axes.add_patch(rect)

    plant_dict.update({img: image_dict})
    widget.pt_MplWidget.canvas.axes.set_axis_off()
    widget.pt_MplWidget.canvas.figure.tight_layout()
    widget.pt_MplWidget.canvas.draw()
    widget.pt_progressBar.setValue(100)


def updateImage(widget, i):
    img = plt.imread(widget.img_file_list_array[i])
    widget.pt_MplWidget.canvas.axes.clear()
    widget.pt_MplWidget.canvas.axes.imshow(img)
    widget.pt_MplWidget.canvas.axes.set_axis_off()
    widget.pt_MplWidget.canvas.figure.tight_layout()
    widget.pt_MplWidget.canvas.draw()

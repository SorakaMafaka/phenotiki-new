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
import skimage as sk
import numpy as np

from phenotiki.plugin.tray.src.fg_mask import fg_mask


def log(widget, image, img, plant_dict, total_subjects, sequences, fg_mask_list, detected_plants_list):
    # original = cv2.imread(image)
    # # widget.pt_progressBar.progressInit("Mask Extraction")
    # widget.pt_progressBar.setEnabled(True)
    # l_min = 111
    # a_min = 49
    # b_min = 137
    # l_max = 240
    # a_max = 114
    # b_max = 240
    #
    # min_lab = np.array([l_min, a_min, b_min])
    # max_lab = np.array([l_max, a_max, b_max])
    #
    # # Convert the BGR image to other color spaces
    # image_lab = cv2.cvtColor(original, cv2.COLOR_BGR2LAB)
    #
    # # Create the mask using the min and max values obtained from trackbar and apply bitwise and operation to get the results
    # mask_lab = cv2.inRange(image_lab, min_lab, max_lab)
    # result_lab = cv2.bitwise_and(original, original, mask=mask_lab)
    #
    # # Apply Masks
    # image = rgb2gray(result_lab)

    image = fg_mask(image)

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
    progUpdate = 100 % len(regionprops(label_image))
    image_dict = {}
    id = 0
    date_match = re.search(r'\d{4}-\d{2}-\d{2}_\d{2}-\d{2}', img)
    date = datetime.strptime(date_match.group(), '%Y-%m-%d_%H-%M').date()
    time = datetime.strptime(date_match.group(), '%Y-%m-%d_%H-%M').time()
    date_time = str(date) + " " + str(time)
    subjects = []
    subject_ids = []
    subject_group = []
    subject_project_leaf_areas = []
    subject_perimeters = []
    subject_diameters = []
    subject_stockiness = []
    subject_compactness = []
    subject_hue = []
    subject_count = []
    subject_relative_rate_change = []
    subject_absolute_growth_rate = []
    subject_relative_growth_rate = []

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

            # extract traits
            convex_area = region.convex_area
            filled_area = region.filled_area
            perimeter = (2 * ((maxr - minr) + (maxc - minc)))
            height = rect.get_height()
            width = rect.get_width()

            if height >= width:
                diameter = height
            else:
                diameter = width

            stockiness = (4 * np.math.pi * filled_area / (perimeter ^ 2))
            compactness = filled_area / convex_area
            group = None
            hue = None  # needs to be added
            count = None  # needs to be added
            relative_rate_change = None
            absolute_growth_rate = None
            relative_growth_rate = None

            # add traits to lists
            subject_ids.append(int(id))
            subject_project_leaf_areas.append(int(filled_area))
            subject_perimeters.append(int(perimeter))
            subject_diameters.append(int(diameter))
            subject_stockiness.append(float(stockiness))
            subject_compactness.append(float(compactness))
            subject_hue.append(hue)
            # subject_group.append(group)
            subject_count.append(count)
            subject_relative_rate_change.append(relative_rate_change)
            subject_absolute_growth_rate.append(absolute_growth_rate)
            subject_relative_growth_rate.append(relative_growth_rate)

            # get total number of subjects
            total_subjects.append(id)

            widget.pt_MplWidget.canvas.axes.add_patch(rect)


    subject_dict = {'ID': subject_ids,
                    'Group': subject_group,
                    'ProjectedLeafArea': subject_project_leaf_areas,
                    'Perimeter': subject_perimeters,
                    'Diameter': subject_diameters,
                    'Stockiness': subject_stockiness,
                    'Compactness': subject_compactness,
                    'Hue': subject_hue,
                    'Count': subject_count,
                    'RelativeRateChange': subject_relative_rate_change,
                    'AbsoluteGrowthRate': subject_absolute_growth_rate,
                    'RelativeGrowthRate': subject_relative_growth_rate}

    subjects.append(subject_dict)
    fg_mask_list.append(image)
    image_dict.update({'Filename': img, 'TimeStamp': date_time, 'Subjects': subjects, 'FGMask': str(fg_mask_list)})
    sequences.append(image_dict)
    plant_dict.update({'Sequences': sequences, 'NumberOfSubjects': len(total_subjects), 'MaxImageSize': None,
                       'BasePath': None, 'ml': None})
    widget.pt_MplWidget.canvas.axes.set_axis_off()
    widget.pt_MplWidget.canvas.figure.tight_layout()
    widget.pt_MplWidget.canvas.draw()
    detected_plants_list.append(image_label_overlay)
    widget.pt_progressBar.setValue(50)


def updateImage(widget, i, active_list):
    img = active_list[i]
    widget.pt_MplWidget.canvas.axes.clear()
    widget.pt_MplWidget.canvas.axes.imshow(img)
    widget.pt_MplWidget.canvas.axes.set_axis_off()
    widget.pt_MplWidget.canvas.figure.tight_layout()
    widget.pt_MplWidget.canvas.draw()

import re
from datetime import datetime

import cv2
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from PySide2.QtCore import QCoreApplication

from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb, rgb2gray
from skimage import io
import skimage as sk
import numpy as np

from phenotiki.plugin.tray.src.fg_mask import fg_mask


def traits_log(widget, image, img, plant_dict, total_subjects, sequences, fg_mask_list, detected_plants_list,
               path_list):
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
    widget.pt_MplWidget.canvas.axes.imshow(image_label_overlay)

    # Update progress
    progUpdate = 100 % len(regionprops(label_image))

    # Declare Variables and List for Extraction
    image_dict = {}
    id = 0
    date_match = re.search(r'\d{4}-\d{2}-\d{2}_\d{2}-\d{2}', img)
    date = datetime.strptime(date_match.group(), '%Y-%m-%d_%H-%M').date()
    time = datetime.strptime(date_match.group(), '%Y-%m-%d_%H-%M').time()
    date_time = str(date) + " " + str(time)
    subjects = []
    subject_ids = []
    subject_center = []
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

    # Find regions and add rectangles
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

            # add rectangle patches to image
            widget.pt_MplWidget.canvas.axes.add_patch(rect)

    # Build Subject Dictionary
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

    # Build sequence dictionary
    image_dict.update({'Filename': img, 'TimeStamp': date_time, 'Subjects': subjects, 'FGMask': str(fg_mask_list)})
    sequences.append(image_dict)

    # build top level dataset
    plant_dict.update({'Sequences': sequences, 'NumberOfSubjects': len(total_subjects), 'MaxImageSize': None,
                       'BasePath': path_list[0], 'ml': None})

    # Display to Canvas UI
    widget.pt_MplWidget.canvas.axes.set_axis_off()
    widget.pt_MplWidget.canvas.figure.tight_layout()
    widget.pt_MplWidget.canvas.draw()
    detected_plants_list.append(image_label_overlay)

    # Update Progress Bar
    widget.pt_progressBar.setValue(50)
    widget.pt_lblProgress.setText(
        QCoreApplication.translate("MainWindow", u"Progress: Extracting Traits", None))


#
def log(widget, image, detected_plants_list, subject_center_list):
    image = fg_mask(image)

    # apply threshold
    thresh = threshold_otsu(image)
    bw = closing(image > thresh, square(3))

    # remove artifacts connected to image border
    cleared = clear_border(bw)

    # label image regions
    label_image = label(cleared)
    image_label_overlay = label2rgb(label_image, image=image, bg_label=0)

    # Setup and Display on Canvas Widget
    widget.pt_MplWidget.canvas.axes.clear()
    widget.pt_MplWidget.canvas.axes.imshow(image_label_overlay)

    # Update Progress
    progUpdate = 100 % len(regionprops(label_image))

    # Declare Variables and Lists
    subject_center = []

    # Find regions and centre spots
    for region in regionprops(label_image):
        # take regions with large enough areas

        if region.area >= 100:
            minr, minc, maxr, maxc = region.bbox
            rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                                      fill=False, edgecolor='red', linewidth=1)
            newVal = widget.pt_progressBar.value() + progUpdate
            widget.pt_progressBar.setValue(newVal)
            center = region.centroid
            subject_center.append(center)

            widget.pt_MplWidget.canvas.axes.add_patch(rect)

    # Add center spots to list
    subject_center_list.append(subject_center)

    # Display image on widget
    widget.pt_MplWidget.canvas.axes.set_axis_off()
    widget.pt_MplWidget.canvas.figure.tight_layout()
    widget.pt_MplWidget.canvas.draw()

    # Cannot find way to display image with borders without saving the image first.
    # This can be improved.
    det_img = "./det_img.png"
    widget.pt_MplWidget.canvas.figure.savefig(det_img, bbox_inches='tight',
                                              pad_inches=0)
    det_img = sk.io.imread("./det_img.png")

    # Add detected plants to list
    detected_plants_list.append(det_img)

    # Update Progress Bar and Text
    widget.pt_progressBar.setValue(50)
    widget.pt_lblProgress.setText(
        QCoreApplication.translate("MainWindow", u"Progress: Extracting Masks", None))


# Update the image when UI interaction
def updateImage(widget, i, active_list):
    img = active_list[i]
    widget.pt_MplWidget.canvas.axes.clear()
    widget.pt_MplWidget.canvas.axes.imshow(img)
    widget.pt_MplWidget.canvas.axes.set_axis_off()
    widget.pt_MplWidget.canvas.figure.tight_layout()
    widget.pt_MplWidget.canvas.draw()

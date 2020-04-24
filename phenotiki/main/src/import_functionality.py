import os
import glob

from PySide2.QtWidgets import QWidget, QFileDialog

#Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020

def openFileDialog(self):
    w = QWidget()
    path = str(QFileDialog.getExistingDirectory(w,  "Select Directory"))
    return path


def print_image_files(self):
    path = openFileDialog(self)
    try:
        os.chdir(path)
    except OSError:
        print("Load Image Cancelled")
    filenames = []
    paths = []
    names = {}
    for file in glob.glob('IMG?*png'):


        filenames.append(file)
        full_path = path + "/" + file
        name = "/" + file
        names[file] = full_path
        #paths.append(names[file])
    #print(paths)
    #print(names.items())
    return names





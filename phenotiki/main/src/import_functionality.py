import os
import glob

from PySide2.QtWidgets import QWidget, QFileDialog


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
    print(names.items())
    return names





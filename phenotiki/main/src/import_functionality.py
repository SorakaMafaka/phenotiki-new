import json
import os
import glob

from PySide2.QtWidgets import QWidget, QFileDialog, QMessageBox


def openFileDialog(self):
    w = QWidget()
    path = str(QFileDialog.getExistingDirectory(w, "Select Directory"))
    return path


def save_data(self, file):
    w = QWidget()
    path = (QFileDialog.getSaveFileName(w, 'Save as', "", '*.json'))
    if path[0] != "":
        with open(path[0], 'w') as outfile:
            json.dump(self.plant_dict, outfile, indent=4)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("New document saved at " + path[0])
        msgBox.setWindowTitle("Document saved")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
    else:
        self.show_errormsg("Save Cancelled")


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
        # paths.append(names[file])
    # print(paths)
    # print(names.items())
    return names

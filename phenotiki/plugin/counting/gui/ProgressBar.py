
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QLabel
from PyQt5.QtCore import Qt

#Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020

class ProgressBar(QMainWindow):
#work in progress, made for leave counting
    def __init__(self):
        super().__init__()

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.pbar.setValue(0)
        self.label = QLabel("")

    def progressInit(self, title):
        self.setWindowTitle(title)
        self.setGeometry(32, 32, 320, 200)
        self.show()
        self.pbar.setEnabled(True)
        self.pbar.show()


    def progressUpdate(self, progressValue, info):
        self.pbar.setValue(progressValue)
        self.label.setText(str(progressValue))


    def progressEnd(self):
        self.hide()
        self.pbar.setValue(0)
        self.label.setText("")
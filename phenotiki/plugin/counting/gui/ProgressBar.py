
from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar, QLabel
from PyQt5.QtCore import Qt


class ProgressBar(QMainWindow):

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
       # self.pbar.show()
        self.label.setText(str(progressValue))


    def progressEnd(self):
        self.hide()
        self.pbar.setValue(0)
        self.label.setText("")
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

from phenotiki.main.gui.ui_mainwindow import Ui_MainWindow

#Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
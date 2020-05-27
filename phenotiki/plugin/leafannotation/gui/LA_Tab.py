from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

#Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020

class LA_Tab():
    def __init__(self, tab):

        ## Tab setup
        self.tabsystem = tab
        self.tabsystem.setFont(QFont("Helvetica", 12))
        self.tabLeafLabelling = QWidget()
        self.tabLeafLabelling.setObjectName(u"tabLeafLabelling")
        self.tabLeafLabelling.setFont(QFont("Helvetica", 8))

        ## File List Group Box set up
        self.ll_gbxFileList_2 = QGroupBox(self.tabLeafLabelling)
        self.ll_gbxFileList_2.setObjectName(u"ll_gbxFileList_2")
        self.ll_gbxFileList_2.setGeometry(QRect(10, 20, 251, 671))

        # Combobox Subject setup
        self.ll_cbxSubject = QComboBox(self.ll_gbxFileList_2)
        self.ll_cbxSubject.setObjectName(u"ll_cbxSubject")
        self.ll_cbxSubject.setGeometry(QRect(10, 570, 221, 31))

        #Subject's Label Setup
        self.ll_lblSubject = QLabel(self.ll_gbxFileList_2)
        self.ll_lblSubject.setObjectName(u"ll_lblSubject")
        self.ll_lblSubject.setGeometry(QRect(10, 550, 55, 16))

        #File List setup
        self.ll_lstFileListLL = QListView(self.ll_gbxFileList_2)
        self.ll_lstFileListLL.setObjectName(u"ll_lstFileListLL")
        self.ll_lstFileListLL.setGeometry(QRect(10, 20, 231, 521))

        #Button Load setup
        self.ll_btnLoad = QPushButton(self.ll_gbxFileList_2)
        self.ll_btnLoad.setObjectName(u"ll_btnLoad")
        self.ll_btnLoad.setGeometry(QRect(10, 610, 221, 41))

        ##self.ll_btnHelp = QPushButton(self.ll_gbxFileList_2)
        ##self.ll_btnHelp.setObjectName(u"ll_btnHelp")
        ##self.ll_btnHelp.setGeometry(QRect(10, 500, 50,50))


        ## Image group box setup
        self.ll_gbxImage = QGroupBox(self.tabLeafLabelling)
        self.ll_gbxImage.setObjectName(u"ll_gbxImage")
        self.ll_gbxImage.setGeometry(QRect(270, 20, 741, 521))


        ## Horizontal slider in Image group box setup
        self.ll_horizontalSlider = QSlider(self.ll_gbxImage)
        self.ll_horizontalSlider.setObjectName(u"ll_horizontalSlider")
        self.ll_horizontalSlider.setGeometry(QRect(120, 470, 251, 21))
        self.ll_horizontalSlider.setOrientation(Qt.Horizontal)


        ## Annotations checkbox setup
        self.ll_cbxAnnotations = QCheckBox(self.ll_gbxImage)
        self.ll_cbxAnnotations.setObjectName(u"ll_cbxAnnotations")
        self.ll_cbxAnnotations.setGeometry(QRect(560, 470, 161, 20))

        ## Current label in Image group box setup
        self.ll_lblCurrent = QLabel(self.ll_gbxImage)
        self.ll_lblCurrent.setObjectName(u"lblCurrent")
        self.ll_lblCurrent.setGeometry(QRect(580, 440, 121, 16))

        ## File list in Image groupbox setup
        self.ll_lstFileView = QListWidget(self.ll_gbxImage)
        self.ll_lstFileView.setObjectName(u"ll_lstFileView")
        self.ll_lstFileView.setGeometry(QRect(550, 190, 171, 241))

        ##Toolbox groupbox setup
        self.ll_gbxToolbox = QGroupBox(self.tabLeafLabelling)
        self.ll_gbxToolbox.setObjectName(u"ll_gbxToolbox")
        self.ll_gbxToolbox.setGeometry(QRect(270, 550, 741, 141))

        tab.addTab(self.tabLeafLabelling, "")
        self.retranslate_UI()

    ## Puts in proper text names on variour retranslated elements
    def retranslate_UI(self):
        self.ll_gbxFileList_2.setTitle(QCoreApplication.translate("MainWindow", u"File List", None))
        self.ll_lblSubject.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
        self.ll_btnLoad.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.ll_gbxImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.ll_cbxAnnotations.setText(QCoreApplication.translate("MainWindow", u"Show/Hide Annotations", None))
        self.ll_lblCurrent.setText(QCoreApplication.translate("MainWindow", u"Current Label: new", None))
        self.ll_gbxToolbox.setTitle(QCoreApplication.translate("MainWindow", u"Toolbox", None))
        self.tabsystem.setTabText(self.tabsystem.indexOf(self.tabLeafLabelling),
                                  QCoreApplication.translate("MainWindow", u"Leaf Labelling", None))
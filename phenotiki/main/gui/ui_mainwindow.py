from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide2.QtGui import (QCursor, QFont,
                           QIcon, QPixmap)
from PySide2.QtWidgets import *

from phenotiki.plugin.counting.gui.LC_Tab import LC_Tab
from phenotiki.plugin.dataextraction.gui.DE_Tab import DE_Tab
from phenotiki.main.src.import_functionality import *
from phenotiki.plugin.leafannotation.gui.LA_Tab import LA_Tab
from phenotiki.plugin.tray.gui.PT_Tab import PT_Tab


# Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # set main window
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 740)  # change this line to make resizable
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1024, 740))
        MainWindow.setMaximumSize(QSize(1024, 740))
        icon = QIcon()
        icon.addFile(u"../gui/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1031, 771))

        # set up main tab
        self.tabMain = QWidget()
        self.tabMain.setObjectName(u"tabMain")
        sizePolicy.setHeightForWidth(self.tabMain.sizePolicy().hasHeightForWidth())
        self.tabMain.setSizePolicy(sizePolicy)

        # About Button
        self.main_btnAbout = QPushButton(self.tabMain)
        self.main_btnAbout.setObjectName(u"main_btnAbout")
        self.main_btnAbout.setGeometry(QRect(900, 350, 111, 51))

        # Header Label
        self.main_lblHeader = QLabel(self.tabMain)
        self.main_lblHeader.setObjectName(u"main_lblHeader")
        self.main_lblHeader.setGeometry(QRect(10, 280, 301, 81))
        font = QFont()
        font.setPointSize(40)
        self.main_lblHeader.setFont(font)
        self.main_lblHeader.setTextFormat(Qt.PlainText)
        self.main_lblHeader.setTextInteractionFlags(Qt.NoTextInteraction)

        # Sub Header Label
        self.main_lblSubHeader = QLabel(self.tabMain)
        self.main_lblSubHeader.setObjectName(u"main_lblSubHeader")
        self.main_lblSubHeader.setGeometry(QRect(10, 350, 471, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.main_lblSubHeader.setFont(font1)
        self.main_lblSubHeader.setFocusPolicy(Qt.NoFocus)
        self.main_lblSubHeader.setStyleSheet(u"color: green")
        self.main_lblSubHeader.setWordWrap(False)

        # Logo Label
        self.main_lblLogo = QLabel(self.tabMain)
        self.main_lblLogo.setObjectName(u"main_lblLogo")
        self.main_lblLogo.setGeometry(QRect(0, 0, 1021, 261))
        self.main_lblLogo.setPixmap(QPixmap(u"../gui/img/Logo.png"))

        # Group Box News
        self.main_gbxNews = QGroupBox(self.tabMain)
        self.main_gbxNews.setObjectName(u"main_gbxNews")
        self.main_gbxNews.setGeometry(QRect(10, 400, 1001, 291))

        # News Label
        self.main_lblNews = QLabel(self.main_gbxNews)
        self.main_lblNews.setObjectName(u"main_lblNews")
        self.main_lblNews.setGeometry(QRect(10, 40, 281, 21))
        self.tabWidget.addTab(self.tabMain, "")

        # Add Module UI Tabs
        self.PotTrayTab = PT_Tab(self.tabWidget)
        self.LeafAnnotationTab = LA_Tab(self.tabWidget)
        self.LeafCountingTab = LC_Tab(self.tabWidget)
        self.DataExtractionTab = DE_Tab(self.tabWidget)


        # Finish Building Main UI
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.main_btnAbout.clicked.connect(self.show_about)
        QMetaObject.connectSlotsByName(MainWindow)

    def show_about(self):
        msg = QMessageBox()
        msg.setWindowTitle("About")
        # Program Title
        msg.setText("<h1> Phenotiki </h1> <h2> True Phenotyping-in-a-box solution </h2> ")
        # Main Text of the About Page
        # Read Changelog in Hyperlink colour as well as "Freepik" "Plainicon" "www.flaticon.com"
        msg.setInformativeText(
            'Current Version 1.2 \n \nRead CHANGELOG\n  \nAuthor(s): M.Minervini[1], M.V.Giuffrida[1], S,Tsaftaris[2] '
            '\nIMT Advanced Studies of Lucca[1] \nUniversity of Edinburgh[2] \n '
            '\n Converted from "Phenotiki - True phenotyping-in-a-box solution"\n'
            '\n by Steven Dixon, Milena Bromm, Mateusz Glowacki as part of "Make Phenotiki Great Again" Edinburgh Napier University Group Project\n'
            '\n UI conversion by Steven Dixon, Maciej Garbowski, Ross Macleod and Lech Psztyk\n'
            '\nSoftware License reported in the user\'s manual. \n \nIcons made by Freepik, Plainicon'
            'from www.flaticon.com is licensed by CC BY 3.0')
        # Add Authors University Logos
        msg.setIconPixmap(QPixmap(u"../gui/img/unis.PNG"))

        x = msg.exec_()

    # add main tab items
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Phenotiki", None))
        MainWindow.setWindowFilePath("")
        self.main_btnAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.main_lblHeader.setText(QCoreApplication.translate("MainWindow", u"Phenotiki", None))
        self.main_lblSubHeader.setText(
            QCoreApplication.translate("MainWindow", u"True pheotyping-in-a-box solution", None))
        self.main_lblLogo.setText("")
        self.main_gbxNews.setTitle(QCoreApplication.translate("MainWindow", u"Updates / News", None))
        self.main_lblNews.setText(
            QCoreApplication.translate("MainWindow", u"Placeholder text of latest updates and news", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMain),
                                  QCoreApplication.translate("MainWindow", u"Main", None))

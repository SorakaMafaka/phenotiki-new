# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from phenotiki.main.gui.mplwidget import MplWidget
from phenotiki.main.gui.DE_UIFunction import *
from phenotiki.plugin.dataextraction.src.dataex import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # set main window
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 740)
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
        self.main_btnAbout = QPushButton(self.tabMain)
        self.main_btnAbout.setObjectName(u"main_btnAbout")
        self.main_btnAbout.setGeometry(QRect(900, 350, 111, 51))
        self.main_lblHeader = QLabel(self.tabMain)
        self.main_lblHeader.setObjectName(u"main_lblHeader")
        self.main_lblHeader.setGeometry(QRect(10, 280, 301, 81))
        font = QFont()
        font.setPointSize(40)
        self.main_lblHeader.setFont(font)
        self.main_lblHeader.setTextFormat(Qt.PlainText)
        self.main_lblHeader.setTextInteractionFlags(Qt.NoTextInteraction)
        self.main_lblSubHeader = QLabel(self.tabMain)
        self.main_lblSubHeader.setObjectName(u"main_lblSubHeader")
        self.main_lblSubHeader.setGeometry(QRect(10, 350, 471, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.main_lblSubHeader.setFont(font1)
        self.main_lblSubHeader.setFocusPolicy(Qt.NoFocus)
        self.main_lblSubHeader.setStyleSheet(u"color: green")
        self.main_lblSubHeader.setWordWrap(False)
        self.main_lblLogo = QLabel(self.tabMain)
        self.main_lblLogo.setObjectName(u"main_lblLogo")
        self.main_lblLogo.setGeometry(QRect(0, 0, 1021, 261))
        self.main_lblLogo.setPixmap(QPixmap(u"../gui/img/Logo.png"))
        self.main_gbxNews = QGroupBox(self.tabMain)
        self.main_gbxNews.setObjectName(u"main_gbxNews")
        self.main_gbxNews.setGeometry(QRect(10, 400, 1001, 291))
        self.main_lblNews = QLabel(self.main_gbxNews)
        self.main_lblNews.setObjectName(u"main_lblNews")
        self.main_lblNews.setGeometry(QRect(10, 40, 281, 21))
        self.tabWidget.addTab(self.tabMain, "")

        # Pot Tray Analysis Tab
        self.tabPotTrayAnalysis = QWidget()
        self.tabPotTrayAnalysis.setObjectName(u"tabPotTrayAnalysis")
        self.pt_gbxFileList = QGroupBox(self.tabPotTrayAnalysis)
        self.pt_gbxFileList.setObjectName(u"pt_gbxFileList")
        self.pt_gbxFileList.setGeometry(QRect(10, 20, 251, 671))
        self.pt_btnLoad = QPushButton(self.pt_gbxFileList)
        self.pt_btnLoad.setObjectName(u"pt_btnLoad")
        self.pt_btnLoad.setGeometry(QRect(10, 560, 231, 41))
        self.pt_btnImport = QPushButton(self.pt_gbxFileList)
        self.pt_btnImport.setObjectName(u"pt_btnImport")
        self.pt_btnImport.setGeometry(QRect(10, 610, 231, 41))
        self.pt_lstFileList = QListWidget(self.pt_gbxFileList)
        self.pt_lstFileList.setObjectName(u"pt_lstFileList")
        self.pt_lstFileList.setGeometry(QRect(10, 20, 231, 521))
        self.pt_gbxImage = QGroupBox(self.tabPotTrayAnalysis)
        self.pt_gbxImage.setObjectName(u"pt_gbxImage")
        self.pt_gbxImage.setGeometry(QRect(270, 20, 741, 521))
        self.pt_lblViewImage = QLabel(self.pt_gbxImage)
        self.pt_lblViewImage.setObjectName(u"pt_lblViewImage")
        self.pt_lblViewImage.mousePressEvent = self.getPos
        self.pt_lblViewImage.setPixmap(QPixmap(u"../gui/img/IMG_2013-09-28_08-00.png"))
        self.pt_lblViewImage.setGeometry(QRect(10, 40, 491, 401))
        self.pt_lblViewImage.setScaledContents(True)
        self.pt_horizontalSlider = QSlider(self.pt_gbxImage)
        self.pt_horizontalSlider.setObjectName(u"pt_horizontalSlider")
        self.pt_horizontalSlider.setGeometry(QRect(90, 470, 321, 31))
        self.pt_horizontalSlider.setOrientation(Qt.Horizontal)
        self.pt_cmbType = QComboBox(self.pt_gbxImage)
        self.pt_cmbType.addItem("")
        self.pt_cmbType.addItem("")
        self.pt_cmbType.addItem("")
        self.pt_cmbType.addItem("")
        self.pt_cmbType.setObjectName(u"pt_cmbType")
        self.pt_cmbType.setEnabled(False)
        self.pt_cmbType.setGeometry(QRect(590, 470, 121, 31))
        self.pt_cmbType.setFrame(True)
        self.pt_lstPlots = QListWidget(self.pt_gbxImage)
        self.pt_lstPlots.setObjectName(u"pt_lstPlots")
        self.pt_lstPlots.setGeometry(QRect(510, 30, 221, 431))
        self.pt_gbxToolbox = QGroupBox(self.tabPotTrayAnalysis)
        self.pt_gbxToolbox.setObjectName(u"pt_gbxToolbox")
        self.pt_gbxToolbox.setGeometry(QRect(270, 550, 741, 141))
        self.pt_progressBar = QProgressBar(self.pt_gbxToolbox)
        self.pt_progressBar.setObjectName(u"pt_progressBar")
        self.pt_progressBar.setGeometry(QRect(20, 60, 431, 31))
        self.pt_progressBar.setValue(0)
        self.pt_progressBar.setTextVisible(False)
        self.pt_btnSettings = QPushButton(self.pt_gbxToolbox)
        self.pt_btnSettings.setObjectName(u"pt_btnSettings")
        self.pt_btnSettings.setEnabled(False)
        self.pt_btnSettings.setGeometry(QRect(480, 20, 121, 51))
        self.pt_btnMask = QPushButton(self.pt_gbxToolbox)
        self.pt_btnMask.setObjectName(u"pt_btnMask")
        self.pt_btnMask.setEnabled(False)
        self.pt_btnMask.setGeometry(QRect(610, 20, 121, 51))
        self.pt_btnTraits = QPushButton(self.pt_gbxToolbox)
        self.pt_btnTraits.setObjectName(u"pt_btnTraits")
        self.pt_btnTraits.setEnabled(False)
        self.pt_btnTraits.setGeometry(QRect(480, 80, 121, 51))
        self.pt_btnSave = QPushButton(self.pt_gbxToolbox)
        self.pt_btnSave.setObjectName(u"pt_btnSave")
        self.pt_btnSave.setEnabled(False)
        self.pt_btnSave.setGeometry(QRect(610, 80, 121, 51))
        self.tabWidget.addTab(self.tabPotTrayAnalysis, "")

        # Leaf Labelling Tab
        self.tabLeafLabelling = QWidget()
        self.tabLeafLabelling.setObjectName(u"tabLeafLabelling")
        self.ll_gbxFileList_2 = QGroupBox(self.tabLeafLabelling)
        self.ll_gbxFileList_2.setObjectName(u"ll_gbxFileList_2")
        self.ll_gbxFileList_2.setGeometry(QRect(10, 20, 251, 671))
        self.ll_cbxSubject = QComboBox(self.ll_gbxFileList_2)
        self.ll_cbxSubject.setObjectName(u"ll_cbxSubject")
        self.ll_cbxSubject.setGeometry(QRect(10, 570, 221, 31))
        self.ll_lblSubject = QLabel(self.ll_gbxFileList_2)
        self.ll_lblSubject.setObjectName(u"ll_lblSubject")
        self.ll_lblSubject.setGeometry(QRect(10, 550, 55, 16))
        self.ll_lstFileListLL = QListView(self.ll_gbxFileList_2)
        self.ll_lstFileListLL.setObjectName(u"ll_lstFileListLL")
        self.ll_lstFileListLL.setGeometry(QRect(10, 20, 231, 521))
        self.ll_btnLoad = QPushButton(self.ll_gbxFileList_2)
        self.ll_btnLoad.setObjectName(u"ll_btnLoad")
        self.ll_btnLoad.setGeometry(QRect(10, 610, 221, 41))
        self.ll_gbxImage = QGroupBox(self.tabLeafLabelling)
        self.ll_gbxImage.setObjectName(u"ll_gbxImage")
        self.ll_gbxImage.setGeometry(QRect(270, 20, 741, 521))
        self.ll_horizontalSlider = QSlider(self.ll_gbxImage)
        self.ll_horizontalSlider.setObjectName(u"ll_horizontalSlider")
        self.ll_horizontalSlider.setGeometry(QRect(120, 470, 251, 21))
        self.ll_horizontalSlider.setOrientation(Qt.Horizontal)
        self.ll_cbxAnnotations = QCheckBox(self.ll_gbxImage)
        self.ll_cbxAnnotations.setObjectName(u"ll_cbxAnnotations")
        self.ll_cbxAnnotations.setGeometry(QRect(560, 470, 161, 20))
        self.ll_lblCurrent = QLabel(self.ll_gbxImage)
        self.ll_lblCurrent.setObjectName(u"lblCurrent")
        self.ll_lblCurrent.setGeometry(QRect(580, 440, 121, 16))
        self.ll_lstFileView = QListWidget(self.ll_gbxImage)
        self.ll_lstFileView.setObjectName(u"ll_lstFileView")
        self.ll_lstFileView.setGeometry(QRect(550, 190, 171, 241))
        self.ll_gbxToolbox = QGroupBox(self.tabLeafLabelling)
        self.ll_gbxToolbox.setObjectName(u"ll_gbxToolbox")
        self.ll_gbxToolbox.setGeometry(QRect(270, 550, 741, 141))
        self.tabWidget.addTab(self.tabLeafLabelling, "")

        # Leaf Counting Tab
        self.tabCounting = QWidget()
        self.tabCounting.setObjectName(u"tabCounting")
        self.lc_gbxPlantList = QGroupBox(self.tabCounting)
        self.lc_gbxPlantList.setObjectName(u"lc_gbxPlantList")
        self.lc_gbxPlantList.setGeometry(QRect(10, 20, 251, 671))
        self.lc_cmbSequence = QComboBox(self.lc_gbxPlantList)
        self.lc_cmbSequence.addItem("")
        self.lc_cmbSequence.setObjectName(u"lc_cmbSequence")
        self.lc_cmbSequence.setGeometry(QRect(100, 30, 91, 31))
        self.lc_lblSequ = QLabel(self.lc_gbxPlantList)
        self.lc_lblSequ.setObjectName(u"lc_lblSequ")
        self.lc_lblSequ.setGeometry(QRect(30, 30, 71, 21))
        self.lc_lblSequ.setAutoFillBackground(False)
        self.lc_lblSequ.setStyleSheet(u"background-color: none")
        self.lc_listWidget = QListWidget(self.lc_gbxPlantList)
        self.lc_listWidget.setObjectName(u"lc_listWidget")
        self.lc_listWidget.setGeometry(QRect(10, 70, 231, 391))
        self.lc_btnLoad = QPushButton(self.lc_gbxPlantList)
        self.lc_btnLoad.setObjectName(u"lc_btnLoad")
        self.lc_btnLoad.setGeometry(QRect(10, 570, 231, 41))
        self.lc_import = QPushButton(self.lc_gbxPlantList)
        self.lc_import.setObjectName(u"lc_import")
        self.lc_import.setGeometry(QRect(10, 620, 151, 41))
        self.lc_lblTotalNumPlants = QLabel(self.lc_gbxPlantList)
        self.lc_lblTotalNumPlants.setObjectName(u"lc_lblTotalNumPlants")
        self.lc_lblTotalNumPlants.setGeometry(QRect(30, 480, 141, 16))
        self.lc_lblTrainingSetSize = QLabel(self.lc_gbxPlantList)
        self.lc_lblTrainingSetSize.setObjectName(u"lc_lblTrainingSetSize")
        self.lc_lblTrainingSetSize.setGeometry(QRect(30, 510, 111, 16))
        self.lc_lblTestingSetSize = QLabel(self.lc_gbxPlantList)
        self.lc_lblTestingSetSize.setObjectName(u"lc_lblTestingSetSize")
        self.lc_lblTestingSetSize.setGeometry(QRect(30, 540, 101, 16))
        self.lc_lblTotalNumber = QLabel(self.lc_gbxPlantList)
        self.lc_lblTotalNumber.setObjectName(u"lc_lblTotalNumber")
        self.lc_lblTotalNumber.setGeometry(QRect(180, 480, 41, 16))
        self.lc_lblTrainingSizeNumber = QLabel(self.lc_gbxPlantList)
        self.lc_lblTrainingSizeNumber.setObjectName(u"lc_lblTrainingSizeNumber")
        self.lc_lblTrainingSizeNumber.setGeometry(QRect(180, 510, 41, 16))
        self.lc_lblTestingNumber = QLabel(self.lc_gbxPlantList)
        self.lc_lblTestingNumber.setObjectName(u"lc_lblTestingNumber")
        self.lc_lblTestingNumber.setGeometry(QRect(180, 540, 41, 16))
        self.lc_gbx_tt = QGroupBox(self.tabCounting)
        self.lc_gbx_tt.setObjectName(u"lc_gbx_tt")
        self.lc_gbx_tt.setGeometry(QRect(270, 20, 741, 671))
        self.lc_cbxTraining = QComboBox(self.lc_gbx_tt)
        self.lc_cbxTraining.addItem("")
        self.lc_cbxTraining.addItem("")
        self.lc_cbxTraining.setObjectName(u"lc_cbxTraining")
        self.lc_cbxTraining.setGeometry(QRect(280, 20, 271, 41))
        self.lc_cbxTesting = QComboBox(self.lc_gbx_tt)
        self.lc_cbxTesting.addItem("")
        self.lc_cbxTesting.addItem("")
        self.lc_cbxTesting.addItem("")
        self.lc_cbxTesting.addItem("")
        self.lc_cbxTesting.setObjectName(u"lc_cbxTesting")
        self.lc_cbxTesting.setGeometry(QRect(280, 70, 271, 41))
        self.lc__tbName = QLineEdit(self.lc_gbx_tt)
        self.lc__tbName.setObjectName(u"lc__tbName")
        self.lc__tbName.setEnabled(False)
        self.lc__tbName.setGeometry(QRect(280, 120, 271, 31))
        self.lc_progressBar = QProgressBar(self.lc_gbx_tt)
        self.lc_progressBar.setObjectName(u"lc_progressBar")
        self.lc_progressBar.setGeometry(QRect(60, 180, 611, 23))
        self.lc_progressBar.setValue(0)
        self.lc_progressBar.setTextVisible(False)
        self.lc_btnTraining = QPushButton(self.lc_gbx_tt)
        self.lc_btnTraining.setObjectName(u"lc_btnTraining")
        self.lc_btnTraining.setGeometry(QRect(90, 240, 261, 41))
        self.lc_btnTraining.setStyleSheet(u"")
        self.lc_btnAdvanced = QPushButton(self.lc_gbx_tt)
        self.lc_btnAdvanced.setObjectName(u"lc_btnAdvanced")
        self.lc_btnAdvanced.setGeometry(QRect(360, 240, 261, 41))
        self.lc_btnAdvanced.setStyleSheet(u"")
        self.lc_btnTesting = QPushButton(self.lc_gbx_tt)
        self.lc_btnTesting.setObjectName(u"lc_btnTesting")
        self.lc_btnTesting.setGeometry(QRect(90, 300, 261, 41))
        self.lc_btnTesting.setStyleSheet(u"")
        self.lc_btnSave = QPushButton(self.lc_gbx_tt)
        self.lc_btnSave.setObjectName(u"lc_btnSave")
        self.lc_btnSave.setGeometry(QRect(360, 300, 261, 41))
        self.lc_btnSave.setStyleSheet(u"")
        self.lc_gbxResults = QGroupBox(self.lc_gbx_tt)
        self.lc_gbxResults.setObjectName(u"lc_gbxResults")
        self.lc_gbxResults.setGeometry(QRect(10, 350, 721, 311))
        self.lc_cbxType = QComboBox(self.lc_gbxResults)
        self.lc_cbxType.addItem("")
        self.lc_cbxType.addItem("")
        self.lc_cbxType.addItem("")
        self.lc_cbxType.addItem("")
        self.lc_cbxType.setObjectName(u"lc_cbxType")
        self.lc_cbxType.setGeometry(QRect(80, 220, 261, 31))
        self.lc_cbxLog = QComboBox(self.lc_gbxResults)
        self.lc_cbxLog.addItem("")
        self.lc_cbxLog.addItem("")
        self.lc_cbxLog.addItem("")
        self.lc_cbxLog.setObjectName(u"lc_cbxLog")
        self.lc_cbxLog.setGeometry(QRect(370, 220, 261, 31))
        self.lc_cbxTT = QComboBox(self.lc_gbxResults)
        self.lc_cbxTT.addItem("")
        self.lc_cbxTT.addItem("")
        self.lc_cbxTT.setObjectName(u"lc_cbxTT")
        self.lc_cbxTT.setGeometry(QRect(80, 260, 261, 31))
        self.lc_lstView = QListView(self.lc_gbxResults)
        self.lc_lstView.setObjectName(u"lc_lstView")
        self.lc_lstView.setGeometry(QRect(40, 30, 641, 81))
        self.lc_tblView = QTableView(self.lc_gbxResults)
        self.lc_tblView.setObjectName(u"lc_tblView")
        self.lc_tblView.setGeometry(QRect(40, 120, 641, 81))
        self.lc_btnAssignCount = QPushButton(self.lc_gbxResults)
        self.lc_btnAssignCount.setObjectName(u"lc_btnAssignCount")
        self.lc_btnAssignCount.setGeometry(QRect(370, 260, 261, 31))
        self.lc_lblTrainingSamples = QLabel(self.lc_gbx_tt)
        self.lc_lblTrainingSamples.setObjectName(u"lc_lblTrainingSamples")
        self.lc_lblTrainingSamples.setGeometry(QRect(160, 30, 111, 16))
        self.lc_lblTestingSamples = QLabel(self.lc_gbx_tt)
        self.lc_lblTestingSamples.setObjectName(u"lc_lblTestingSamples")
        self.lc_lblTestingSamples.setGeometry(QRect(160, 80, 111, 16))
        self.lc_lblNameTest = QLabel(self.lc_gbx_tt)
        self.lc_lblNameTest.setObjectName(u"lc_lblNameTest")
        self.lc_lblNameTest.setGeometry(QRect(160, 130, 111, 16))
        self.tabWidget.addTab(self.tabCounting, "")

        # Data Extraction Tab
        self.tabDataExtraction = QWidget()
        self.tabDataExtraction.setObjectName(u"tabDataExtraction")
        self.de_gbxPhenoData = QGroupBox(self.tabDataExtraction)
        self.de_gbxPhenoData.setObjectName(u"de_gbxPhenoData")
        self.de_gbxPhenoData.setGeometry(QRect(10, 20, 251, 511))
        self.de_wgtPhenoData = QListWidget(self.de_gbxPhenoData)
        self.dataSelections = ["ProjectedLeafArea", "Diameter", "Perimeter", "Stockiness", "Compactness", "Hue",
                               "Count", "RelativeRateChange", "AbsoluteGrowthRate", "RelativeGrowthRate"]
        self.de_wgtPhenoData.addItems(self.dataSelections)
        self.de_wgtPhenoData.clicked.connect(self.on_Choice)
        self.de_wgtPhenoData.setObjectName(u"de_wgtPhenoData")
        self.de_wgtPhenoData.setEnabled(True)
        self.de_wgtPhenoData.setGeometry(QRect(10, 20, 231, 361))
        self.de_cbxCm = QCheckBox(self.de_gbxPhenoData)
        self.de_cbxCm.setObjectName(u"de_cbxCm")
        self.de_cbxCm.setGeometry(QRect(40, 390, 151, 21))
        self.de_btnLoadDE = QPushButton(self.de_gbxPhenoData)
        self.de_btnLoadDE.setObjectName(u"de_btnLoadDE")
        self.de_btnLoadDE.setGeometry(QRect(60, 430, 121, 51))
        self.de_btnLoadDE.clicked.connect(loadDataset)
        self.de_gbxPlotParams = QGroupBox(self.tabDataExtraction)
        self.de_gbxPlotParams.setObjectName(u"de_gbxPlotParams")
        self.de_gbxPlotParams.setGeometry(QRect(10, 530, 1001, 171))
        self.de_cbxFrom = QComboBox(self.de_gbxPlotParams)
        self.de_cbxFrom.setObjectName(u"de_cbxFrom")
        self.de_cbxFrom.addItem("N/A")
        self.de_cbxFrom.setGeometry(QRect(160, 50, 221, 31))
        self.de_cbxFrom.setEnabled(False)
        self.de_cbxFrom.activated[int].connect(self.update_from)
        self.de_cbxTo = QComboBox(self.de_gbxPlotParams)
        self.de_cbxTo.setObjectName(u"de_cbxTo")
        self.de_cbxTo.addItem("N/A")
        self.de_cbxTo.setGeometry(QRect(160, 120, 221, 31))
        self.de_cbxTo.setEnabled(False)
        self.de_cbxTo.activated[int].connect(self.update_from)
        self.de_cbxShow = QComboBox(self.de_gbxPlotParams)
        self.de_cbxShow.setObjectName(u"de_cbxShow")
        self.de_cbxShow.setGeometry(QRect(490, 50, 221, 31))
        self.de_cbxShow.addItem("All")
        self.de_cbxShow.setEnabled(False)
        self.de_cbxSpecify = QComboBox(self.de_gbxPlotParams)
        self.de_cbxSpecify.setObjectName(u"de_cbxSpecify")
        self.de_cbxSpecify.setGeometry(QRect(490, 120, 221, 31))
        self.de_cbxSpecify.addItem("N/A")
        self.de_cbxSpecify.setEnabled(False)
        self.de_lblFrom = QLabel(self.de_gbxPlotParams)
        self.de_lblFrom.setObjectName(u"de_lblFrom")
        self.de_lblFrom.setGeometry(QRect(100, 60, 55, 16))
        font2 = QFont()
        font2.setPointSize(12)
        self.de_lblFrom.setFont(font2)
        self.de_lblTo = QLabel(self.de_gbxPlotParams)
        self.de_lblTo.setObjectName(u"de_lblTo")
        self.de_lblTo.setGeometry(QRect(120, 130, 31, 16))
        self.de_lblTo.setFont(font2)
        self.de_lblShow = QLabel(self.de_gbxPlotParams)
        self.de_lblShow.setObjectName(u"de_lblShow")
        self.de_lblShow.setGeometry(QRect(420, 60, 55, 16))
        self.de_lblShow.setFont(font2)
        self.de_lblSpecify = QLabel(self.de_gbxPlotParams)
        self.de_lblSpecify.setObjectName(u"de_lblSpecify")
        self.de_lblSpecify.setGeometry(QRect(410, 120, 81, 31))
        self.de_lblSpecify.setFont(font2)
        self.de_btnSaveDE = QPushButton(self.de_gbxPlotParams)
        self.de_btnSaveDE.setObjectName(u"de_btnSaveDE")
        self.de_btnSaveDE.setGeometry(QRect(830, 30, 131, 51))
        self.de_btnSaveDE.setEnabled(False)
        self.de_btnSaveDE.clicked.connect(self.save_plot)
        self.de_btnExportDE = QPushButton(self.de_gbxPlotParams)
        self.de_btnExportDE.setObjectName(u"de_btnExportDE")
        self.de_btnExportDE.setGeometry(QRect(830, 100, 131, 51))
        self.de_btnExportDE.setEnabled(False)
        self.de_gbxMatPlot = QGroupBox(self.tabDataExtraction)
        self.de_gbxMatPlot.setObjectName(u"de_gbxMatPlot")
        self.de_gbxMatPlot.setGeometry(QRect(270, 20, 741, 511))
        self.de_MplWidget = MplWidget(self.de_gbxMatPlot)
        self.de_MplWidget.setObjectName(u"de_MplWidget")
        self.de_MplWidget.setGeometry(QRect(10, 20, 721, 481))
        self.tabWidget.addTab(self.tabDataExtraction, "")
        self.de_gbxMatPlot.raise_()
        self.de_gbxPhenoData.raise_()
        self.de_gbxPlotParams.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pt_cmbType.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        # add main tab items
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

        # add pt items
        self.pt_gbxFileList.setTitle(QCoreApplication.translate("MainWindow", u"File List", None))
        self.pt_btnLoad.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.pt_btnImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.pt_gbxImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.pt_cmbType.setItemText(0, QCoreApplication.translate("MainWindow", u"Raw Image", None))
        self.pt_cmbType.setItemText(1, QCoreApplication.translate("MainWindow", u"Detected Plants", None))
        self.pt_cmbType.setItemText(2, QCoreApplication.translate("MainWindow", u"Contour", None))
        self.pt_cmbType.setItemText(3, QCoreApplication.translate("MainWindow", u"FG Mask", None))
        self.pt_cmbType.setCurrentText(QCoreApplication.translate("MainWindow", u"Raw Image", None))
        self.pt_lblViewImage.setText("")
        self.pt_gbxToolbox.setTitle(QCoreApplication.translate("MainWindow", u"Toolbox", None))
        self.pt_btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pt_btnMask.setText(QCoreApplication.translate("MainWindow", u"Extract Mask", None))
        self.pt_btnTraits.setText(QCoreApplication.translate("MainWindow", u"Get Traits", None))
        self.pt_btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabPotTrayAnalysis),
                                  QCoreApplication.translate("MainWindow", u"Pot Tray Analysis", None))

        # add leaf lavelling items
        self.ll_gbxFileList_2.setTitle(QCoreApplication.translate("MainWindow", u"File List", None))
        self.ll_lblSubject.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
        self.ll_btnLoad.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.ll_gbxImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.ll_cbxAnnotations.setText(QCoreApplication.translate("MainWindow", u"Show/Hide Annotations", None))
        self.ll_lblCurrent.setText(QCoreApplication.translate("MainWindow", u"Current Label: new", None))
        self.ll_gbxToolbox.setTitle(QCoreApplication.translate("MainWindow", u"Toolbox", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLeafLabelling),
                                  QCoreApplication.translate("MainWindow", u"Leaf Labelling", None))

        #add leaf counting items
        self.lc_gbxPlantList.setTitle(QCoreApplication.translate("MainWindow", u"Plant List", None))
        self.lc_cmbSequence.setItemText(0, QCoreApplication.translate("MainWindow", u"N/A", None))
        self.lc_lblSequ.setText(QCoreApplication.translate("MainWindow", u"Sequence:", None))
        self.lc_btnLoad.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.lc_import.setText(QCoreApplication.translate("MainWindow", u"Import Count from CSV", None))
        self.lc_lblTotalNumPlants.setText(QCoreApplication.translate("MainWindow", u"Total Number of Plants:", None))
        self.lc_lblTrainingSetSize.setText(QCoreApplication.translate("MainWindow", u"Training Set Size:", None))
        self.lc_lblTestingSetSize.setText(QCoreApplication.translate("MainWindow", u"Testing Set Size:", None))
        self.lc_lblTotalNumber.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lc_lblTrainingSizeNumber.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lc_lblTestingNumber.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lc_gbx_tt.setTitle(QCoreApplication.translate("MainWindow", u"Training/Testing Setup", None))
        self.lc_cbxTraining.setItemText(0, QCoreApplication.translate("MainWindow", u"All labelled images", None))
        self.lc_cbxTraining.setItemText(1, QCoreApplication.translate("MainWindow", u"Custom...", None))
        self.lc_cbxTesting.setItemText(0, QCoreApplication.translate("MainWindow", u"All unlabelled images", None))
        self.lc_cbxTesting.setItemText(1, QCoreApplication.translate("MainWindow", u"All labelled images", None))
        self.lc_cbxTesting.setItemText(2, QCoreApplication.translate("MainWindow", u"All", None))
        self.lc_cbxTesting.setItemText(3, QCoreApplication.translate("MainWindow", u"Custom...", None))
        self.lc__tbName.setText(QCoreApplication.translate("MainWindow", u"No name", None))
        self.lc_btnTraining.setText(QCoreApplication.translate("MainWindow", u"Start Training", None))
        self.lc_btnAdvanced.setText(QCoreApplication.translate("MainWindow", u"Advanced Options...", None))
        self.lc_btnTesting.setText(QCoreApplication.translate("MainWindow", u"Start Testing", None))
        self.lc_btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.lc_gbxResults.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.lc_cbxType.setItemText(0, QCoreApplication.translate("MainWindow", u"LASSO", None))
        self.lc_cbxType.setItemText(1, QCoreApplication.translate("MainWindow", u"RandomForest", None))
        self.lc_cbxType.setItemText(2, QCoreApplication.translate("MainWindow", u"SVR", None))
        self.lc_cbxType.setItemText(3, QCoreApplication.translate("MainWindow", u"SVR_OPT", None))
        self.lc_cbxLog.setItemText(0, QCoreApplication.translate("MainWindow", u"Logpolar", None))
        self.lc_cbxLog.setItemText(1, QCoreApplication.translate("MainWindow", u"Cartesian", None))
        self.lc_cbxLog.setItemText(2, QCoreApplication.translate("MainWindow", u"Combined", None))
        self.lc_cbxTT.setItemText(0, QCoreApplication.translate("MainWindow", u"Training Results", None))
        self.lc_cbxTT.setItemText(1, QCoreApplication.translate("MainWindow", u"Testing Results", None))
        self.lc_btnAssignCount.setText(QCoreApplication.translate("MainWindow", u"Assign Count", None))
        self.lc_lblTrainingSamples.setText(QCoreApplication.translate("MainWindow", u"Training Samples:", None))
        self.lc_lblTestingSamples.setText(QCoreApplication.translate("MainWindow", u"Testing Samples:", None))
        self.lc_lblNameTest.setText(QCoreApplication.translate("MainWindow", u"Name of the test:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCounting),
                                  QCoreApplication.translate("MainWindow", u"Leaf Counting", None))

        # add data extraction items
        self.de_gbxPhenoData.setTitle(QCoreApplication.translate("MainWindow", u"Phenotyping Data", None))
        __sortingEnabled = self.de_wgtPhenoData.isSortingEnabled()
        self.de_wgtPhenoData.setSortingEnabled(False)
        self.de_wgtPhenoData.setSortingEnabled(__sortingEnabled)
        self.de_cbxCm.setText(QCoreApplication.translate("MainWindow", u"Convert values to cm", None))
        self.de_btnLoadDE.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.de_gbxPlotParams.setTitle(QCoreApplication.translate("MainWindow", u"Plot Patameters", None))
        self.de_lblFrom.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.de_lblTo.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.de_lblShow.setText(QCoreApplication.translate("MainWindow", u"Show:", None))
        self.de_lblSpecify.setText(QCoreApplication.translate("MainWindow", u"Specify:", None))
        self.de_btnSaveDE.setText(QCoreApplication.translate("MainWindow", u"Save Plot As...", None))
        self.de_btnExportDE.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.de_gbxMatPlot.setTitle(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDataExtraction),
                                  QCoreApplication.translate("MainWindow", u"Data Extraction", None))

    # retranslateUi

    def on_Choice(self):
        select = self.de_wgtPhenoData.currentItem().text()
        plot_graph(self, select)

    def save_plot(self):
        w = QWidget()
        path = (QFileDialog.getSaveFileName(w, 'Save as', "", '*.png'))
        print(path[0])
        self.de_MplWidget.canvas.figure.savefig(path[0])
        #self.de_MplWidget

    def update_from(self, index):
        UpdateFrom(self, index)

    def update_to(self, index):
        UpdateTo(self, index)
    def getPos(self, event):
        x = event.pos().x()
        y = event.pos().y()
        print(x, y)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading gui file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling gui file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide2.QtGui import (QFont,
                           QIcon, QPixmap)
from PySide2.QtWidgets import *

from phenotiki.main.gui.mplwidget import MplWidget
#from phenotiki.plugin.dataextraction.src.DE_UIFunction


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1024, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(1024, 768))
        icon = QIcon()
        icon.addFile(u"../gui/img/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabPotTray = QTabWidget(self.centralwidget)
        self.tabPotTray.setObjectName(u"tabPotTray")
        self.tabPotTray.setGeometry(QRect(0, 0, 1031, 771))
        self.tabMain = QWidget()
        self.tabMain.setObjectName(u"tabMain")
        sizePolicy.setHeightForWidth(self.tabMain.sizePolicy().hasHeightForWidth())
        self.tabMain.setSizePolicy(sizePolicy)
        self.btnAbout = QPushButton(self.tabMain)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setGeometry(QRect(900, 350, 111, 51))
        self.lblHeader = QLabel(self.tabMain)
        self.lblHeader.setObjectName(u"lblHeader")
        self.lblHeader.setGeometry(QRect(10, 280, 301, 81))
        font = QFont()
        font.setPointSize(40)
        self.lblHeader.setFont(font)
        self.lblHeader.setTextFormat(Qt.PlainText)
        self.lblHeader.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label = QLabel(self.tabMain)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 350, 471, 41))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setFocusPolicy(Qt.NoFocus)
        self.label.setStyleSheet(u"color: green")
        self.label.setWordWrap(False)
        self.lblLogo = QLabel(self.tabMain)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setGeometry(QRect(0, 0, 1021, 261))
        self.lblLogo.setPixmap(QPixmap(u"../gui/img/Logo.png"))
        self.groupBox_2 = QGroupBox(self.tabMain)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 400, 1001, 291))
        self.lblNews = QLabel(self.groupBox_2)
        self.lblNews.setObjectName(u"lblNews")
        self.lblNews.setGeometry(QRect(10, 40, 281, 21))
        self.tabPotTray.addTab(self.tabMain, "")
        self.tabPotTrayAnalysis = QWidget()
        self.tabPotTrayAnalysis.setObjectName(u"tabPotTrayAnalysis")
        self.gbxFileList = QGroupBox(self.tabPotTrayAnalysis)
        self.gbxFileList.setObjectName(u"gbxFileList")
        self.gbxFileList.setGeometry(QRect(10, 20, 251, 671))
        self.btnLoad = QPushButton(self.gbxFileList)
        self.btnLoad.setObjectName(u"btnLoad")
        self.btnLoad.setGeometry(QRect(10, 560, 231, 41))
        self.btnImport = QPushButton(self.gbxFileList)
        self.btnImport.setObjectName(u"btnImport")
        self.btnImport.setGeometry(QRect(10, 610, 231, 41))
        self.lstFileList = QListWidget(self.gbxFileList)
        self.lstFileList.setObjectName(u"lstFileList")
        self.lstFileList.setGeometry(QRect(10, 20, 231, 521))
        self.gbxImage = QGroupBox(self.tabPotTrayAnalysis)
        self.gbxImage.setObjectName(u"gbxImage")
        self.gbxImage.setGeometry(QRect(270, 20, 741, 521))
        self.horizontalSlider = QSlider(self.gbxImage)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(90, 470, 321, 31))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.cmbType = QComboBox(self.gbxImage)
        self.cmbType.addItem("")
        self.cmbType.addItem("")
        self.cmbType.addItem("")
        self.cmbType.addItem("")
        self.cmbType.setObjectName(u"cmbType")
        self.cmbType.setEnabled(False)
        self.cmbType.setGeometry(QRect(590, 470, 121, 31))
        self.cmbType.setFrame(True)
        self.lstPlots = QListWidget(self.gbxImage)
        self.lstPlots.setObjectName(u"lstPlots")
        self.lstPlots.setGeometry(QRect(510, 30, 221, 431))
        self.gbxToolbox_PTA = QGroupBox(self.tabPotTrayAnalysis)
        self.gbxToolbox_PTA.setObjectName(u"gbxToolbox_PTA")
        self.gbxToolbox_PTA.setGeometry(QRect(270, 550, 741, 141))
        self.progressBar = QProgressBar(self.gbxToolbox_PTA)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 60, 431, 31))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.btnSettings = QPushButton(self.gbxToolbox_PTA)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setEnabled(False)
        self.btnSettings.setGeometry(QRect(480, 20, 121, 51))
        self.btnMask = QPushButton(self.gbxToolbox_PTA)
        self.btnMask.setObjectName(u"btnMask")
        self.btnMask.setEnabled(False)
        self.btnMask.setGeometry(QRect(610, 20, 121, 51))
        self.btnTraits = QPushButton(self.gbxToolbox_PTA)
        self.btnTraits.setObjectName(u"btnTraits")
        self.btnTraits.setEnabled(False)
        self.btnTraits.setGeometry(QRect(480, 80, 121, 51))
        self.btnSave = QPushButton(self.gbxToolbox_PTA)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setEnabled(False)
        self.btnSave.setGeometry(QRect(610, 80, 121, 51))
        self.tabPotTray.addTab(self.tabPotTrayAnalysis, "")
        self.tabLeafLabelling = QWidget()
        self.tabLeafLabelling.setObjectName(u"tabLeafLabelling")
        self.gbxFileList_2 = QGroupBox(self.tabLeafLabelling)
        self.gbxFileList_2.setObjectName(u"gbxFileList_2")
        self.gbxFileList_2.setGeometry(QRect(10, 20, 251, 671))
        self.cbxSubject = QComboBox(self.gbxFileList_2)
        self.cbxSubject.setObjectName(u"cbxSubject")
        self.cbxSubject.setGeometry(QRect(10, 570, 221, 31))
        self.lblSubject = QLabel(self.gbxFileList_2)
        self.lblSubject.setObjectName(u"lblSubject")
        self.lblSubject.setGeometry(QRect(10, 550, 55, 16))
        self.lstFileListLL = QListView(self.gbxFileList_2)
        self.lstFileListLL.setObjectName(u"lstFileListLL")
        self.lstFileListLL.setGeometry(QRect(10, 20, 231, 521))
        self.btnLoad_2 = QPushButton(self.gbxFileList_2)
        self.btnLoad_2.setObjectName(u"btnLoad_2")
        self.btnLoad_2.setGeometry(QRect(10, 610, 221, 41))
        self.gbxImage_LL = QGroupBox(self.tabLeafLabelling)
        self.gbxImage_LL.setObjectName(u"gbxImage_LL")
        self.gbxImage_LL.setGeometry(QRect(270, 20, 741, 521))
        self.horizontalSlider_2 = QSlider(self.gbxImage_LL)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(120, 470, 251, 21))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)
        self.cbxAnnotations = QCheckBox(self.gbxImage_LL)
        self.cbxAnnotations.setObjectName(u"cbxAnnotations")
        self.cbxAnnotations.setGeometry(QRect(560, 470, 161, 20))
        self.lblCurrent = QLabel(self.gbxImage_LL)
        self.lblCurrent.setObjectName(u"lblCurrent")
        self.lblCurrent.setGeometry(QRect(580, 440, 121, 16))
        self.lstFileView = QListWidget(self.gbxImage_LL)
        self.lstFileView.setObjectName(u"lstFileView")
        self.lstFileView.setGeometry(QRect(550, 190, 171, 241))
        self.gbxToolbox = QGroupBox(self.tabLeafLabelling)
        self.gbxToolbox.setObjectName(u"gbxToolbox")
        self.gbxToolbox.setGeometry(QRect(270, 550, 741, 141))
        self.tabPotTray.addTab(self.tabLeafLabelling, "")
        self.tabCounting = QWidget()
        self.tabCounting.setObjectName(u"tabCounting")
        self.gbxPlantList = QGroupBox(self.tabCounting)
        self.gbxPlantList.setObjectName(u"gbxPlantList")
        self.gbxPlantList.setGeometry(QRect(10, 20, 251, 671))
        self.cmbSequence = QComboBox(self.gbxPlantList)
        self.cmbSequence.addItem("")
        self.cmbSequence.setObjectName(u"cmbSequence")
        self.cmbSequence.setGeometry(QRect(100, 30, 91, 31))
        self.lblSequ = QLabel(self.gbxPlantList)
        self.lblSequ.setObjectName(u"lblSequ")
        self.lblSequ.setGeometry(QRect(30, 30, 71, 21))
        self.lblSequ.setAutoFillBackground(False)
        self.lblSequ.setStyleSheet(u"background-color: none")
        self.listWidget_2 = QListWidget(self.gbxPlantList)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(10, 70, 231, 391))
        self.btnLoad_LC = QPushButton(self.gbxPlantList)
        self.btnLoad_LC.setObjectName(u"btnLoad_LC")
        self.btnLoad_LC.setGeometry(QRect(10, 570, 231, 41))
        self.btnLoad_4 = QPushButton(self.gbxPlantList)
        self.btnLoad_4.setObjectName(u"btnLoad_4")
        self.btnLoad_4.setGeometry(QRect(10, 620, 151, 41))
        self.lblTotalNumPlants = QLabel(self.gbxPlantList)
        self.lblTotalNumPlants.setObjectName(u"lblTotalNumPlants")
        self.lblTotalNumPlants.setGeometry(QRect(30, 480, 141, 16))
        self.lblTrainingSetSize = QLabel(self.gbxPlantList)
        self.lblTrainingSetSize.setObjectName(u"lblTrainingSetSize")
        self.lblTrainingSetSize.setGeometry(QRect(30, 510, 111, 16))
        self.lblTestingSetSize = QLabel(self.gbxPlantList)
        self.lblTestingSetSize.setObjectName(u"lblTestingSetSize")
        self.lblTestingSetSize.setGeometry(QRect(30, 540, 101, 16))
        self.lblTotalNumber = QLabel(self.gbxPlantList)
        self.lblTotalNumber.setObjectName(u"lblTotalNumber")
        self.lblTotalNumber.setGeometry(QRect(180, 480, 41, 16))
        self.lblTrainingSizeNumber = QLabel(self.gbxPlantList)
        self.lblTrainingSizeNumber.setObjectName(u"lblTrainingSizeNumber")
        self.lblTrainingSizeNumber.setGeometry(QRect(180, 510, 41, 16))
        self.lblTestingNumber = QLabel(self.gbxPlantList)
        self.lblTestingNumber.setObjectName(u"lblTestingNumber")
        self.lblTestingNumber.setGeometry(QRect(180, 540, 41, 16))
        self.gbxtt = QGroupBox(self.tabCounting)
        self.gbxtt.setObjectName(u"gbxtt")
        self.gbxtt.setGeometry(QRect(270, 20, 741, 671))
        self.cbxTraining = QComboBox(self.gbxtt)
        self.cbxTraining.addItem("")
        self.cbxTraining.addItem("")
        self.cbxTraining.setObjectName(u"cbxTraining")
        self.cbxTraining.setGeometry(QRect(280, 20, 271, 41))
        self.cbxTesting = QComboBox(self.gbxtt)
        self.cbxTesting.addItem("")
        self.cbxTesting.addItem("")
        self.cbxTesting.addItem("")
        self.cbxTesting.addItem("")
        self.cbxTesting.setObjectName(u"cbxTesting")
        self.cbxTesting.setGeometry(QRect(280, 70, 271, 41))
        self.leName = QLineEdit(self.gbxtt)
        self.leName.setObjectName(u"leName")
        self.leName.setEnabled(False)
        self.leName.setGeometry(QRect(280, 120, 271, 31))
        self.progressBar_2 = QProgressBar(self.gbxtt)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setGeometry(QRect(60, 180, 611, 23))
        self.progressBar_2.setValue(0)
        self.progressBar_2.setTextVisible(False)
        self.btnTraining = QPushButton(self.gbxtt)
        self.btnTraining.setObjectName(u"btnTraining")
        self.btnTraining.setGeometry(QRect(90, 240, 261, 41))
        self.btnTraining.setStyleSheet(u"")
        self.btnAdvanced = QPushButton(self.gbxtt)
        self.btnAdvanced.setObjectName(u"btnAdvanced")
        self.btnAdvanced.setGeometry(QRect(360, 240, 261, 41))
        self.btnAdvanced.setStyleSheet(u"")
        self.btnTesting = QPushButton(self.gbxtt)
        self.btnTesting.setObjectName(u"btnTesting")
        self.btnTesting.setGeometry(QRect(90, 300, 261, 41))
        self.btnTesting.setStyleSheet(u"")
        self.btnSave_2 = QPushButton(self.gbxtt)
        self.btnSave_2.setObjectName(u"btnSave_2")
        self.btnSave_2.setGeometry(QRect(360, 300, 261, 41))
        self.btnSave_2.setStyleSheet(u"")
        self.gbxResults = QGroupBox(self.gbxtt)
        self.gbxResults.setObjectName(u"gbxResults")
        self.gbxResults.setGeometry(QRect(10, 350, 721, 311))
        self.cbxType = QComboBox(self.gbxResults)
        self.cbxType.addItem("")
        self.cbxType.addItem("")
        self.cbxType.addItem("")
        self.cbxType.addItem("")
        self.cbxType.setObjectName(u"cbxType")
        self.cbxType.setGeometry(QRect(80, 220, 261, 31))
        self.cbxLog = QComboBox(self.gbxResults)
        self.cbxLog.addItem("")
        self.cbxLog.addItem("")
        self.cbxLog.addItem("")
        self.cbxLog.setObjectName(u"cbxLog")
        self.cbxLog.setGeometry(QRect(370, 220, 261, 31))
        self.cbxTT = QComboBox(self.gbxResults)
        self.cbxTT.addItem("")
        self.cbxTT.addItem("")
        self.cbxTT.setObjectName(u"cbxTT")
        self.cbxTT.setGeometry(QRect(80, 260, 261, 31))
        self.lstView = QListView(self.gbxResults)
        self.lstView.setObjectName(u"lstView")
        self.lstView.setGeometry(QRect(40, 30, 641, 81))
        self.tblView = QTableView(self.gbxResults)
        self.tblView.setObjectName(u"tblView")
        self.tblView.setGeometry(QRect(40, 120, 641, 81))
        self.btnAssignCount = QPushButton(self.gbxResults)
        self.btnAssignCount.setObjectName(u"btnAssignCount")
        self.btnAssignCount.setGeometry(QRect(370, 260, 261, 31))
        self.lblTrainingSamples = QLabel(self.gbxtt)
        self.lblTrainingSamples.setObjectName(u"lblTrainingSamples")
        self.lblTrainingSamples.setGeometry(QRect(160, 30, 111, 16))
        self.lblTestingSamples = QLabel(self.gbxtt)
        self.lblTestingSamples.setObjectName(u"lblTestingSamples")
        self.lblTestingSamples.setGeometry(QRect(160, 80, 111, 16))
        self.lblNameTest = QLabel(self.gbxtt)
        self.lblNameTest.setObjectName(u"lblNameTest")
        self.lblNameTest.setGeometry(QRect(160, 130, 111, 16))
        self.tabPotTray.addTab(self.tabCounting, "")
        self.tabDataExtraction = QWidget()
        self.tabDataExtraction.setObjectName(u"tabDataExtraction")
        self.gbxPhenoData = QGroupBox(self.tabDataExtraction)
        self.gbxPhenoData.setObjectName(u"gbxPhenoData")
        self.gbxPhenoData.setGeometry(QRect(10, 20, 251, 511))
        #changed this part because it was hard to understand how to access sorry...
        self.wgtPhenoData = QListWidget(self.gbxPhenoData)
        self.dataSelections = ["ProjectedLeafArea", "Diameter", "Perimeter", "Stockiness", "Compactness", "Hue", "Count", "RelativeRateChange", "AbsoluteGrowthRate", "RelativeGrowthRate"]
        self.wgtPhenoData.addItems(self.dataSelections)
        self.wgtPhenoData.clicked.connect(self.on_Choice)



      #  self.wgtPhenoData.connect(self.on_Choice)
     #   QListWidgetItem(self.wgtPhenoData)
      #  QListWidgetItem(self.wgtPhenoData)
       # QListWidgetItem(self.wgtPhenoData)
        #QListWidgetItem(self.wgtPhenoData)
        #QListWidgetItem(self.wgtPhenoData)
        #QListWidgetItem(self.wgtPhenoData)
        #QListWidgetItem(self.wgtPhenoData)
        #QListWidgetItem(self.wgtPhenoData)
        #QListWidgetItem(self.wgtPhenoData)
        #QListWidgetItem(self.wgtPhenoData)
        self.wgtPhenoData.setObjectName(u"wgtPhenoData")
        self.wgtPhenoData.setEnabled(True)
        self.wgtPhenoData.setGeometry(QRect(10, 20, 231, 361))
      #  self.wgtPhenoData.
        self.cbxCm = QCheckBox(self.gbxPhenoData)
        self.cbxCm.setObjectName(u"cbxCm")
        self.cbxCm.setGeometry(QRect(40, 390, 151, 21))
        self.btnLoadDE = QPushButton(self.gbxPhenoData)
        self.btnLoadDE.setObjectName(u"btnLoadDE")
        self.btnLoadDE.clicked.connect(loadDataset)
        self.btnLoadDE.setGeometry(QRect(60, 430, 121, 51))
        self.gbxPlotParams = QGroupBox(self.tabDataExtraction)
        self.gbxPlotParams.setObjectName(u"gbxPlotParams")
        self.gbxPlotParams.setGeometry(QRect(10, 530, 1001, 171))
        self.comboBox = QComboBox(self.gbxPlotParams)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(160, 50, 221, 31))
        self.comboBox_2 = QComboBox(self.gbxPlotParams)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(160, 120, 221, 31))
        self.comboBox_3 = QComboBox(self.gbxPlotParams)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setGeometry(QRect(490, 50, 221, 31))
        self.comboBox_4 = QComboBox(self.gbxPlotParams)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(490, 120, 221, 31))
        self.lblFrom = QLabel(self.gbxPlotParams)
        self.lblFrom.setObjectName(u"lblFrom")
        self.lblFrom.setGeometry(QRect(100, 60, 55, 16))
        font2 = QFont()
        font2.setPointSize(12)
        self.lblFrom.setFont(font2)
        self.lblTo = QLabel(self.gbxPlotParams)
        self.lblTo.setObjectName(u"lblTo")
        self.lblTo.setGeometry(QRect(120, 130, 31, 16))
        self.lblTo.setFont(font2)
        self.lblShow = QLabel(self.gbxPlotParams)
        self.lblShow.setObjectName(u"lblShow")
        self.lblShow.setGeometry(QRect(420, 60, 55, 16))
        self.lblShow.setFont(font2)
        self.lblSpecify = QLabel(self.gbxPlotParams)
        self.lblSpecify.setObjectName(u"lblSpecify")
        self.lblSpecify.setGeometry(QRect(410, 120, 81, 31))
        self.lblSpecify.setFont(font2)
        self.btnSaveDE = QPushButton(self.gbxPlotParams)
        self.btnSaveDE.setObjectName(u"btnSaveDE")
        self.btnSaveDE.setGeometry(QRect(830, 30, 131, 51))
        self.btnExportDE = QPushButton(self.gbxPlotParams)
        self.btnExportDE.setObjectName(u"btnExportDE")
        self.btnExportDE.setGeometry(QRect(830, 100, 131, 51))
        self.gbxMatPlot = QGroupBox(self.tabDataExtraction)
        self.gbxMatPlot.setObjectName(u"gbxMatPlot")
        self.gbxMatPlot.setGeometry(QRect(270, 20, 741, 511))
        self.MplWidget = MplWidget(self.gbxMatPlot)
        self.MplWidget.setObjectName(u"MplWidget")
        self.MplWidget.setGeometry(QRect(10, 20, 721, 481))
        self.btnSaveDE.clicked.connect(self.save_plot)
        self.tabPotTray.addTab(self.tabDataExtraction, "")
        self.gbxMatPlot.raise_()
        self.gbxPhenoData.raise_()
        self.gbxPlotParams.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabPotTray.setCurrentIndex(0)
        self.cmbType.setCurrentIndex(0)

       # update_graph(self)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Phenotiki", None))
        MainWindow.setWindowFilePath("")
        self.btnAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.lblHeader.setText(QCoreApplication.translate("MainWindow", u"Phenotiki", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"True pheotyping-in-a-box solution", None))
        self.lblLogo.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Updates / News", None))
        self.lblNews.setText(QCoreApplication.translate("MainWindow", u"Placeholder text of latest updates and news", None))
        self.tabPotTray.setTabText(self.tabPotTray.indexOf(self.tabMain), QCoreApplication.translate("MainWindow", u"Main", None))
        self.gbxFileList.setTitle(QCoreApplication.translate("MainWindow", u"File List", None))
        self.btnLoad.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.btnImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.gbxImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.cmbType.setItemText(0, QCoreApplication.translate("MainWindow", u"Raw Image", None))
        self.cmbType.setItemText(1, QCoreApplication.translate("MainWindow", u"Detected Plants", None))
        self.cmbType.setItemText(2, QCoreApplication.translate("MainWindow", u"Contour", None))
        self.cmbType.setItemText(3, QCoreApplication.translate("MainWindow", u"FG Mask", None))

        self.cmbType.setCurrentText(QCoreApplication.translate("MainWindow", u"Raw Image", None))
        self.gbxToolbox_PTA.setTitle(QCoreApplication.translate("MainWindow", u"Toolbox", None))
        self.btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btnMask.setText(QCoreApplication.translate("MainWindow", u"Extract Mask", None))
        self.btnTraits.setText(QCoreApplication.translate("MainWindow", u"Get Traits", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabPotTray.setTabText(self.tabPotTray.indexOf(self.tabPotTrayAnalysis), QCoreApplication.translate("MainWindow", u"Pot tray Analysis", None))
        self.gbxFileList_2.setTitle(QCoreApplication.translate("MainWindow", u"File List", None))
        self.lblSubject.setText(QCoreApplication.translate("MainWindow", u"Subject:", None))
        self.btnLoad_2.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.gbxImage_LL.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.cbxAnnotations.setText(QCoreApplication.translate("MainWindow", u"Show/Hide Annotations", None))
        self.lblCurrent.setText(QCoreApplication.translate("MainWindow", u"Current Label: new", None))
        self.gbxToolbox.setTitle(QCoreApplication.translate("MainWindow", u"Toolbox", None))
        self.tabPotTray.setTabText(self.tabPotTray.indexOf(self.tabLeafLabelling), QCoreApplication.translate("MainWindow", u"Leaf Labelling", None))
        self.gbxPlantList.setTitle(QCoreApplication.translate("MainWindow", u"Plant List", None))
        self.cmbSequence.setItemText(0, QCoreApplication.translate("MainWindow", u"N/A", None))

        self.lblSequ.setText(QCoreApplication.translate("MainWindow", u"Sequence:", None))
        self.btnLoad_LC.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.btnLoad_4.setText(QCoreApplication.translate("MainWindow", u"Import Count from CSV", None))
        self.lblTotalNumPlants.setText(QCoreApplication.translate("MainWindow", u"Total Number of Plants:", None))
        self.lblTrainingSetSize.setText(QCoreApplication.translate("MainWindow", u"Training Set Size:", None))
        self.lblTestingSetSize.setText(QCoreApplication.translate("MainWindow", u"Testing Set Size:", None))
        self.lblTotalNumber.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblTrainingSizeNumber.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.lblTestingNumber.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.gbxtt.setTitle(QCoreApplication.translate("MainWindow", u"Training/Testing Setup", None))
        self.cbxTraining.setItemText(0, QCoreApplication.translate("MainWindow", u"All labelled images", None))
        self.cbxTraining.setItemText(1, QCoreApplication.translate("MainWindow", u"Custom...", None))

        self.cbxTesting.setItemText(0, QCoreApplication.translate("MainWindow", u"All unlabelled images", None))
        self.cbxTesting.setItemText(1, QCoreApplication.translate("MainWindow", u"All labelled images", None))
        self.cbxTesting.setItemText(2, QCoreApplication.translate("MainWindow", u"All", None))
        self.cbxTesting.setItemText(3, QCoreApplication.translate("MainWindow", u"Custom...", None))

        self.leName.setText(QCoreApplication.translate("MainWindow", u"No name", None))
        self.btnTraining.setText(QCoreApplication.translate("MainWindow", u"Start Training", None))
        self.btnAdvanced.setText(QCoreApplication.translate("MainWindow", u"Advanced Options...", None))
        self.btnTesting.setText(QCoreApplication.translate("MainWindow", u"Start Testing", None))
        self.btnSave_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.gbxResults.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.cbxType.setItemText(0, QCoreApplication.translate("MainWindow", u"LASSO", None))
        self.cbxType.setItemText(1, QCoreApplication.translate("MainWindow", u"RandomForest", None))
        self.cbxType.setItemText(2, QCoreApplication.translate("MainWindow", u"SVR", None))
        self.cbxType.setItemText(3, QCoreApplication.translate("MainWindow", u"SVR_OPT", None))

        self.cbxLog.setItemText(0, QCoreApplication.translate("MainWindow", u"Logpolar", None))
        self.cbxLog.setItemText(1, QCoreApplication.translate("MainWindow", u"Cartesian", None))
        self.cbxLog.setItemText(2, QCoreApplication.translate("MainWindow", u"Combined", None))

        self.cbxTT.setItemText(0, QCoreApplication.translate("MainWindow", u"Training Results", None))
        self.cbxTT.setItemText(1, QCoreApplication.translate("MainWindow", u"Testing Results", None))

        self.btnAssignCount.setText(QCoreApplication.translate("MainWindow", u"Assign Count", None))
        self.lblTrainingSamples.setText(QCoreApplication.translate("MainWindow", u"Training Samples:", None))
        self.lblTestingSamples.setText(QCoreApplication.translate("MainWindow", u"Testing Samples:", None))
        self.lblNameTest.setText(QCoreApplication.translate("MainWindow", u"Name of the test:", None))
        self.tabPotTray.setTabText(self.tabPotTray.indexOf(self.tabCounting), QCoreApplication.translate("MainWindow", u"Leaf counting", None))
        self.gbxPhenoData.setTitle(QCoreApplication.translate("MainWindow", u"Phenotyping Data", None))

        __sortingEnabled = self.wgtPhenoData.isSortingEnabled()
        self.wgtPhenoData.setSortingEnabled(False)
      #  ___qlistwidgetitem = self.wgtPhenoData.item(0)
       # ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"ProjectedLeafArea", None));
       # ___qlistwidgetitem1 = self.wgtPhenoData.item(1)
       # ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Diameter", None));
        #___qlistwidgetitem2 = self.wgtPhenoData.item(2)
        #___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Perimeter", None));
       # ___qlistwidgetitem3 = self.wgtPhenoData.item(3)
        #___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Stockiness", None));
        #___qlistwidgetitem4 = self.wgtPhenoData.item(4)
        #___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Compactness", None));
        #___qlistwidgetitem5 = self.wgtPhenoData.item(5)
        #___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Hue", None));
        #___qlistwidgetitem6 = self.wgtPhenoData.item(6)
        #___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Count", None));
        #___qlistwidgetitem7 = self.wgtPhenoData.item(7)
        #___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"RelativeRateChange", None));
        #___qlistwidgetitem8 = self.wgtPhenoData.item(8)
        #___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"AbsoluteGrowthRate", None));
        #___qlistwidgetitem9 = self.wgtPhenoData.item(9)
        #___qlistwidgetitem9.setText(QCoreApplication.translate("MainWindow", u"RelativeGrowthRate", None));
        self.wgtPhenoData.setSortingEnabled(__sortingEnabled)


        self.cbxCm.setText(QCoreApplication.translate("MainWindow", u"Convert values to cm", None))
        self.btnLoadDE.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.gbxPlotParams.setTitle(QCoreApplication.translate("MainWindow", u"Plot Patameters", None))
        self.lblFrom.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.lblTo.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.lblShow.setText(QCoreApplication.translate("MainWindow", u"Show:", None))
        self.lblSpecify.setText(QCoreApplication.translate("MainWindow", u"Specify:", None))
        self.btnSaveDE.setText(QCoreApplication.translate("MainWindow", u"Save Plot As...", None))
        self.btnExportDE.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.gbxMatPlot.setTitle(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.tabPotTray.setTabText(self.tabPotTray.indexOf(self.tabDataExtraction), QCoreApplication.translate("MainWindow", u"Data Extraction", None))
    # retranslateUi

    def on_Choice(self):
        select = self.wgtPhenoData.currentItem().text()
        plot_graph(self, select)

    def save_plot(self):
        w = QWidget()
        path = (QFileDialog.getSaveFileName(w, 'Save as', "", '*.png'))
        print(path[0])
        self.MplWidget.canvas.figure.savefig(path[0])
        self.MplWidget



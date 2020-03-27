from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class LC_Tab():
    def __init__(self,tab):
        self.tabsystem = tab
        self.tabCounting = QWidget()
        self.tabCounting.setObjectName(u"tabCounting")

        ## Plant List Group Box
        self.lc_gbxPlantList = QGroupBox(self.tabCounting)
        self.lc_gbxPlantList.setObjectName(u"lc_gbxPlantList")
        self.lc_gbxPlantList.setGeometry(QRect(10, 20, 251, 671))

        ## Sequence drop down menu setup
        self.lc_cmbSequence = QComboBox(self.lc_gbxPlantList)
        self.lc_cmbSequence.addItem("")
        self.lc_cmbSequence.setObjectName(u"lc_cmbSequence")
        self.lc_cmbSequence.setGeometry(QRect(100, 30, 91, 31))

        ## Sequence Label
        self.lc_lblSequ = QLabel(self.lc_gbxPlantList)
        self.lc_lblSequ.setObjectName(u"lc_lblSequ")
        self.lc_lblSequ.setGeometry(QRect(30, 30, 71, 21))
        self.lc_lblSequ.setAutoFillBackground(False)
        self.lc_lblSequ.setStyleSheet(u"background-color: none")

        ## Plant List list setup
        self.lc_listWidget = QListWidget(self.lc_gbxPlantList)
        self.lc_listWidget.setObjectName(u"lc_listWidget")
        self.lc_listWidget.setGeometry(QRect(10, 70, 231, 391))

        ## Load Button Setup
        self.lc_btnLoad = QPushButton(self.lc_gbxPlantList)
        self.lc_btnLoad.setObjectName(u"lc_btnLoad")
        self.lc_btnLoad.setGeometry(QRect(10, 570, 231, 41))

        ## Import Button setup
        self.lc_import = QPushButton(self.lc_gbxPlantList)
        self.lc_import.setObjectName(u"lc_import")
        self.lc_import.setGeometry(QRect(10, 620, 151, 41))

        ## Total number of plans Label
        self.lc_lblTotalNumPlants = QLabel(self.lc_gbxPlantList)
        self.lc_lblTotalNumPlants.setObjectName(u"lc_lblTotalNumPlants")
        self.lc_lblTotalNumPlants.setGeometry(QRect(30, 480, 141, 16))

        ## Training Set Size label
        self.lc_lblTrainingSetSize = QLabel(self.lc_gbxPlantList)
        self.lc_lblTrainingSetSize.setObjectName(u"lc_lblTrainingSetSize")
        self.lc_lblTrainingSetSize.setGeometry(QRect(30, 510, 111, 16))
        self.lc_lblTestingSetSize = QLabel(self.lc_gbxPlantList)
        self.lc_lblTestingSetSize.setObjectName(u"lc_lblTestingSetSize")
        self.lc_lblTestingSetSize.setGeometry(QRect(30, 540, 101, 16))

        ## Total Number Label
        self.lc_lblTotalNumber = QLabel(self.lc_gbxPlantList)
        self.lc_lblTotalNumber.setObjectName(u"lc_lblTotalNumber")
        self.lc_lblTotalNumber.setGeometry(QRect(180, 480, 41, 16))
        self.lc_lblTrainingSizeNumber = QLabel(self.lc_gbxPlantList)
        self.lc_lblTrainingSizeNumber.setObjectName(u"lc_lblTrainingSizeNumber")
        self.lc_lblTrainingSizeNumber.setGeometry(QRect(180, 510, 41, 16))

        ## Testing Number Label
        self.lc_lblTestingNumber = QLabel(self.lc_gbxPlantList)
        self.lc_lblTestingNumber.setObjectName(u"lc_lblTestingNumber")
        self.lc_lblTestingNumber.setGeometry(QRect(180, 540, 41, 16))

        ## Training/Testing Group Box
        self.lc_gbx_tt = QGroupBox(self.tabCounting)
        self.lc_gbx_tt.setObjectName(u"lc_gbx_tt")
        self.lc_gbx_tt.setGeometry(QRect(270, 20, 741, 671))

        ## Training drop down menu setup
        self.lc_cbxTraining = QComboBox(self.lc_gbx_tt)
        self.lc_cbxTraining.addItem("")
        self.lc_cbxTraining.addItem("")
        self.lc_cbxTraining.setObjectName(u"lc_cbxTraining")
        self.lc_cbxTraining.setGeometry(QRect(280, 20, 271, 41))

        ## Testing drop down menu setup
        self.lc_cbxTesting = QComboBox(self.lc_gbx_tt)
        self.lc_cbxTesting.addItem("")
        self.lc_cbxTesting.addItem("")
        self.lc_cbxTesting.addItem("")
        self.lc_cbxTesting.addItem("")
        self.lc_cbxTesting.setObjectName(u"lc_cbxTesting")
        self.lc_cbxTesting.setGeometry(QRect(280, 70, 271, 41))

        ## Name of the Test setup (editable line ?)
        self.lc__tbName = QLineEdit(self.lc_gbx_tt)
        self.lc__tbName.setObjectName(u"lc__tbName")
        self.lc__tbName.setEnabled(False)
        self.lc__tbName.setGeometry(QRect(280, 120, 271, 31))

        ## Progress bar inside T/T box
        self.lc_progressBar = QProgressBar(self.lc_gbx_tt)
        self.lc_progressBar.setObjectName(u"lc_progressBar")
        self.lc_progressBar.setGeometry(QRect(60, 180, 611, 23))
        self.lc_progressBar.setValue(0)
        self.lc_progressBar.setTextVisible(False)

        ## Training Button
        self.lc_btnTraining = QPushButton(self.lc_gbx_tt)
        self.lc_btnTraining.setObjectName(u"lc_btnTraining")
        self.lc_btnTraining.setGeometry(QRect(90, 240, 261, 41))
        self.lc_btnTraining.setStyleSheet(u"")

        ## Advanced Button
        self.lc_btnAdvanced = QPushButton(self.lc_gbx_tt)
        self.lc_btnAdvanced.setObjectName(u"lc_btnAdvanced")
        self.lc_btnAdvanced.setGeometry(QRect(360, 240, 261, 41))
        self.lc_btnAdvanced.setStyleSheet(u"")

        ## Testing Button
        self.lc_btnTesting = QPushButton(self.lc_gbx_tt)
        self.lc_btnTesting.setObjectName(u"lc_btnTesting")
        self.lc_btnTesting.setGeometry(QRect(90, 300, 261, 41))
        self.lc_btnTesting.setStyleSheet(u"")

        ## Save Button
        self.lc_btnSave = QPushButton(self.lc_gbx_tt)
        self.lc_btnSave.setObjectName(u"lc_btnSave")
        self.lc_btnSave.setGeometry(QRect(360, 300, 261, 41))
        self.lc_btnSave.setStyleSheet(u"")

        ## Results Group Box inside T/T group box
        self.lc_gbxResults = QGroupBox(self.lc_gbx_tt)
        self.lc_gbxResults.setObjectName(u"lc_gbxResults")
        self.lc_gbxResults.setGeometry(QRect(10, 350, 721, 311))

        ## Type drop down menu
        self.lc_cbxType = QComboBox(self.lc_gbxResults)
        self.lc_cbxType.addItem("")
        self.lc_cbxType.addItem("")
        self.lc_cbxType.addItem("")
        self.lc_cbxType.addItem("")
        self.lc_cbxType.setObjectName(u"lc_cbxType")
        self.lc_cbxType.setGeometry(QRect(80, 220, 261, 31))

        ## Log drop down menu
        self.lc_cbxLog = QComboBox(self.lc_gbxResults)
        self.lc_cbxLog.addItem("")
        self.lc_cbxLog.addItem("")
        self.lc_cbxLog.addItem("")
        self.lc_cbxLog.setObjectName(u"lc_cbxLog")
        self.lc_cbxLog.setGeometry(QRect(370, 220, 261, 31))

        ## Training/ Testing drop down
        self.lc_cbxTT = QComboBox(self.lc_gbxResults)
        self.lc_cbxTT.addItem("")
        self.lc_cbxTT.addItem("")
        self.lc_cbxTT.setObjectName(u"lc_cbxTT")
        self.lc_cbxTT.setGeometry(QRect(80, 260, 261, 31))

        ## View list
        self.lc_lstView = QListView(self.lc_gbxResults)
        self.lc_lstView.setObjectName(u"lc_lstView")
        self.lc_lstView.setGeometry(QRect(40, 30, 641, 81))
        self.lc_tblView = QTableView(self.lc_gbxResults)
        self.lc_tblView.setObjectName(u"lc_tblView")
        self.lc_tblView.setGeometry(QRect(40, 120, 641, 81))

        ## Assign Count button
        self.lc_btnAssignCount = QPushButton(self.lc_gbxResults)
        self.lc_btnAssignCount.setObjectName(u"lc_btnAssignCount")
        self.lc_btnAssignCount.setGeometry(QRect(370, 260, 261, 31))

        ## Training Samples lael
        self.lc_lblTrainingSamples = QLabel(self.lc_gbx_tt)
        self.lc_lblTrainingSamples.setObjectName(u"lc_lblTrainingSamples")
        self.lc_lblTrainingSamples.setGeometry(QRect(160, 30, 111, 16))

        ## Testing Samples label
        self.lc_lblTestingSamples = QLabel(self.lc_gbx_tt)
        self.lc_lblTestingSamples.setObjectName(u"lc_lblTestingSamples")
        self.lc_lblTestingSamples.setGeometry(QRect(160, 80, 111, 16))

        ##Test Name label
        self.lc_lblNameTest = QLabel(self.lc_gbx_tt)
        self.lc_lblNameTest.setObjectName(u"lc_lblNameTest")
        self.lc_lblNameTest.setGeometry(QRect(160, 130, 111, 16))


        tab.addTab(self.tabCounting, "")
        self.retranslate_UI()

    def retranslate_UI(self):
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
        self.tabsystem.setTabText(self.tabsystem.indexOf(self.tabCounting),
                                  QCoreApplication.translate("MainWindow", u"Leaf Counting", None))
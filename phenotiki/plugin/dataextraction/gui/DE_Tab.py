# seperate file to remove data extraction from main UI file.
from PySide2.QtCore import QRect, QCoreApplication

from phenotiki.plugin.dataextraction.gui.mplwidget import MplWidget
from phenotiki.plugin.dataextraction.src.DE_UIFunction import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *


class DE_Tab():
    def __init__(self, tab):

        self.DataFunct = DE_Functionality()
        self.tabsystem = tab
        self.tabsystem.setFont(QFont("Helvetica", 12))
        self.tabDataExtraction = QWidget()
        self.tabDataExtraction.setObjectName(u"tabDataExtraction")
        self.tabDataExtraction.setFont(QFont("Helvetica", 8))

        ## PhenoData QGroup Box setup
        self.de_gbxPhenoData = QGroupBox(self.tabDataExtraction)
        self.de_gbxPhenoData.setObjectName(u"de_gbxPhenoData")
        self.de_gbxPhenoData.setGeometry(QRect(10, 20, 251, 511))

        ## Phenodata Widget setup
        self.de_wgtPhenoData = QListWidget(self.de_gbxPhenoData)
        self.dataSelections = ["ProjectedLeafArea", "Diameter", "Perimeter", "Stockiness", "Compactness", "Hue",
                               "Count", "RelativeRateChange", "AbsoluteGrowthRate", "RelativeGrowthRate"]
        self.de_wgtPhenoData.addItems(self.dataSelections)
        self.de_wgtPhenoData.clicked.connect(self.on_Choice)
        self.de_wgtPhenoData.setObjectName(u"de_wgtPhenoData")
        self.de_wgtPhenoData.setEnabled(False)
        self.de_wgtPhenoData.setGeometry(QRect(10, 20, 231, 361))

        ## Cobvert Checkbox Setup
        self.de_cbxCm = QCheckBox(self.de_gbxPhenoData)
        self.de_cbxCm.setObjectName(u"de_cbxCm")
        self.de_cbxCm.setGeometry(QRect(40, 390, 151, 21))

        ## Load Button setup
        self.de_btnLoadDE = QPushButton(self.de_gbxPhenoData)
        self.de_btnLoadDE.setObjectName(u"de_btnLoadDE")
        self.de_btnLoadDE.setGeometry(QRect(60, 430, 121, 51))
        self.de_btnLoadDE.clicked.connect(self.load_Dataset)

        ## PlotParams Group Box setup
        self.de_gbxPlotParams = QGroupBox(self.tabDataExtraction)
        self.de_gbxPlotParams.setObjectName(u"de_gbxPlotParams")
        self.de_gbxPlotParams.setGeometry(QRect(10, 530, 1001, 171))

        # FROM drop down setup
        self.de_cbxFrom = QComboBox(self.de_gbxPlotParams)
        self.de_cbxFrom.setObjectName(u"de_cbxFrom")
        self.de_cbxFrom.addItem("N/A")
        self.de_cbxFrom.setGeometry(QRect(160, 50, 221, 31))
        self.de_cbxFrom.setEnabled(False)
        self.de_cbxFrom.activated[int].connect(self.update_from)

        ## To drop down setup
        self.de_cbxTo = QComboBox(self.de_gbxPlotParams)
        self.de_cbxTo.setObjectName(u"de_cbxTo")
        self.de_cbxTo.addItem("N/A")
        self.de_cbxTo.setGeometry(QRect(160, 120, 221, 31))
        self.de_cbxTo.setEnabled(False)
        self.de_cbxTo.activated[int].connect(self.update_to)

        ## Show drop down Setup
        self.de_cbxShow = QComboBox(self.de_gbxPlotParams)
        self.de_cbxShow.setObjectName(u"de_cbxShow")
        self.de_cbxShow.setGeometry(QRect(490, 50, 221, 31))
        self.de_cbxShow.addItem("All")
        self.de_cbxShow.setEnabled(False)
        self.de_cbxShow.activated[int].connect(self.update_show)

        ## Specify drop down setup
        self.de_cbxSpecify = QComboBox(self.de_gbxPlotParams)
        self.de_cbxSpecify.setObjectName(u"de_cbxSpecify")
        self.de_cbxSpecify.setGeometry(QRect(490, 120, 221, 31))
        self.de_cbxSpecify.addItem("N/A")
        self.de_cbxSpecify.setEnabled(False)
        self.de_cbxSpecify.activated[int].connect(self.update_select)

        ## Fron label
        self.de_lblFrom = QLabel(self.de_gbxPlotParams)
        self.de_lblFrom.setObjectName(u"de_lblFrom")
        self.de_lblFrom.setGeometry(QRect(100, 60, 55, 16))
        font2 = QFont()
        font2.setPointSize(12)
        self.de_lblFrom.setFont(font2)

        ## To label
        self.de_lblTo = QLabel(self.de_gbxPlotParams)
        self.de_lblTo.setObjectName(u"de_lblTo")
        self.de_lblTo.setGeometry(QRect(120, 130, 31, 16))
        self.de_lblTo.setFont(font2)

        ## Show Label
        self.de_lblShow = QLabel(self.de_gbxPlotParams)
        self.de_lblShow.setObjectName(u"de_lblShow")
        self.de_lblShow.setGeometry(QRect(420, 60, 55, 16))
        self.de_lblShow.setFont(font2)

        ## Specify Label
        self.de_lblSpecify = QLabel(self.de_gbxPlotParams)
        self.de_lblSpecify.setObjectName(u"de_lblSpecify")
        self.de_lblSpecify.setGeometry(QRect(410, 120, 81, 31))
        self.de_lblSpecify.setFont(font2)

        ## Save button setup in Plot Parameters
        self.de_btnSaveDE = QPushButton(self.de_gbxPlotParams)
        self.de_btnSaveDE.setObjectName(u"de_btnSaveDE")
        self.de_btnSaveDE.setGeometry(QRect(830, 30, 131, 51))
        self.de_btnSaveDE.setEnabled(False)
        self.de_btnSaveDE.clicked.connect(self.save_plot)

        ## Export Button Setup
        self.de_btnExportDE = QPushButton(self.de_gbxPlotParams)
        self.de_btnExportDE.setObjectName(u"de_btnExportDE")
        self.de_btnExportDE.setGeometry(QRect(830, 100, 131, 51))
        self.de_btnExportDE.setEnabled(False)
 UIDevelopment

        ## MatPlot Group Box

        self.de_btnExportDE.clicked.connect(self.save_data)
 master
        self.de_gbxMatPlot = QGroupBox(self.tabDataExtraction)
        self.de_gbxMatPlot.setObjectName(u"de_gbxMatPlot")
        self.de_gbxMatPlot.setGeometry(QRect(270, 20, 741, 511))

        ## MatPlot Widget
        self.de_MplWidget = MplWidget(self.de_gbxMatPlot)
        self.de_MplWidget.setObjectName(u"de_MplWidget")
        self.de_MplWidget.setGeometry(QRect(10, 20, 721, 481))


        tab.addTab(self.tabDataExtraction, "")
        self.de_gbxMatPlot.raise_()
        self.de_gbxPhenoData.raise_()
        self.de_gbxPlotParams.raise_()
        self.retranslate_UI()

    def retranslate_UI(self):
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
        self.tabsystem.setTabText(self.tabsystem.indexOf(self.tabDataExtraction),
                                  QCoreApplication.translate("MainWindow", u"Data Extraction", None))

    def load_Dataset(self):
        self.DataFunct.loadDataset(self)

    def on_Choice(self):
        select = self.de_wgtPhenoData.currentItem().text()
        self.DataFunct.plot_graph(self, select)

    def save_plot(self):
        w = QWidget()
        path = (QFileDialog.getSaveFileName(w, 'Save as', "", '*png'))
        if path[0] != "":
            self.de_MplWidget.canvas.figure.savefig(path[0])
        else:
            self.show_errormsg()

    def update_from(self, index):
        self.DataFunct.UpdateFrom(self, index)

    def update_to(self, index):
        self.DataFunct.UpdateTo(self, index)

    def update_show(self, index):
        self.DataFunct.UpdateShow(self, index)

    def update_select(self, index):
        self.DataFunct.UpdateSpecify(self, index)

    def save_data(self):
        w = QWidget()
        path = (QFileDialog.getSaveFileName(w, 'Save as', "", '*.csv'))
        if path[0] != "":
            self.DataFunct.to_csv(path[0])
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText("New document saved at " + path[0])
            msgBox.setWindowTitle("Document saved")
            msgBox.setStandardButtons(QMessageBox.Ok)

            msgBox.exec()
        else:
            self.show_errormsg()

    def show_errormsg(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("document could not be saved")
        msgBox.setWindowTitle("Error")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()
import skimage
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from phenotiki.main.src.import_functionality import print_image_files
from phenotiki.plugin.counting.gui.ProgressBar import ProgressBar
from phenotiki.plugin.tray.gui.mplwidget import MplWidget
from phenotiki.plugin.tray.src.pt_src import *


class PT_Tab():
    def __init__(self, tab):

        ## Tab setup
        self.img_plots_array = []
        self.img_file_list_array = []
        self.tabsystem = tab
        self.tabsystem.setFont(QFont("Helvetica", 12))
        self.tabPotTrayAnalysis = QWidget()
        self.tabPotTrayAnalysis.setObjectName(u"tabPotTrayAnalysis")
        self.tabPotTrayAnalysis.setFont(QFont("Helvetica", 8))

        ## File list group box Setup
        self.pt_gbxFileList = QGroupBox(self.tabPotTrayAnalysis)
        self.pt_gbxFileList.setObjectName(u"pt_gbxFileList")
        self.pt_gbxFileList.setGeometry(QRect(10, 20, 251, 671))

        ##Load button in File list setup
        self.pt_btnLoad = QPushButton(self.pt_gbxFileList)
        self.pt_btnLoad.setObjectName(u"pt_btnLoad")
        self.pt_btnLoad.setGeometry(QRect(10, 560, 231, 41))

        ## Import Button in file list setup
        self.pt_btnImport = QPushButton(self.pt_gbxFileList)
        self.pt_btnImport.setObjectName(u"pt_btnImport")
        self.pt_btnImport.setGeometry(QRect(10, 610, 231, 41))
        ## Connects to on click function
        self.pt_btnImport.clicked.connect(self.on_import_click)

        ## Sets File list inside File list group box
        self.pt_lstFileList = QListWidget(self.pt_gbxFileList)
        self.pt_lstFileList.setObjectName(u"pt_lstFileList")
        self.pt_lstFileList.setGeometry(QRect(10, 20, 231, 521))
        self.pt_lstFileList.clicked.connect(self.on_treeView_clicked)

        ## Image group box setup
        self.pt_gbxImage = QGroupBox(self.tabPotTrayAnalysis)
        self.pt_gbxImage.setObjectName(u"pt_gbxImage")
        self.pt_gbxImage.setGeometry(QRect(270, 20, 741, 521))

        ## MatPlot Widget
        self.pt_MplWidget = MplWidget(self.pt_gbxImage)
        self.pt_MplWidget.setObjectName(u"pt_MplWidget")
        self.pt_MplWidget.setGeometry(QRect(2, 40, 537, 378))

        ##Active image inside Image group box setup
        # self.pt_lblViewImage = QLabel(self.pt_gbxImage)
        # self.pt_lblViewImage.setObjectName(u"pt_lblViewImage")
        # self.pt_lblViewImage.setCursor(QCursor(Qt.CrossCursor))
        # self.pt_lblViewImage.mousePressEvent = self.getPos
        # self.pt_lblViewImage.setPixmap(QPixmap(u"../gui/img/holder.jpg"))
        # self.pt_lblViewImage.setGeometry(QRect(2, 40, 537, 378))
        # self.pt_lblViewImage.setScaledContents(True)

        ## Slider in Image group box setup
        self.pt_horizontalSlider = QSlider(self.pt_gbxImage)
        self.pt_horizontalSlider.setObjectName(u"pt_horizontalSlider")
        self.pt_horizontalSlider.setGeometry(QRect(90, 470, 321, 31))
        self.pt_horizontalSlider.setOrientation(Qt.Horizontal)
        self.pt_horizontalSlider.valueChanged[int].connect(self.slider_selected)
        self.pt_horizontalSlider.setSingleStep(1)
        self.pt_horizontalSlider.setEnabled(False)
        self.pt_horizontalSlider.setMinimum(0)


        ## Type drop down menu setup in image group box
        self.pt_cmbType = QComboBox(self.pt_gbxImage)
        self.pt_cmbType.addItem("")
        self.pt_cmbType.addItem("")
        self.pt_cmbType.addItem("")
        self.pt_cmbType.addItem("")
        self.pt_cmbType.setObjectName(u"pt_cmbType")
        self.pt_cmbType.setEnabled(False)
        self.pt_cmbType.setGeometry(QRect(590, 470, 121, 31))
        self.pt_cmbType.setFrame(True)

        ## Plots widget setup in Image Qbox
        self.pt_lstPlots = QListWidget(self.pt_gbxImage)
        self.pt_lstPlots.setObjectName(u"pt_lstPlots")
        self.pt_lstPlots.setGeometry(QRect(540, 30, 191, 431))

        ## Toolbox Qbox setup
        self.pt_gbxToolbox = QGroupBox(self.tabPotTrayAnalysis)
        self.pt_gbxToolbox.setObjectName(u"pt_gbxToolbox")
        self.pt_gbxToolbox.setGeometry(QRect(270, 550, 741, 141))

        ## Progress bar in Toolbox setup
        self.pt_progressBar = QProgressBar(self.pt_gbxToolbox)
        self.pt_progressBar.setObjectName(u"pt_progressBar")
        self.pt_progressBar.setGeometry(QRect(20, 60, 431, 31))
        self.pt_progressBar.setValue(0)
        self.pt_progressBar.setRange(0, 100)
        self.pt_progressBar.setTextVisible(False)

        ## Settings Button
        self.pt_btnSettings = QPushButton(self.pt_gbxToolbox)
        self.pt_btnSettings.setObjectName(u"pt_btnSettings")
        self.pt_btnSettings.setEnabled(False)
        self.pt_btnSettings.setGeometry(QRect(480, 20, 121, 51))

        ## Mask Button
        self.pt_btnMask = QPushButton(self.pt_gbxToolbox)
        self.pt_btnMask.setObjectName(u"pt_btnMask")
        self.pt_btnMask.setEnabled(False)
        self.pt_btnMask.setGeometry(QRect(610, 20, 121, 51))
        self.pt_btnMask.clicked.connect(self.on_mask_click)

        ##Task Button
        self.pt_btnTraits = QPushButton(self.pt_gbxToolbox)
        self.pt_btnTraits.setObjectName(u"pt_btnTraits")
        self.pt_btnTraits.setEnabled(False)
        self.pt_btnTraits.setGeometry(QRect(480, 80, 121, 51))

        ## Save Button
        self.pt_btnSave = QPushButton(self.pt_gbxToolbox)
        self.pt_btnSave.setObjectName(u"pt_btnSave")
        self.pt_btnSave.setEnabled(False)
        self.pt_btnSave.setGeometry(QRect(610, 80, 121, 51))

        ##Progress bar
       # self.pt_progressBar = ProgressBar()
        #self.pt_progressBar.hide()


        self.pt_cmbType.setCurrentIndex(0)

        tab.addTab(self.tabPotTrayAnalysis, "")
        self.retranslate_UI()

    ## Naming things
    def retranslate_UI(self):
        self.pt_gbxFileList.setTitle(QCoreApplication.translate("MainWindow", u"File List", None))
        self.pt_btnLoad.setText(QCoreApplication.translate("MainWindow", u"Load Dataset", None))
        self.pt_btnImport.setText(QCoreApplication.translate("MainWindow", u"Import", None))
        self.pt_gbxImage.setTitle(QCoreApplication.translate("MainWindow", u"Image", None))
        self.pt_cmbType.setItemText(0, QCoreApplication.translate("MainWindow", u"Raw Image", None))
        self.pt_cmbType.setItemText(1, QCoreApplication.translate("MainWindow", u"Detected Plants", None))
        self.pt_cmbType.setItemText(2, QCoreApplication.translate("MainWindow", u"Contour", None))
        self.pt_cmbType.setItemText(3, QCoreApplication.translate("MainWindow", u"FG Mask", None))
        self.pt_cmbType.setCurrentText(QCoreApplication.translate("MainWindow", u"Raw Image", None))

        # self.pt_lblViewImage.setText("")
        self.pt_gbxToolbox.setTitle(QCoreApplication.translate("MainWindow", u"Toolbox", None))
        self.pt_btnSettings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.pt_btnMask.setText(QCoreApplication.translate("MainWindow", u"Extract Mask", None))
        self.pt_btnTraits.setText(QCoreApplication.translate("MainWindow", u"Get Traits", None))
        self.pt_btnSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.tabsystem.setTabText(self.tabsystem.indexOf(self.tabPotTrayAnalysis),
                                  QCoreApplication.translate("MainWindow", u"Pot Tray Analysis", None))

    def build_pos_array(self, array):
        array.append(array)
        self.pt_lstPlots.clear()
        self.pt_lstPlots.addItems(array)

    ##Gets coordinates of a click within Image and puts them inside image plots array
    # def getPos(self, event):
    #     x = event.pos().x()
    #     y = event.pos().y()
    #     self.build_pos_array(self.img_plots_array, x, y)

    ## Function performed when import button is clicked
    def on_import_click(self):
        self.img_file_list_array.clear()
        for i in print_image_files(self):
            self.img_file_list_array.append(i)
        self.pt_lstFileList.clear()
        self.pt_lstFileList.addItems(self.img_file_list_array)
        self.pt_btnMask.setEnabled(True)
        self.pt_btnSave.setEnabled(True)
        self.pt_btnSettings.setEnabled(True)
        self.pt_btnTraits.setEnabled(True)
        self.pt_cmbType.setEnabled(True)

        if len(self.img_file_list_array) > 0:
            img = plt.imread(self.img_file_list_array[0])
            self.pt_MplWidget.canvas.axes.clear()
            self.pt_MplWidget.canvas.axes.imshow(img)
            self.pt_MplWidget.canvas.axes.set_axis_off()
            self.pt_MplWidget.canvas.draw()
            self.pt_horizontalSlider.setMaximum(len(self.img_file_list_array)-1)
            self.pt_horizontalSlider.setEnabled(True)
#            points = self.pt_MplWidget.canvas.figure.ginput(n=24)
#            self.build_pos_array(points)



    # Function performed when treeview button is clicked
    def on_treeView_clicked(self):
                i = self.pt_lstFileList.currentRow()
                #print(self.img_file_list_array.index(i))
                print(i)
                updateImage(self, i)


    def on_mask_click(self):
        for i in self.img_file_list_array:
            print("Image: " + str(i))
            log(self, i)
        self.pt_MplWidget.canvas.draw()

    def slider_selected(self, index):
        updateImage(self, index)
import random
import numpy as np
from PySide2.QtWidgets import QWidget, QFileDialog
import datetime
from phenotiki.main.gui.mplwidget import MplWidget
from phenotiki.plugin.dataextraction.src.dataex import *
from matplotlib import dates

fileOpened = False
matdata = {}
selection = ""
times = []
x_values = []
y_values = []
fr = 0
to = 0

def update_graph(self):
    fs = 500
    f = random.randint(1, 100)
    ts = 1 / fs
    length_of_signal = 100
    t = np.linspace(0, 1, length_of_signal)

    cosinus_signal = np.cos(2 * np.pi * f * t)
    sinus_signal = np.sin(2 * np.pi * f * t)

    self.MplWidget.canvas.axes.clear()
    self.MplWidget.canvas.axes.plot(t, cosinus_signal)
    self.MplWidget.canvas.axes.plot(t, sinus_signal)
    self.MplWidget.canvas.axes.legend(('cosinus', 'sinus'), loc='upper right')
    self.MplWidget.canvas.axes.set_title('Cosinus - Sinus Signal')
    self.MplWidget.canvas.draw()


def loadDataset(self):
    global fileOpened, matdata, x_values, to, uiRef
    w = QWidget()
    fname = QFileDialog.getOpenFileName(w, "Open File", "C:", ("MATLAB files (*mat)"))
    fname = fname[0]
    try:
        matdata = open_mat_file(fname)
        fileOpened = True
    except:
        print("invalid path")

    timestamps = matdata['Timestamp']
    for i in timestamps:
        time = datetime.datetime.fromtimestamp(i)
        x_values.append(time)
        if len(times) <= len(timestamps):
            times.append(time.strftime("%d-%b-%Y %H:%m:%S"))

    to = len(times)
    print(fname)

def openFileDialog(self):
    w = QWidget()
    path = str(QFileDialog.getExistingDirectory(w,  "Select Directory"))
    return path

def plot_graph(self, select):
    global selection, times, x_values, y_values, fr, to
    selection = select
    if fileOpened:
        ys = matdata['Subject']
#        x_values = []
        y_values = []
        std_values = []
        maxstd_values = []
        minstd_values = []

        for i in ys:
            sub = i
            try:
                y_values.append(np.mean(sub[selection]))
            except:
                y_values.append(None)

            try:
                std_values.append(np.std(sub[selection]))
            except:
                std_values.append(0.0)

        try:
            maxstd_values = np.add(std_values, y_values)
            minstd_values = np.subtract(y_values, std_values)
        except:
            count = 0
            for i in y_values:
                if i == None:
                    maxstd_values.append(float(0) + float(std_values[count]))
                    minstd_values.append(float(0) - float(std_values[count]))
                else:
                    maxstd_values.append(float(i) + float(std_values[count]))
                    minstd_values.append(float(i) - float(std_values[count]))
                count+= 1

       # print(timestamps)
        formatter = dates.DateFormatter("%d/%b")
        print(x_values)
     #   x = x_values.
        self.de_MplWidget.canvas.axes.clear()
        self.de_MplWidget.canvas.axes.xaxis.set_major_formatter(formatter)
        self.de_MplWidget.canvas.figure.autofmt_xdate()
        #I think maybe this should be zoomed in instead of changed, didn't realise earlier
        self.de_MplWidget.canvas.axes.plot(x_values[fr:to], y_values[fr:to])
        self.de_MplWidget.canvas.axes.fill_between(x_values[fr:to], minstd_values[fr:to], maxstd_values[fr:to], alpha=0.2)
        self.de_MplWidget.canvas.axes.set_title(selection)
        self.de_MplWidget.canvas.draw()
      #  self.de_MplWidget.canvas.figure.autofmt_xdate()

        if not self.de_cbxFrom.isEnabled():
            setupPlotParams(self)


def getDataset(self):
    return matdata


def setupPlotParams(self):
    self.de_cbxFrom.clear()
    self.de_cbxTo.clear()
    self.de_cbxFrom.addItems(times)
    self.de_cbxTo.addItems(times)
    self.de_cbxTo.setCurrentIndex(self.de_cbxTo.count()-1)
    self.de_cbxFrom.setEnabled(True)
    self.de_cbxTo.setEnabled(True)
    self.de_btnSaveDE.setEnabled(True)
    self.de_btnExportDE.setEnabled(True)

    #Setup show and specify butons
    self.de_cbxShow.addItems(["Specific Group", "Specific Subject"])
    self.de_cbxShow.setEnabled(True)


def UpdateFrom(self, index):
    global fr
    fr = index
    plot_graph(self, selection)

def UpdateTo(self, index):
    global to
    to = index
    plot_graph(self, selection)
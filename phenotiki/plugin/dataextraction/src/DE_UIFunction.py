import numpy as np
from PySide2.QtWidgets import QWidget, QFileDialog
import datetime
from phenotiki.main.gui.mplwidget import MplWidget
from pymatreader import read_mat
from matplotlib import dates


# class holds the dataset after it has been loaded from file and other values,
# to plot the data (x_values, and y_values.
class DE_Functionality():
    def __init__(self):
        self.fileOpened = False
        self.matdata = {}
        self.selection = ""
        self.times = []
        self.x_values = []
        self.y_values = []
        self.fr = 0
        self.to = 0
        self.bySubject = False
        self.byGroup = False
        self.groups = []
        self.subjectNum = 0

    # Opens a file dialog so that a mmatlabfile can be opened and stored.
    def loadDataset(self, widget):
        w = QWidget()
        fname = QFileDialog.getOpenFileName(w, "Open File", "C:", ("MATLAB files (*mat)"))
        fname = fname[0]
        try:
            self.matdata = self.open_mat_file(fname)
            self.fileOpened = True

            widget.de_wgtPhenoData.setEnabled(True)
            # stores all time values for x axis and from and to choice buttons
            timestamps = self.matdata['Timestamp']
            for i in timestamps:
                time = datetime.datetime.fromtimestamp(i)
                self.x_values.append(time)
                # save times as string for choice buttons
                if len(self.times) <= len(timestamps):
                    self.times.append(time.strftime("%d-%b-%Y %H:%m:%S"))

            # set to, so that the latest time is selected
            self.to = len(self.times)

        except:
            print("invalid path")

    # opens file dialog to select a directory
    def openFileDialog(self):
        w = QWidget()
        path = str(QFileDialog.getExistingDirectory(w, "Select Directory"))
        return path

    # for plotting and updating the graph based on selection
    def plot_graph(self, widget, select):
        self.selection = select

        # If file has been opened go ahead with plotting and getting the data for the graph
        if self.fileOpened:
            ys = self.matdata['Subject']
            # set y values back to empty to reflect potential change in selection
            self.y_values = []
            std_values = []
            maxstd_values = []
            minstd_values = []

            # For all instances in subject
            # Subject instance holds a dictionary
            for i in ys:
                sub = i
                # append the mean of selected data held in subject to y values
                # If this is none or another N/A type append none instead
                if not self.bySubject and not self.byGroup:
                    try:
                        self.y_values.append(np.mean(sub[self.selection]))
                    except:
                        self.y_values.append(None)

                    # append the std of selected data held in subject to y values
                    # This will be used to show range filling on the graph later
                    # If this is none or another N/A type append 0 instead
                    try:
                        std_values.append(np.std(sub[self.selection]))
                    except:
                        std_values.append(0.0)


                elif self.bySubject:
                    select = sub[self.selection]
                    self.y_values.append(select[self.subjectNum])


            if not self.bySubject and not self.byGroup:
                # get positive and negative std by adding and substracting std from y values
                try:
                    maxstd_values = np.add(std_values, self.y_values)
                    minstd_values = np.subtract(self.y_values, std_values)
                except:
                    count = 0
                    for i in self.y_values:
                        if i == None:
                            maxstd_values.append(float(0) + float(std_values[count]))
                            minstd_values.append(float(0) - float(std_values[count]))
                        else:
                            maxstd_values.append(float(i) + float(std_values[count]))
                            minstd_values.append(float(i) - float(std_values[count]))
                        count += 1
            # Sets format for time values
            formatter = dates.DateFormatter("%d/%b")
            # setup plot
            widget.de_MplWidget.canvas.axes.clear()
            widget.de_MplWidget.canvas.axes.xaxis.set_major_formatter(formatter)
            widget.de_MplWidget.canvas.figure.autofmt_xdate()
            # I think maybe this should be zoomed in instead of changed, didn't realise earlier
            widget.de_MplWidget.canvas.axes.plot(self.x_values[self.fr:self.to], self.y_values[self.fr:self.to])
            # Show range by using standart deviation
            if self.bySubject == False:
                widget.de_MplWidget.canvas.axes.fill_between(self.x_values[self.fr:self.to], minstd_values[self.fr:self.to], maxstd_values[self.fr:self.to], alpha=0.2)
            widget.de_MplWidget.canvas.axes.set_title(self.selection)
            widget.de_MplWidget.canvas.draw()

            # If from choice widget has not been enabled yet
            if not widget.de_cbxFrom.isEnabled():
                # set up choice widgets
                self.setupPlotParams(widget)

    # return dataset
    def getDataset(self):
        return self.matdata

    # setup choice widget contents
    def setupPlotParams(self, widget):
        widget.de_cbxFrom.clear()
        widget.de_cbxTo.clear()
        widget.de_cbxFrom.addItems(self.times)
        widget.de_cbxTo.addItems(self.times)
        widget.de_cbxTo.setCurrentIndex(widget.de_cbxTo.count() - 1)
        widget.de_cbxFrom.setEnabled(True)
        widget.de_cbxTo.setEnabled(True)
        widget.de_btnSaveDE.setEnabled(True)
        widget.de_btnExportDE.setEnabled(True)

        # Setup show button
        widget.de_cbxShow.addItems(["Specific Group", "Specific Subject"])
        widget.de_cbxShow.setEnabled(True)

    # update the from value
    def UpdateFrom(self, widget, index):
        self.fr = index
        self.plot_graph(widget, self.selection)

    # update the to value
    def UpdateTo(self, widget, index):
        self.to = index + 1
        self.plot_graph(widget, self.selection)

    # open matfile
    def open_mat_file(self, filename):
        data = read_mat(filename)
        data = data['ans']
        self.matdata = data['Sequences']

        return self.matdata

#called when show is changed, between all group or subject
    #
    def UpdateShow(self, widget, index):
        subjects = self.matdata['Subject']
        NumOfSub = 0
        valid = False
        for sub in subjects:
            if NumOfSub == 0:
                NumOfSub = len(sub['ID'])
            if len(sub['ID']) > NumOfSub or len(sub['ID']) < NumOfSub:
                print("subject number not equal")
        if index == 0:
            self.byGroup = False
            self.bySubject = False
        elif index == 1:
            for sub in subjects:
                if sub['Group'] != 0:
                    valid = True
            if valid:
                firstSub = subjects[0]
                self.groups = []
                for i in firstSub['Group']:
                    if i != None or i != "":
                        group = "Group " + str(i)
                        if not np.isin(self.groups, group):
                            self.groups.append(group)
                if not len(group) == 0:
                    self.byGroup = True
                    self.bySubject = False
                    widget.de_cbxSpecify.clear()
                    widget.de_cbxSpecify.setEnabled(True)
                    widget.de_cbxSpecify.addItems(self.groups)
        elif index == 2:
            self.byGroup = False
            self.bySubject = True
            widget.de_cbxSpecify.clear()
            widget.de_cbxSpecify.setEnabled(True)
            firstSub = subjects[0]
            subNum = []
            for i in firstSub['ID']:
                subNum.append("Subject " + str(i))
            widget.de_cbxSpecify.addItems(subNum)
            print(firstSub['ID'])

        self.plot_graph(widget, self.selection)

#   called when different dubject or group is selected
    #only works for subject at the moment
    def UpdateSpecify(self, widget, index):
        self.subjectNum = index
        self.plot_graph(widget, self.selection)
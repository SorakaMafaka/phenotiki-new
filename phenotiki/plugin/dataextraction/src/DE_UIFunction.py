#Author(s):
#   Converted from "Phenotiki - True phenotyping-in-a-box solution"
#   by Steven Dixon, Milena Bromm, Mateusz Glowacki
#   Original "Phenotiki - True phenotyping-in-a-box solution"
#   by M. Minervini and M.V. Giuffrida from IMT Advanced Studies of Lucca, S. Tsaftaris from University of Edinburgh
#
#
#   Version:   1.0
#   Date:      24/04/2020

import numpy as np
from PySide2.QtWidgets import QWidget, QFileDialog
import datetime
from pymatreader import read_mat
from matplotlib import dates
import csv
import json

# class holds the dataset after it has been loaded from file and other values,
# to plot the data (x_values, and y_values)
class DE_Functionality():
    def __init__(self):
        self.fileOpened = False #has data set been loaded
        self.matdata = {} # dataset
        self.selection = "" #part of data selected, such as Diameter of plant
        self.times = [] #full lenght string representation of timestamp
        self.x_values = [] #timestamp formatted for plot
        self.y_values = [] #plot y values
        self.fr = 0 #from which date the data should be shown
        self.to = 0 #y_values maximum index
        self.bySubject = False #Is data displayed by subject
        self.byGroup = False #Is data displayed by group
        self.groupsStr = [] #String representation of group
        self.subjectNum = 0 #Currently displayed subject, if by subject is true

    # Opens a file dialog so that a json file can be opened and stored.
    def loadDataset(self, widget):
        w = QWidget()
        fname = QFileDialog.getOpenFileName(w, "Open File", "C:", ("JSON files (*json)"))
        fname = fname[0]
        try:
            self.matdata = self.open_json_file(fname)
            self.fileOpened = True

            widget.de_wgtPhenoData.setEnabled(True)
            #store all time values for x axis and for from and to choice buttons
            timestamps = self.matdata['TimeStamp']
            self.times = timestamps
            self.x_values = []
            datevalues = [datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in self.times]

            #Formats datetime value into string for plot xaxis
            for x in datevalues:
                self.x_values.append(x.strftime("%d/%b %H:%M"))


            # set to, so that the latest time is selected
            self.to = len(self.times)
            widget.de_btnExportDE.setEnabled(True)

        except:
            print("invalid path")

    # opens file dialog to select a directory
    def openFileDialog(self):
        w = QWidget()
        path = str(QFileDialog.getExistingDirectory(w, "Select Directory"))
        return path

    # for plotting and updating the graph based on selection
    def plot_graph(self, widget, select):
        #get the selected type of data from ui
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
            for sub in ys:
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

                #If graph is displayed by subject, only append y values for selected subject number
                elif self.bySubject:
                    select = sub[self.selection]
                    self.y_values.append(select[self.subjectNum])

                elif self.byGroup:
                    # get the selected subject values
                    select = sub[self.selection]
                    groupvalues = []
                   #check for the group members and append values to group values
                    for item in sub['Group']:
                        #subjectnum = groupnumber
                        if item == self.subjectNum:
                            groupvalues.append(select[sub['Group'].index()])

                    #mean
                    try:
                        self.y_values.append(np.mean(groupvalues))
                    except:
                        self.y_values.append(None)
                    #std
                    try:
                        std_values.append(np.std(groupvalues))
                    except:
                        std_values.append(0.0)



            if not self.bySubject:
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

            # setup plot
            widget.de_MplWidget.canvas.axes.clear()

            widget.de_MplWidget.canvas.axes.plot(self.x_values[self.fr:self.to], self.y_values[self.fr:self.to])

            # Show range by using standart deviation
            if self.bySubject == False:
                widget.de_MplWidget.canvas.axes.fill_between(self.x_values[self.fr:self.to], minstd_values[self.fr:self.to], maxstd_values[self.fr:self.to], alpha=0.2)

            widget.de_MplWidget.canvas.axes.set_title(self.selection)
            widget.de_MplWidget.canvas.axes.grid(linestyle='-', linewidth=0.5, alpha=0.5);
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

        #enable choice wigets
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

    #open json
    def open_json_file(self, filename):

    #open json file
        with open(filename, "r") as read_file:
            # Converting JSON encoded data into Python dictionary
            data = json.load(read_file)

            #restucture file so, the structure is similar to the previously used matlab structure
            times = []
            Filename = []
            Subjects = []
            FGMask = []
            mdata = data['Sequences']
            for i in mdata:
                times.append(i['TimeStamp'])
                Filename.append(i['Filename'])
                Subjects.append(i['Subjects'][0])
                FGMask.append(i['FGMask'])

            #return dataset contents
            return {"Filename": Filename, "TimeStamp" : times, "Subject": Subjects, "FGMask": FGMask}



#called when show is changed, between all, by group or subject
    def UpdateShow(self, widget, index):
        subjects = self.matdata['Subject']
        NumOfSub = 0
        valid = False
        #check if subject num is equal for each set of data
        for sub in subjects:
            if NumOfSub == 0:
                NumOfSub = len(sub['ID'])
            if len(sub['ID']) > NumOfSub or len(sub['ID']) < NumOfSub:
                print("subject number not equal")

        # User selected display all
        if index == 0:
            self.byGroup = False
            self.bySubject = False

        #User selected by group displayed
        elif index == 1:
            for sub in subjects:
                for item in sub['Group']:
                    if item != []:
                        valid = True
            if valid:
                firstSub = subjects[0]
                self.groupsStr = []
                for i in firstSub['Group']:
                    if i is not None or i != "":
                        group = "Group " + str(i)
                        if not np.isin(self.groupsStr, group):
                            self.groupsStr.append(group)

                if not len(group) == 0:
                    self.byGroup = True
                    self.bySubject = False
                    widget.de_cbxSpecify.clear()
                    widget.de_cbxSpecify.setEnabled(True)
                    widget.de_cbxSpecify.addItems(self.groupsStr)

        #user selected by subject
        elif index == 2:
            self.byGroup = False
            self.bySubject = True
            widget.de_cbxSpecify.clear()
            widget.de_cbxSpecify.setEnabled(True)
            #get an the subject number min, in case that the subject num is not equal among all sets
            subjectmin = []
            for i in subjects:
                subjectmin.append(np.max(i['ID']))
            subjectmin = np.min(subjectmin)
            subNum = []
            for i in range(1, subjectmin):
                subNum.append("Subject " + str(i))
            #Add subject numbers to choice widget
            widget.de_cbxSpecify.addItems(subNum)

        self.plot_graph(widget, self.selection)

#   called when different subject or group is selected
    #only works for subject at the moment
    def UpdateSpecify(self, widget, index):
        self.subjectNum = index
        self.plot_graph(widget, self.selection)

    #function to write data to CSV
    def to_csv(self, path):
        subjects = self.matdata['Subject']
        selects = ["Date", "ID", "Group", "ProjectedLeafArea", "Diameter", "Perimeter", "Stockiness", "Compactness",
                   "Hue", "Count", "RelativeRateChange", "AbsoluteGrowthRate", "RelativeGrowthRate"]
        try:
            with open(path, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=selects)
                #writer header to csv
                writer.writeheader()
                index = 0
                data = ""
                #Add the data from all subjects
                while (index < len(subjects)):
                    sub = subjects[index]
                    i = 0
                    while (i < len(sub['ID'])):
                        data += str(self.times[index])
                        for key in selects:
                            if (key != "Date"):
                                row = sub[key]
                                if row:
                                    if row[i] != None:
                                        data += "," + str(row[i])
                                    else:
                                        data += ","
                                else:
                                    data += ","

                        data += "\n"
                        i += 1

                    index += 1
                csvfile.write(data)

        except IOError:
            print("I/O error")

import wx
from numpy import arange, sin, pi
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas, FigureCanvasWxAgg
from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure
from Plugin.Modules.DataExtraction.src.Functionality import *


class DataExtractionTab(wx.Panel):
    # We pass the main frame as the last parameter of the constructor
    def __init__(self, parent, mainFrame):
        wx.Panel.__init__(self, parent)
        self._mainFrame = mainFrame
        self.dataSelections = ["ProjectedLeafArea", "Diameter", "Perimeter", "Stockiness", "Compactness", "Hue", "Count", "RelativeRateChange", "AbsoluteGrowthRate", "RelativeGrowthRate"]
        self.btnLoadDataset = wx.Button(self, label="Load Dataset")
        self.choiceData = wx.Choice(self, choices=self.dataSelections)
        self.btnLoadDataset.Bind(wx.EVT_BUTTON, self.onFileOpen)
        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(self.btnLoadDataset, 1)
        self.sizer.Add(self.choiceData, 1)
        self.sizer.Add(self.canvas, 1)
        self.SetSizer(self.sizer)
        self.Fit()

    def draw(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2 * pi * t)
        self.axes.plot(t, s)

    def onFileOpen(self, event):
        dialog = wx.FileDialog(self, "Open", "", "", "CSV files (*.csv)|*.csv", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        dialog.ShowModal()
        path = dialog.GetPath()
        open_file(path)
import wx


class DataExtractionTab(wx.Panel):
    # We pass the main frame as the last parameter of the constructor
    def __init__(self, parent, mainFrame):
        wx.Panel.__init__(self, parent=parent)
        self._mainFrame = mainFrame
        headerText = wx.StaticText(self, label="Data Extraction", pos=(20,20))
        self.dataSelections = ["ProjectedLeafArea", "Diameter", "Perimeter", "Stockiness", "Compactness", "Hue", "Count", "RelativeRateChange", "AbsoluteGrowthRate", "RelativeGrowthRate"]
        self.btnLoadDataset = wx.Button(self, label="Load Dataset", pos=(20,150))
        self.choiceData = wx.Choice(self, pos=(20, 117), choices=self.dataSelections)
        self.btnLoadDataset.Bind(wx.EVT_BUTTON, self.onFileOpen)

    def onFileOpen(self, event):
        dialog = wx.FileDialog(self, "Open", "", "", "CSV files (*.csv)|*.csv", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        dialog.ShowModal()


import wx
from Plugin.Main.src import Functionality
from Plugin.Modules.Counting.UI.CountingUI import CountingTab
from Plugin.Modules.LeafAnnotation.UI.LeafAnnotationUI import LeafAnnotationTab
from Plugin.Modules.Tray.UI.TrayAnalysisUI import TrayTab
from Plugin.Modules.DataExtraction.UI.DataExtractionUI import DataExtractionTab


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Information", size=(1200, 700))
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # Add Modules
        self.mainTab = MainTab(nb, self)
        self.countingTab = CountingTab(nb, self)
        self.leafTab = LeafAnnotationTab(nb, self)
        self.trayTab = TrayTab(nb, self)
        self.dataExTab = DataExtractionTab(nb, self)

        # Add Module Tabs
        nb.AddPage(self.mainTab, "Main")
        nb.AddPage(self.countingTab, "Leaf Counting")
        nb.AddPage(self.leafTab, "Leaf Annotation")
        nb.AddPage(self.trayTab, "Tray Analysis")
        nb.AddPage(self.dataExTab, "Data Extraction")
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


class MainTab(wx.Panel):
    def __init__(self, parent, mainFrame):
        wx.Panel.__init__(self, parent=parent)
        self._mainFrame = mainFrame
        headerText = wx.StaticText(self, label="Main Page", pos=(20, 20))


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()

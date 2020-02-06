import wx

class TrayTab(wx.Panel):
    # We pass the main frame as the last parameter of the constructor
    def __init__(self, parent, mainFrame):
        wx.Panel.__init__(self, parent=parent)
        self._mainFrame = mainFrame
        headerText = wx.StaticText(self, label="Tray Analysis", pos=(20,20))

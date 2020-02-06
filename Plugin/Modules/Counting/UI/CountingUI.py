import wx


class CountingPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        headerText = wx.StaticText(self, label="Counting", pos=(20, 20))

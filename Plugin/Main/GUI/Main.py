import wx
from Plugin.Main.src import Functionality
from Plugin.Modules.Counting.UI.CountingUI import CountingPanel


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "Phenotiki")

        self.mainPanel = MainPanel(self)
        self.countingPanel = CountingPanel(self)
        self.countingPanel.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.mainPanel, 1, wx.EXPAND)
        self.sizer.Add(self.countingPanel, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        switch_panels_menu_item = fileMenu.Append(wx.ID_ANY,
                                                  "Counting Panel",
                                                  "Test text")
        self.Bind(wx.EVT_MENU, self.onSwitchPanels,
                  switch_panels_menu_item)
        menubar.Append(fileMenu, '&Modules')
        self.SetMenuBar(menubar)

    def onSwitchPanels(self, event):
        """"""
        if self.mainPanel.IsShown():
            self.SetTitle("Panel Two Showing")
            self.mainPanel.Hide()
            self.countingPanel.Show()
        else:
            self.SetTitle("Panel One Showing")
            self.mainPanel.Show()
            self.countingPanel.Hide()
        self.Layout()


class MainPanel(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self, parent=parent)
        self.countingPanel = CountingPanel(self)
        self.countingPanel.Hide()
        headerText = wx.StaticText(self, label="Phenotiki", pos=(20,20))


if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
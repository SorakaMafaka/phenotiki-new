import wx
import os, sys
from Plugin.Main.src import *


class PhenotikiApp(wx.App):
    def __init__(self):
        super().__init__(clearSigInt=True)

        self.initFrame()

    def initFrame(self):
        frame = MainFrame(parent=None, title="Phenotiki", pos = (200, 200))
        frame.Show()


class MainFrame(wx.Frame):
    def __init__(self, parent, title, pos):
        super().__init__(parent=parent, title=title, pos=pos)
        self.OnInit()

    def OnInit(self):
        panel = MainPanel(parent=self)


class MainPanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent=parent)

        headerText = wx.StaticText(self, id=wx.ID_ANY, label="Phenotiki", pos=(20, 20))


if __name__ == "__main__":
    app = PhenotikiApp()
    app.MainLoop()
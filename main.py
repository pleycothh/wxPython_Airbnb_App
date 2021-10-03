import wx
import matplotlib
import numpy as np


class LeftPanel (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent
        wx.Button(self, -1, "Button 1")

class RightPanel (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent
        wx.Button(self, -1, "Button 1")






class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None, title = "title", size = (600,600)) # from wx

        # split the window
        splitter = wx.SplitterWindow(self)
        left = LeftPanel(splitter) # need to create two panel
        right = RightPanel(splitter)
        splitter.SplitVertically(left,right)
        splitter.SetMinimumPaneSize(100)






if __name__ == "__main__":
    print("init")
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()
import wx
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class LeftPanel (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent
        wx.Button(self, -1, "Button lift")




class RightPanel (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent
        wx.Button(self, -1, "Button right")

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)
        self.axes.set_xlabel("Time")
        self.axes.set_ylabel("A/D")




    def draw(self):
        x = np.arange(0, 2, 0.01)
        y = np.sin(np.pi * x)
        self.axes.plot(x, y)





class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None, title = "title", size = (800,600)) # from wx

        # split the window
        splitter = wx.SplitterWindow(self)
        left = LeftPanel(splitter) # need to create two panel
        right = RightPanel(splitter)
        splitter.SplitVertically(left,right)
        splitter.SetMinimumPaneSize(200)

        right.draw()









if __name__ == "__main__":
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()
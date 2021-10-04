import wx
import wx.grid as grid
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class RightPanelTwo (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent, loadData):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent

       #wx.Button(self, -1, "Button right")

        self.data_summary = loadData

        ################################## table display ####################################
        def drawTable(self):
            summary = self.data_summary  # load the entire data
            print(summary.values)
            ####################################
            mygrid = grid.Grid(self)
            mygrid.CreateGrid(26, 9)

            sizer = wx.BoxSizer(wx.VERTICAL)
            sizer.Add(mygrid, 1, wx.EXPAND)
            self.SetSizer(sizer)

            self.canvas.draw()

        ####################################

        def changeSuber(self, newSuber):
            pass

        def changeDate(self, newDate):
            pass

        def changeKeyWord(self, newKey):
            pass
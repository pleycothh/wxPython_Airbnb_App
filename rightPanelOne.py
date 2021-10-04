import wx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np





class RightPanelOne (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent, loadData):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent

       #wx.Button(self, -1, "Button right")

        self.data_summary = loadData



    def drawMap(self):

        self.figure = Figure() # what does this do?
        self.axes = self.figure.add_subplot(111) # first row, column and graph
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL) # init the sizer with horizontal
        self.sizer.Add(self.canvas, 1, wx.ALL) # give sizer a size which is canvas
        self.SetSizer(self.sizer) # call the sizer

        self.axes.set_xlabel("Time")
        self.axes.set_ylabel("A/D")

        x = np.arange(0, 2, 0.01)
        y = np.sin(np.pi * x)
        self.axes.plot(x, y)
        print("draw")
        #self.canvas.draw() # update the draw

    def changeAxes(self, min, max): # data min and max value,
        self.axes.set_ylim(float(min), float(max))
        self.canvas.draw() # refresh the canvas
        # In this function, I recive two value from control panel
        # I use these two value redraw the canvas

import wx
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class LeftPanel (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent
        #wx.Button(self, -1, "Button lift")


# add toggle button
        self.togglebuttonStart = wx.ToggleButton(self, id=-1, label="Start", pos=(10,10))
        self.togglebuttonStart.Bind(wx.EVT_TOGGLEBUTTON, self.OnStartClick)

# add check box
        labelChannels = wx.StaticText(self, -1, "Input:", pos=(10, 200))
        self.cb1 = wx.CheckBox(self, -1, label="A0", pos=(10, 220))
        self.cb2 = wx.CheckBox(self, -1, label="A1", pos=(10, 240))
        self.Bind(wx.EVT_CHECKBOX, self.OnChecked) # bind the check box

# create time box
        self.textboxSampleTime = wx.TextCtrl(self, -1, "1000", pos=(10,300), size=(50,-1))# -1 means defult
        self.buttonSend = wx.Button(self, -1, "Send", pos=(70,300), size = (50,-1))
        self.buttonSend.Bind(wx.EVT_BUTTON, self.OnSend)

    def OnSend(self, event):
        value = self.textboxSampleTime.GetValue()
        print(value)

    def OnChecked(self, event):
        cb = event.GetEventObject()
        print("%s is clicked" % (cb.GetLabel()))

    def OnStartClick(self, event):
        value = self.togglebuttonStart.GetValue()
        if value:
            self.togglebuttonStart.SetLabel("Stop")
        else:
            self.togglebuttonStart.SetLabel("Start")





class RightPanel (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent
       #wx.Button(self, -1, "Button right")

        self.figure = Figure()
        self.axes = self.figure.add_subplot(111)
        self.canvas = FigureCanvas(self, -1, self.figure)

        self.sizer = wx.BoxSizer(wx.HORIZONTAL) # init the sizer with horizontal
        self.sizer.Add(self.canvas, 1, wx.ALL) # give sizer a size which is canvas
        self.SetSizer(self.sizer) # call the sizer

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
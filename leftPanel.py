import wx

class LeftPanel (wx.Panel): # class need inheritance of wx.Panel
    def __init__(self, parent, right, loadData):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent
        #wx.Button(self, -1, "Button lift")

        self.graph = right # this graph will have reference to figure panel
        self.data = loadData

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

        labelMinY = wx.StaticText(self, -1, "Min Y", pos = (10, 400))
        self.textboxMinYAxis = wx.TextCtrl(self, -1, "0", pos=(50, 400))
        labelMaxY = wx.StaticText(self, -1, "Max Y", pos=(10, 450))
        self.textboxMaxYAxis = wx.TextCtrl(self, -1, "1024", pos=(50, 450))

        self.buttonRange = wx.Button(self, -1, "Set Y Axis", pos= (10, 500))
        self.buttonRange.Bind(wx.EVT_BUTTON, self.SetButtonRange)

    def SetButtonRange(self, event):
        min = self.textboxMinYAxis.GetValue()
        max =  self.textboxMaxYAxis.GetValue()
        self.graph.changeAxes(min,max) # change the

        self.data.load()

        # a function in figure panel called change axes, this function can change the figure axes.
        # now, I call this function in control pannel because I create reference called graph.
        #once I call the changeAxes, I pass two value to this function. Then I let function do the rest

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

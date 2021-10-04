import wx

class LeftPanel (wx.Panel): # class need inheritance of wx.Panel
    def __init__(self, parent, rightOne, rightTwo, loadData):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent
        #wx.Button(self, -1, "Button lift")

        self.graphOne = rightOne
        self.graphTwo = rightTwo # this graph will have reference to figure panel
        self.data_summary = loadData


# add toggle button
        self.toggleDarkStart = wx.ToggleButton(self, id=-1, label = 'light',pos=(10,20)) # deleted label = 'Start' here
        self.toggleDarkStart.Bind(wx.EVT_TOGGLEBUTTON, self.OnDarkClick)

# add second toggle button
        self.toggleDrawStart = wx.ToggleButton(self, id=-1, label = 'Table',pos=(100,20)) # deleted label = 'Start' here
        self.toggleDrawStart.Bind(wx.EVT_TOGGLEBUTTON, self.OnMapClick)

# add check box
        labelChannels = wx.StaticText(self, -1, "Suber:", pos=(10, 110))
        self.cb1 = wx.CheckBox(self, -1, label="S0", pos=(10, 140)) # move down 30
        self.cb2 = wx.CheckBox(self, -1, label="S1", pos=(10, 160)) # move down 20
        self.Bind(wx.EVT_CHECKBOX, self.OnChecked) # bind the check box

# create time box
        self.textboxSampleTime = wx.TextCtrl(self, -1, "Enter Key words", pos=(10,60), size=(180,-1))# -1 means defult
        self.buttonSend = wx.Button(self, -1, "Search", pos=(200,60), size = (100,-1))
        self.buttonSend.Bind(wx.EVT_BUTTON, self.OnSend)

# range selection box
        labelMinY = wx.StaticText(self, -1, "Date start", pos = (10, 400))
        self.textboxMinYAxis = wx.TextCtrl(self, -1, "2010", pos=(100, 400))
        labelMaxY = wx.StaticText(self, -1, "Date ends", pos=(10, 430))
        self.textboxMaxYAxis = wx.TextCtrl(self, -1, "2020", pos=(100, 430))

# make search button an overall search key
        self.buttonRange = wx.Button(self, -1, "Search", pos= (50, 480), size = (300,50))
        self.buttonRange.Bind(wx.EVT_BUTTON, self.SetButtonRange)

    def SetButtonRange(self, event):
        min = self.textboxMinYAxis.GetValue()
        max =  self.textboxMaxYAxis.GetValue()

        summary = self.data_summary # load the entire data
        print(summary.name)


        self.graphOne.changeAxes(min,max) # change the figure



        # a function in figure panel called change axes, this function can change the figure axes.
        # now, I call this function in control pannel because I create reference called graph.
        #once I call the changeAxes, I pass two value to this function. Then I let function do the rest

    def OnSend(self, event):
        value = self.textboxSampleTime.GetValue()
        print(value)

    def OnChecked(self, event):
        cb = event.GetEventObject()
        print("%s is clicked" % (cb.GetLabel()))

    def OnDarkClick(self, event): # this function is swich light mode
        value = self.toggleDarkStart.GetValue()
        if value:
            self.toggleDarkStart.SetLabel("Dark")
        else:
            self.toggleDarkStart.SetLabel("Light")

    def OnMapClick(self, event): # this function is switch map view
        value = self.toggleDrawStart.GetValue()
        if value:
            self.toggleDrawStart.SetLabel("Map")
            self.graphOne.Hide()
            self.graphTwo.Show()
        else:
            self.toggleDrawStart.SetLabel("Table")
            #self.graphTwo.drawTable()
            self.graphOne.Show()
            self.graphTwo.Hide()

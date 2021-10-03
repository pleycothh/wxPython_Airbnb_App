# First things, first. Import the wxPython package.
import wx
import webbrowser
####################################### App #####################################################
class MyApp (wx.App) :
    def __init__(self):
        super().__init__(clearSigInt=True) #create an application object.

        # init frame
        # self.InitFrame() # run the function

        # init Frame
        frame = MyFrame(parent=None,title="My Frame", pos=(100,100))
        frame.Show()

###################################### Frame #####################################################
# subclass of wx.Window; Frame is a top level window
# A frame is a window whose size and position can (usually) be changed by the user.
# Usually represents the first/main window a user will see
class MyFrame (wx.Frame):
    def __init__(self,parent,title,pos):
        super().__init__(parent=parent,title=title,pos=pos)
        self.InitFrame()                   # run the OnInit function

    def InitFrame(self):
        self.panel = MyForm(parent=self)
        self.Fit()

######################################### Panel #####################################################
    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
class MyForm(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.InitForm()


    def InitForm(self):

        # title
        bmp = wx.ArtProvider.GetBitmap(id=wx.ART_INFORMATION,
                                       client=wx.ART_OTHER,
                                       size=(16,16))
        titleIco = wx.StaticBitmap(parent=self,id=wx.ID_ANY, bitmap=bmp)
        title = wx.StaticText(parent=self, id=wx.ID_ANY, label="my title")

        # input 1
        inputOneIco = wx.StaticBitmap(self,wx.ID_ANY,bmp)
        labelOne = wx.StaticText(self, wx.ID_ANY, 'Input 1')
        self.inputTxtOne = wx.TextCtrl(self, wx.ID_ANY, value = 'Text box') # text control is text box

        # input 2
        inputTwoIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelTwo = wx.StaticText ( self, wx.ID_ANY, 'Input 2')
        # wx.SpinCtrl  combines wx.TextCtrl and wx.SpinButton in One control.
        self.inputTwo = wx.SpinCtrl(self,wx.ID_ANY, value="0", min=0, max=100)

        # input 3
        inputThreeIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelThree = wx.StaticText(self, wx.ID_ANY, 'Input 3')
        self.inputThree = wx.Choice(self, choices=['A', 'B', 'C'])

        # input 4
        inputFourIco = wx.StaticBitmap(self, wx.ID_ANY, bmp)
        labelFour = wx.StaticText(self, wx.ID_ANY, 'Input 4')
        self.inputFour1 = wx.CheckBox(parent=self, label = "Choice 1")
        self.inputFour2 = wx.CheckBox(parent=self, label = "Choice 2")
        self.inputFour3 = wx.CheckBox(parent=self, label = "Choice 3")
        self.inputFour4 = wx.CheckBox(parent=self, label = "Choice 4")

        # submit
        okBtn = wx.Button(parent=self, id=wx.ID_ANY, label="OK")
        #okBtn.Bind(event=wx.EVT_BUTTON, handler=self.onOK)

        cancelBtn = wx.Button(parent=self, id=wx.ID_ANY, label="Cancel")


        # resize the frame
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer()
        inputTwoSizer = wx.BoxSizer()
        inputThreeSizer = wx.BoxSizer()
        inputFourSizer = wx.BoxSizer()
        submitBtnSizer = wx.BoxSizer()

        titleSizer.Add(window=titleIco, proportion = 0, flag = wx.ALL, border = 5)
        titleSizer.Add(window=title, proportion = 0, flag = wx.ALL, border = 5)

        inputOneSizer.Add(window=inputOneIco, proportion=0, flag=wx.ALL, border=5)
        inputOneSizer.Add(window=labelOne, proportion=0, flag=wx.ALL, border=5)
        inputOneSizer.Add(window=self.inputTxtOne, proportion=1, flag=wx.ALL|wx.EXPAND ,border=5)
        # proportion =1 to enable the Expand

        inputTwoSizer.Add(window=inputTwoIco, proportion=0, flag=wx.ALL, border=5)
        inputTwoSizer.Add(window=labelTwo, proportion=0, flag=wx.ALL, border=5)
        inputTwoSizer.Add(window=self.inputTwo, proportion=1, flag=wx.ALL, border=5)

        inputThreeSizer.Add(window=inputThreeIco, proportion=0, flag=wx.ALL, border=5)
        inputThreeSizer.Add(window=labelThree, proportion=0, flag=wx.ALL, border=5)
        inputThreeSizer.Add(window=self.inputThree, proportion=1, flag=wx.ALL, border=5)

        inputFourSizer.Add(window=inputFourIco, proportion=0, flag=wx.ALL, border=5)
        inputFourSizer.Add(window=labelFour, proportion=0, flag=wx.ALL, border=5)
        inputFourSizer.Add(window=self.inputFour1, proportion=1, flag=wx.ALL, border=5)
        inputFourSizer.Add(window=self.inputFour2, proportion=1, flag=wx.ALL, border=5)
        inputFourSizer.Add(window=self.inputFour3, proportion=1, flag=wx.ALL, border=5)
        inputFourSizer.Add(window=self.inputFour4, proportion=1, flag=wx.ALL, border=5)

        submitBtnSizer.Add(okBtn, 0, wx.ALL, 5)
        submitBtnSizer.Add(cancelBtn, 0, wx.ALL, 5)

        mainSizer.Add(titleSizer, 0 , wx.CENTER|wx.ALL,5)
        mainSizer.Add(inputOneSizer, 1, wx.ALL|wx.EXPAND,5)
        mainSizer.Add(inputTwoSizer, 0, wx.ALL,5)
        mainSizer.Add(inputThreeSizer, 0, wx.ALL,5)
        mainSizer.Add(inputFourSizer, 0, wx.ALL,5)
        mainSizer.Add(submitBtnSizer, 0, wx.ALL|wx.CENTER,5) # make button center

        self.SetSizer(mainSizer)
        mainSizer.Fit(self) # set the window for the proper size
        self.Layout()


        def onOK(self,event):
            # Do something
            print("OK")
            data = self.getData
            print("data:", data)

        def onCancel(self,event):
            self.closeProgram()

        def closeProgram(self):
            # self.GetParent() will get the frame which has the .Close() method to close the program
            self.GetParent().Close()

        def getData(self):
            # this here will procure data from all button
            pass

"""
        #self._dont_show = False # for message dialog box

        #####################add hello world massese######################
        welcomeText = wx.StaticText(self, id=wx.ID_ANY, label="hello world", pos = (100,100)) # text position
        # ID_ANY means that id does not matter

        ######################add text box#################################
        self._textbox = wx.TextCtrl(parent=self, value='Enter Name', pos=(20,60))

        ######################add button here############################
        self._button = wx.Button(parent=self, label="here", pos=(20,80))
        self._button.Bind(event=wx.EVT_BUTTON, handler=self.onSubmit) # bind function when click



    def ShowDialog(self):
        if self._dont_show:
            return None # if checked, stop here
        dlg = wx.RichMessageDialog(parent=None,
                                   message="Hi, this is box",
                                   caption = "my box",
                                   style= wx.YES_NO|wx.CANCEL|wx.CENTER)
        dlg.ShowCheckBox("Click here to never show again")           #display check box
        dlg.ShowModal()              # display the dialog box
        if dlg.IsCheckBoxChecked():
            self._dont_show = True   # return true if check box checked

    def onSubmit(self,event): # action when click button
        #webbrowser.open('www.google.com')
        print(self._textbox.GetValue()) # get the value from text box

        self.ShowDialog() # show the check box
"""

############################################ init run #################################################
if __name__ == '__main__':
    app = MyApp()

    app.MainLoop() # Start the event loop.
from loadCSV import *
from leftPanel import *
from rightPanelOne import *
from rightPanelTwo import *

class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None, title = "title", size = (1080,600)) # from wx

        # load database
        loadData = LoadCSV().load()

        # split the window
        splitter = wx.SplitterWindow(self)

       # rightOne = RightPanelOne(splitter,loadData)
        rightTwo = RightPanelTwo(splitter,loadData)
        left = LeftPanel(splitter,rightTwo, loadData) # give a control panel a reference to figure panel
        splitter.SplitVertically(left, rightTwo)
        splitter.SetMinimumPaneSize(350)

       # right.draw() # draw the function, should move to other place
        rightTwo.drawTable() # set the table as defult


if __name__ == "__main__":
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()
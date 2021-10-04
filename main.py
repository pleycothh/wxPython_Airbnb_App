from loadCSV import *
from leftPanel import *
from rightPanel import *






class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent = None, title = "title", size = (800,600)) # from wx

        # load database
        loadData = LoadCSV()

        # split the window
        splitter = wx.SplitterWindow(self)
        right = RightPanel(splitter)
        left = LeftPanel(splitter, right, loadData) # give a control panel a reference to figure panel
        splitter.SplitVertically(left,right)
        splitter.SetMinimumPaneSize(200)

        right.draw()


if __name__ == "__main__":
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()
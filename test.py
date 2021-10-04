
import wx
import wx.grid as grid


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(800, 600))

        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)

        mygrid = grid.Grid(self)
        mygrid.CreateGrid(26, 9)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(mygrid, 1, wx.EXPAND)
        self.SetSizer(sizer)


class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Grid In WxPython")
        self.frame.Show()
        return True


app = MyApp()
app.MainLoop()



import wx
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np




class RightPanel (wx.Panel): # class need inhertance of wx.Panel
    def __init__(self, parent, loadData):
        wx.Panel.__init__(self, parent=parent) # pass the split window to parent

       #wx.Button(self, -1, "Button right")

        self.data_summary = loadData



    def drawMap(self):

        self.figure = Figure() # what does this do?
        self.axes = self.figure.add_subplot(111)
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

################################## table display ####################################
    def drawTable(self):
        summary = self.data_summary # load the entire data
        print(summary.name)

        ###
        data = [[ 66386, 174296,  75131, 577908,  32015],
                [ 58230, 381139,  78045,  99308, 160454],
                [ 89135,  80552, 152558, 497981, 603535],
                [ 78415,  81858, 150656, 193263,  69638],
                [139361, 331509, 343164, 781380,  52269]]

        columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
        rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]

        values = np.arange(0, 2500, 500)
        value_increment = 1000

        # Get some pastel shades for the colors
        colors = plt.cm.BuPu(np.linspace(0, 0.5, len(rows)))
        n_rows = len(data)

        index = np.arange(len(columns)) + 0.3
        bar_width = 0.4

        # Initialize the vertical-offset for the stacked bar chart.
        y_offset = np.zeros(len(columns))

        # Plot bars and create text labels for the table
        cell_text = []
        for row in range(n_rows):
            plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
            y_offset = y_offset + data[row]
            cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
        # Reverse colors and text labels to display the last value at the top.
        colors = colors[::-1]
        cell_text.reverse()

        # Add a table at the bottom of the axes
        the_table = plt.table(cellText=cell_text,
                              rowLabels=rows,
                              rowColours=colors,
                              colLabels=columns,
                              loc='bottom')

        # Adjust layout to make room for the table:
        plt.subplots_adjust(left=0.2, bottom=0.2)

        plt.ylabel("Loss in ${0}'s".format(value_increment))
        plt.yticks(values * value_increment, ['%d' % val for val in values])
        plt.xticks([])
        plt.title('Loss by Disaster')
        ###

    def changeSuber(self,newSuber):
        pass
    def changeDate(self,newDate):
        pass
    def changeKeyWord(self, newKey):
        pass
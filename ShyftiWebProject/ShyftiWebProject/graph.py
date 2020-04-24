import matplotlib.pyplot as plt
from matplotlib import ticker
from enum import Enum
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from flask import Response

class PlotType(Enum): 
    NotSpecified = 0
    Linear = 1
    Logarithmic = 2

class Graph():
    def __init__(self, data):
        self.data = data

    def create_figurelinear(self):
        xs = [i[0] for i in self.data]
        ys = [i[1] for i in self.data]

        fig = plt.figure()
        ax= fig.add_subplot(1, 1, 1)
        fig.autofmt_xdate() 

        M = 10
        xticks = ticker.MaxNLocator(M)

        ax.xaxis.set_major_locator(xticks)
        ax.set_title(f"Linear - (From {xs[0]} to {xs[-1]})")

        ax.set_xlabel('Date')
        ax.set_ylabel('Cases')

        plt.plot(xs, ys)
        return fig

    def create_figurelog(self):
        xs = [i[0] for i in self.data]
        ys = [i[1] for i in self.data]

        fig = plt.figure()
        ax= fig.add_subplot(1, 1, 1)
        fig.autofmt_xdate()
        fig.suptitle('')

        M = 10
        xticks = ticker.MaxNLocator(M)
    
        ax.xaxis.set_major_locator(xticks)
        ax.set_title(f"Logarithmic - (From {xs[0]} to {xs[-1]})")
        ax.set_xlabel('Date')
        ax.set_ylabel('Cases')
        ax.set_yscale('log')

        plt.plot(xs, ys, color='orange')
        return fig

    def getPlotImage(self, plotType = PlotType.NotSpecified):
        if(plotType == PlotType.Logarithmic):
            fig = self.create_figurelinear()
        else:
            fig = self.create_figurelog()

        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')
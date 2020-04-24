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

    def create_figurelastten(self):
        target_y = [i[1] for i in self.data[-11:]]
        difference = []

        for idx, val in enumerate(target_y[:-1]):
            difference.append(target_y[idx + 1] - val)

        xs = [i[0] for i in self.data[-10:]]
        ys = difference


        fig = plt.figure()
        ax= fig.add_subplot(1, 1, 1)
        fig.autofmt_xdate()

        ax.set_title(f"Confirmed new cases in UK over last 10 days")
        ax.set_xlabel('Date')
        ax.set_ylabel('Cases')

        xlocs, xlabs = plt.xticks()
        xlocs=[i+1 for i in range(0,10)]

        for i, v in enumerate(ys):
            plt.text(xlocs[i] - 1.4, v + 0.02, str(v))

        plt.bar(xs, ys, color='blue')
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
            fig = self.create_figurelog()
        else:
            fig = self.create_figurelinear()

        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

    def getLastFiveDaysPlotImage(self):
        fig = self.create_figurelastten()
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

import json
import requests
import datetime
import dateutil.parser
import ShyftiWebProject.coronavirus
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

def getJsonFiltered():
    inputJson = getLatestCoronaInformationUKJson()
    castedJson = json.loads(inputJson)
    filteredJson = [x for x in castedJson if x['Province'] == '']
    outputJson = json.dumps(filteredJson)
    return outputJson

def formattedDateTimeNow():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%dT%H:%M:%SZ")


def getLatestCoronaInformationUKJson():
    dateTimeNow = formattedDateTimeNow()
    return requests.get(f"https://api.covid19api.com/country/united-kingdom/status/confirmed?from=2020-03-01T00:00:00Z&to={dateTimeNow}").text

def getCoronaData():
    filteredJson = getJsonFiltered()
    castedJson = json.loads(filteredJson)
    coronaCaseList = []

    for coronaDayItem in castedJson:
        coronaDetails = { "date": None, "cases":None}
        coronaDetails["date"] = coronaDayItem["Date"]
        coronaDetails["cases"] = coronaDayItem["Cases"]
        coronaCaseList.append(coronaDetails)

    return coronaCaseList

def getCoronaDataArray():
    coronaData = getCoronaData()
    formattedArray = []
    idx = 0

    for coronaDataItem in coronaData:
        parseDate = dateutil.parser.parse(coronaDataItem["date"])

        formattedArray.insert(len(formattedArray), [parseDate.strftime('%d/%m/%Y'), coronaDataItem["cases"]])
        idx += 1

    return formattedArray



def create_figurelinear():
    data = ShyftiWebProject.coronavirus.getCoronaDataArray()
    xs = [i[0] for i in data]
    ys = [i[1] for i in data]

    fig = plt.figure()
    ax= fig.add_subplot(1, 1, 1)
    fig.autofmt_xdate() 

    M = 10
    xticks = ticker.MaxNLocator(M)

    ax.xaxis.set_major_locator(xticks)
    ax.set_title('Linear')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cases')

    plt.plot(xs, ys)
    return fig

def create_figurelog():
    data = ShyftiWebProject.coronavirus.getCoronaDataArray()
    xs = [i[0] for i in data]
    ys = [i[1] for i in data]

    fig = plt.figure()
    ax= fig.add_subplot(1, 1, 1)
    fig.autofmt_xdate()
    fig.suptitle('')

    M = 10
    xticks = ticker.MaxNLocator(M)
    
    ax.xaxis.set_major_locator(xticks)
    ax.set_title('Logarithmic')
    ax.set_xlabel('Date')
    ax.set_ylabel('Cases')
    ax.set_yscale('log')

    plt.plot(xs, ys, color='orange')
    return fig

def getPlotImage(plotType = PlotType.NotSpecified):
    if(plotType == PlotType.Logarithmic):
        fig = create_figurelinear()
    else:
        fig = create_figurelog()

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
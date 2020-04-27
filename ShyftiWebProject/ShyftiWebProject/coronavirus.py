import json
import requests
import datetime
import dateutil.parser
from ShyftiWebProject.graph import Graph
from ShyftiWebProject.graph import PlotType

class CoronaVirus:
    def __init__(self, data):
        self.countrty = data

class CoronaVirusUK():
    def __init__(self, data):
        self.data = data

    def getPlotImage(self, plotType = PlotType.NotSpecified): 
        graph = Graph(self.data)
        return graph.getPlotImage(plotType)

    def getLastTenDaysPlotImageConfirmed(self): 
        graph = Graph(self.data)
        return graph.getLastTenDaysPlotImageConfirmed()

    def getLastTenDaysPlotImageDeaths(self): 
        graph = Graph(self.data)
        return graph.getLastTenDaysPlotImageDeaths()
       
    @staticmethod
    def getCoronaDataArray():
        coronaData = CoronaVirusUK.getCoronaData()
        formattedArray = []
        idx = 0

        for coronaDataItem in coronaData:
            parseDate = dateutil.parser.parse(coronaDataItem["date"])

            formattedArray.insert(len(formattedArray), [parseDate.strftime('%d/%m/%Y'), coronaDataItem["confirmed"], coronaDataItem["deaths"], coronaDataItem["active"], coronaDataItem["recovered"]])
            idx += 1

        return formattedArray

    @staticmethod
    def getJsonFiltered():
        inputJson = CoronaVirusUK.getLatestCoronaInformationUKJson()
        castedJson = json.loads(inputJson)
        filteredJson = [x for x in castedJson if x['Province'] == '']
        outputJson = json.dumps(filteredJson)
        return outputJson

    @staticmethod
    def formattedDateTimeNow():
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%dT%H:%M:%SZ")

    @staticmethod
    def getLatestCoronaInformationUKJson():
        dateTimeNow = CoronaVirusUK.formattedDateTimeNow()
        return requests.get(f"https://api.covid19api.com/country/united-kingdom?from=2020-03-01T00:00:00Z&to={dateTimeNow}").text

    @staticmethod
    def getCoronaData():
        filteredJson = CoronaVirusUK.getJsonFiltered()
        castedJson = json.loads(filteredJson)
        coronaCaseList = []

        for coronaDayItem in castedJson:
            coronaDetails = { "date": None, "confirmed":None, "deaths": 0}
            coronaDetails["date"] = coronaDayItem["Date"]
            coronaDetails["confirmed"] = coronaDayItem["Confirmed"]
            coronaDetails["deaths"] = coronaDayItem["Deaths"]
            coronaDetails["recovered"] = coronaDayItem["Recovered"]
            coronaDetails["active"] = coronaDayItem["Active"]
            coronaCaseList.append(coronaDetails)

        return coronaCaseList
import json
import requests
import datetime
import dateutil.parser
from ShyftiWebProject.graph import Graph
from ShyftiWebProject.graph import PlotType

class CoronaVirusUK():
    def __init__(self, data):
        self.data = data

    def getPlotImage(self, plotType = PlotType.NotSpecified): 
        graph = Graph(self.data)
        return graph.getPlotImage(plotType)
       
    @staticmethod
    def getCoronaDataArray():
        coronaData = CoronaVirusUK.getCoronaData()
        formattedArray = []
        idx = 0

        for coronaDataItem in coronaData:
            parseDate = dateutil.parser.parse(coronaDataItem["date"])

            formattedArray.insert(len(formattedArray), [parseDate.strftime('%d/%m/%Y'), coronaDataItem["cases"]])
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
        return requests.get(f"https://api.covid19api.com/country/united-kingdom/status/confirmed?from=2020-03-01T00:00:00Z&to={dateTimeNow}").text

    @staticmethod
    def getCoronaData():
        filteredJson = CoronaVirusUK.getJsonFiltered()
        castedJson = json.loads(filteredJson)
        coronaCaseList = []

        for coronaDayItem in castedJson:
            coronaDetails = { "date": None, "cases":None}
            coronaDetails["date"] = coronaDayItem["Date"]
            coronaDetails["cases"] = coronaDayItem["Cases"]
            coronaCaseList.append(coronaDetails)

        return coronaCaseList
import json
import requests
import datetime
import dateutil.parser

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
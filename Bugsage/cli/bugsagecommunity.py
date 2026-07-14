import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()
backendurlErrorType = os.getenv('Bugsage_Community_URL_ErrorType')
backendurlErrorCase = os.getenv('Bugsage_Community_URL_ErrorCase')
backendurlUpvote = os.getenv('Bugsage_Community_URL_Upvote')
backendurlDownvote = os.getenv('Bugsage_Community_URL_Downvote')
def BugsageCommunity(errorCase,errorType):
    response = requests.get(backendurlErrorCase,params={"caseName":errorCase})
    if not response.json()['count']:
        response = requests.get(backendurlErrorType,params={"errorType":errorType})
    if not response.json() or response.status_code != 200:
        return (False,None)
    return (True,response)
def Upvote(id):
    response = requests.post(f"{backendurlUpvote}/{id}")
    return response.json()
def Downvote(id):
    response = requests.post(f"{backendurlDownvote}/{id}")
    return response.json()
def AiToBugsageCommunity(response):
    data = json.loads(response)
    errorTypes = data['errorType']
    errorCases = data['errorCases']
    responseErrorTypes = requests.post(backendurlErrorType,data=errorTypes)
    errorTypeId = responseErrorTypes.json()['id']
    errorCases["ErrorTypeID"] = errorTypeId
    responseErrorCases = requests.post(backendurlErrorCase,data=errorCases)
def next(response):
    nextresponse = requests.get(response.json()['next'])
    return nextresponse
def prev(response):
    prevresponse = requests.get(response.json()['previous'])
    return prevresponse


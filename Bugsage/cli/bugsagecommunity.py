import os
import requests
import json
from dotenv import load_dotenv
from ..utils.fingerprintgenerator import generateErrorCaseFingerprint, generateErrorTypeFingerprint
load_dotenv()
backendurlErrorType = os.getenv('Bugsage_Community_URL_ErrorType')
backendurlErrorCase = os.getenv('Bugsage_Community_URL_ErrorCase')
backendurlUpvote = os.getenv('Bugsage_Community_URL_Upvote')
backendurlDownvote = os.getenv('Bugsage_Community_URL_Downvote')
backendurlErrorTypeExist = os.getenv('Bugsage_Community_URL_ErrorTypeExists')
backendurlErrorCaseExist = os.getenv('Bugsage_Community_URL_ErrorCaseExists')
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
def checkIfErrorTypeFingerPrintExist(fingerprint):
    response = requests.get(backendurlErrorTypeExist, params={"fingerprint":fingerprint})
    print(response.json())
    if response.json()['exists']:
        return True
    else:
        return False
def checkIfErrorCaseFingerPrintExist(fingerprint):
    response = requests.get(backendurlErrorCaseExist, params={"fingerprint":fingerprint})
    if response.json()['exists']:
        return True
    else:
        return False
def AiToBugsageCommunity(response,model_version):
    data = json.loads(response)
    errorTypes = data['errorType']
    errorTypeFingerPrint = generateErrorTypeFingerprint(errorTypes.get("errorType"),model_version)
    if not checkIfErrorTypeFingerPrintExist(errorTypeFingerPrint):
        errorTypes['fingerPrint'] = errorTypeFingerPrint
        errorTypes["AiModel"] = model_version
        responseErrorTypes = requests.post(backendurlErrorType,data=errorTypes)
        print(responseErrorTypes)
    errorCases = data['errorCases']
    errorTypeId = responseErrorTypes.json()['id']
    errorCaseFingerPrint = generateErrorCaseFingerprint(errorCases.get('errorCase'),model_version,errorTypeId)
    if not checkIfErrorCaseFingerPrintExist(errorCaseFingerPrint):
        errorCases['fingerPrint'] = errorCaseFingerPrint
        errorCases['AiModel'] = model_version
        errorCases["ErrorTypeID"] = errorTypeId
        responseErrorCases = requests.post(backendurlErrorCase,data=errorCases)
    print(responseErrorTypes,responseErrorCases)
def next(response):
    nextresponse = requests.get(response.json()['next'])
    return nextresponse
def prev(response):
    prevresponse = requests.get(response.json()['previous'])
    return prevresponse


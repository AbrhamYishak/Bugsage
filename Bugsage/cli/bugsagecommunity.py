import os
import requests
import json
from dotenv import load_dotenv
from Bugsage.utils.fingerprintgenerator import generateErrorCaseFingerprint, generateErrorTypeFingerprint
from Bugsage.utils.similaritycheck import similaritycheck
from Bugsage.exceptions import NextPageError, PrevPageError, NoInternetError
load_dotenv()
backendurlErrorType = os.getenv('Bugsage_Community_URL_ErrorType')
backendurlErrorCase = os.getenv('Bugsage_Community_URL_ErrorCase')
backendurlUpvote = os.getenv('Bugsage_Community_URL_Upvote')
backendurlDownvote = os.getenv('Bugsage_Community_URL_Downvote')
backendurlErrorTypeExist = os.getenv('Bugsage_Community_URL_ErrorTypeExists')
backendurlErrorCaseExist = os.getenv('Bugsage_Community_URL_ErrorCaseExists')
def BugsageCommunity(errorCase,errorType):
    try:
        response = requests.get(backendurlErrorCase,params={"caseName":errorCase})
        if not response.json()['count']:
            response = requests.get(backendurlErrorType,params={"errorType":errorType})
        if not response.json()['count'] or response.status_code != 200:
            return (False,None)
        return (True,response)
    except requests.ConnectionError:
        raise NoInternetError("No internet connection.")
def Upvote(id):
    try:
        response = requests.post(f"{backendurlUpvote}/{id}")
        return response.json()
    except requests.ConnectionError:
        raise NoInternetError("No internet connection.")
def Downvote(id):
    try:
        response = requests.post(f"{backendurlDownvote}/{id}")
        return response.json()
    except requests.ConnectionError:
            raise NoInternetError("No internet connection.")
def checkIfErrorTypeFingerPrintExist(fingerprint):
    try:
        response = requests.get(backendurlErrorTypeExist, params={"fingerprint":fingerprint})
        if response.json()['exists']:
            return (True,response.json()['errorType'])
        else:
            return (False,None)
    except requests.ConnectionError:
            raise NoInternetError("No internet connection.")    
def checkIfErrorCaseFingerPrintExist(fingerprint):
    try:
        response = requests.get(backendurlErrorCaseExist, params={"fingerprint":fingerprint})
        if response.json()['exists']:
            return True
        else:
            return False
    except requests.ConnectionError:
            raise NoInternetError("No internet connection.")       
def AiToBugsageCommunity(response,model_version):
    data = json.loads(response)
    errorTypes = data['errorType']
    errorTypeFingerPrint = generateErrorTypeFingerprint(errorTypes.get("errorType"),model_version)
    fingerPrintExist,existingErrorTypes = checkIfErrorTypeFingerPrintExist(errorTypeFingerPrint)  
    newCreated = False
    if fingerPrintExist:
        for existingErrorType in existingErrorTypes:
            existingPackage = existingErrorType ['package']
            if similaritycheck(existingPackage,errorTypes.get("package")):
                responseErrorTypes = existingErrorType
                break
        else:
            errorTypes['fingerPrint'] = errorTypeFingerPrint
            errorTypes["AiModel"] = model_version
            errorTypes["createdByAI"] = True
            responseErrorTypes = requests.post(backendurlErrorType,data=errorTypes)
            newCreated = True
    else:
        errorTypes['fingerPrint'] = errorTypeFingerPrint
        errorTypes["AiModel"] = model_version
        errorTypes["createdByAI"] = True
        responseErrorTypes = requests.post(backendurlErrorType,data=errorTypes)
        newCreated = True
    if newCreated:
        errorTypeId = responseErrorTypes.json()['id']
    else:
        errorTypeId = responseErrorTypes['id']
    errorCases = data['errorCases']
    errorCaseFingerPrint = generateErrorCaseFingerprint(errorCases.get('errorCase'),model_version,errorTypeId)
    if not checkIfErrorCaseFingerPrintExist(errorCaseFingerPrint):
        errorCases['fingerPrint'] = errorCaseFingerPrint
        errorCases['AiModel'] = model_version
        errorCases["ErrorTypeID"] = errorTypeId
        responseErrorCases = requests.post(backendurlErrorCase,data=errorCases)
def next(response):
    nextPage = response.json()['next']
    if nextPage:
        nextresponse = requests.get(response.json()['next'])
        return nextresponse
    raise NextPageError("This is the Last Page.")
def prev(response):
    prevPage = response.json()['previous']
    if prevPage:
        prevresponse = requests.get(response.json()['previous'])
        return prevresponse
    raise PrevPageError("This is the Frist Page.")


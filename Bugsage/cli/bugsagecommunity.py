import os
import requests
from .response import ResponseFromatter
from dotenv import load_dotenv
load_dotenv()
backendurlErrorType = os.getenv('Bugsage_Community_URL_ErrorType')
backendurlErrorCase = os.getenv('Bugsage_Community_URL_ErrorCase')
def BugsageCommunity(errorCase,errorType):
    response = requests.get(backendurlErrorCase,params={"caseName":errorCase})
    if not response.json():
        response = requests.get(backendurlErrorType,params={"errorType":errorType})
    if not response.json() or response.status_code != 200:
        return False
    ResponseFromatter(response)
    return True
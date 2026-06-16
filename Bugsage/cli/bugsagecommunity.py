import os
import requests
from dotenv import load_dotenv
load_dotenv()
backendurlErrorType = os.getenv('Bugsage_Community_URL_ErrorType')
backendurlErrorCase = os.getenv('Bugsage_Community_URL_ErrorCase')
backendurlUpvote = os.getenv('Bugsage_Community_URL_Upvote')
backendurlDownvote = os.getenv('Bugsage_Community_URL_Downvote')
def BugsageCommunity(errorCase,errorType):
    response = requests.get(backendurlErrorCase,params={"caseName":errorCase})
    if not response.json():
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
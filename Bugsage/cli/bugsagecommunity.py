import os
import requests
from dotenv import load_dotenv
load_dotenv()
backendurl = os.getenv('Bugsage_Community_URL')
def BugsageCommunity(errorCype,errorType):
    response = requests.get(backendurl)
    print(response.status_code)
    print(response.json())
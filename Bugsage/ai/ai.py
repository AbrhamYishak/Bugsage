import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
apikey = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = apikey)
def GeminiSearch(error,code):
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents="""
        You are an error analysis engine for BugSage.

        Analyze the programming error and return ONLY valid JSON.

        Rules:

        * Return only JSON
        * No markdown
        * No explanations outside JSON
        * If information is unknown use null
        * Never invent documentation URLs
        * Severity must be one of:
        ["LOW","MEDIUM","HIGH","CRITICAL"]
        * Category must be one of:
        ["SYNTAX","RUNTIME","LOGIC","NETWORK","DATABASE","AUTH","IMPORT","TYPE","MEMORY","API","UNKNOWN"]

        Required JSON format:

        {
        "errorType": {
        "errorType": "",
        "package": "",
        "category": "",
        "severity": "",
        "generalExplanation": "",
        "generalFix": "",
        "docsUrl": ""
        },
        "errorCases": [
        {
        "caseName": "",
        "explanation": "",
        "fix": "",
        "example": "",
        "severity": ""
        }
        ]
        }

        Analyze this error:

        ERROR_MESSAGE_HERE

        %s

        Optional user code:

        %s

        """%(error,code)
    )
    print(response.text)
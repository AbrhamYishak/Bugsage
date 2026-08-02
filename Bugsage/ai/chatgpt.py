from openai import OpenAI
from Bugsage.database.db import getSelectedAPIKey
apikey = getSelectedAPIKey()
client = OpenAI(api_key = apikey)

def chatgpt(error, code):
    prompt = f"""
    You are an error analysis engine for BugSage.

    Analyze the programming error and return ONLY valid JSON.

    Rules:
    - Return only JSON.
    - No markdown.
    - No explanations outside JSON.
    - If information is unknown use null.
    - Never invent documentation URLs.
    - Severity must be one of:
    ["LOW","MEDIUM","HIGH","CRITICAL"]
    - Category must be one of:
    ["SYNTAX","RUNTIME","LOGIC","NETWORK","DATABASE","AUTH","IMPORT","TYPE","MEMORY","API","UNKNOWN"]

    Required JSON format:

    {{
    "errorType": {{
        "errorType": "",
        "package": "",
        "category": "",
        "severity": "",
        "generalExplanation": "",
        "generalFix": "",
        "docsUrl": ""
    }},
    "errorCases": {{
        "caseName": "",
        "explanation": "",
        "fix": "",
        "example": "",
        "severity": ""
    }}
    }}

    Analyze this error:

    {error}

    Optional user code:

    {code}
    """
    try:
        response = client.responses.create(
            model="gpt-5.6",
            input=prompt,
        )

        return (True,response.output_text,"gpt-5.6")
    except Exception as e:
        return (False,e.message)
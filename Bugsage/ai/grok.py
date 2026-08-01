import requests
from Bugsage.database.db import getSelectedAPIKey
api_key = getSelectedAPIKey

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
}


def grok(error,code):
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
    data = {
    "model": "grok-4.5",
    "input": prompt
}
    response = requests.post(
        "https://api.x.ai/v1/responses",
        headers=headers,
        json=data,
    )

    print(response.json())
import os
from dotenv import load_dotenv
from google import genai
load_dotenv()
apikey = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = apikey)
def GeminiSearch(error):
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=f"Explain why this code failed i will pass you the error and you will give me a response in the given format below, the error is {error} the format is errorType, Explanation, possible fix and example for this error and make it specific to my problem"
    )
    print(response.text)
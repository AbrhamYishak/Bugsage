from bugsage.database.db import getSelectedModel
from bugsage.ai.gemini import gemini
from bugsage.ai.chatgpt import chatgpt
from bugsage.ai.grok import grok
def aiSearch(error,code):
    model = getSelectedModel()
    if model == "Gemini":
        return gemini(error,code)
    elif model == "Chatgpt":
        return chatgpt(error,code)
    elif model == "Grok":
        return grok(error,code)
    else:
        return None

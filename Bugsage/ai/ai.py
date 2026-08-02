from Bugsage.database.db import getSelectedModel
from Bugsage.ai.gemini import gemini
from Bugsage.ai.chatgpt import chatgpt
from Bugsage.ai.grok import grok
def aiSearch(error,code):
    model = getSelectedModel()
    print(model)
    if model == "Gemini":
        return gemini(error,code)
    elif model == "Chatgpt":
        return chatgpt(error,code)
    elif model == "Grok":
        return grok(error,code)
    else:
        return None

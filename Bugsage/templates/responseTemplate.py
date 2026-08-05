from rich import print
def formatResponse(response):
    errorType = response[0]['errorType']
    category = response[0]['category']
    generalExplanation = response[0]['generalExplanation']
    generalFix = response[0]['generalFix']
    docs = response[0]['docsUrl']
    createdByAi = response[0]['createdByAI']
    AiModel = response[0]['AiModel']
    print()
    print("________________________________________________")
    print()
    print("Error Type")
    print(errorType)
    print()
    print("Explanation")
    print(generalExplanation)
    print()
    print("Solution")
    print(generalFix)
    print()
    print("Docs Link")
    print(docs)
    print()
    if createdByAi:
        print("AI model")
        print(AiModel)
        print()
    print("________________________________________________")
def formatAIResponse(reponse):
    print(reponse.json())

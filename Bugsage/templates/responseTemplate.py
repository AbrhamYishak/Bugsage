from rich import print
import json
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
def formatAIResponse(response):
    response = json.loads(response)
    errorType = response['errorType']['errorType']
    generalExplanation = response['errorType']['generalExplanation']
    generalFix = response['errorType']['generalFix']
    docs = response['errorType']['docsUrl']
    errorCase = response['errorCases']['caseName']
    explanation = response['errorCases']['explanation']
    fix = response['errorCases']['fix']
    example = response['errorCases']['example']
    print("Succesful")
    print()
    print("Error Type")
    print(errorType)
    print("________________________________________________")
    print()
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
    print("________________________________________________")
    print()
    print("Error Case")
    print(errorCase)
    print("________________________________________________")
    print()
    print()
    print("Explanation")
    print(explanation)
    print()
    print("Solution")
    print(fix)
    print()
    print("Example")
    print(example)
    print()
    print("________________________________________________")
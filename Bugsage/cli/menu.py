from rich import print
from ..database.db import AddAPIKeys,getAPIKeys
import typer
def apiManagementMenu():
    print("Api Management")
    print("1, List API Keys")
    print("2, Add API Keys")
    print("3, Remove API Keys")
    print("4, Update API Keys")
    choice = typer.prompt("Choice")
    if choice == "1":
        apikeys = getAPIKeys()
        print("[bold yellow]Output format (ModelName,APIKey)[/bold yellow]")
        for apikey in apikeys:
            print(apikey)
    elif choice == "2":
        APIKey = typer.prompt("Please Add the API key")
        ModelName = typer.prompt("Please Add the AI model name")
        AddAPIKeys(APIKey,ModelName)
# def modelMenu():

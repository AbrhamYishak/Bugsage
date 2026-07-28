from rich import print
from Bugsage.database.db import addAPIKey,getAPIKeys,removeAPIKey,updateAPIKey,selectAPIKey,addModel,getModels,removeModel,selectModel
import typer
def apiManagementMenu():
    print("API Management")
    print("1. List API Keys")
    print("2. Add API Key")
    print("3. Remove API Key")
    print("4. Update API Key")
    print("5. Select API Key")

    choice = typer.prompt("Choice")

    if choice == "1":
        apikeys = getAPIKeys()
        print("\nID\tModel\t\tAPI Key")
        print("-" * 50)
        for api in apikeys:
            print(api)

    elif choice == "2":
        apikey = typer.prompt("Enter API Key")
        modelname = typer.prompt("Enter Model Name")
        addAPIKey(apikey, modelname)
        print("API key added successfully.")

    elif choice == "3":
        apikey = typer.prompt("Enter API Key to remove")
        removeAPIKey(apikey)
        print("API key removed successfully.")

    elif choice == "4":
        old_key = typer.prompt("Old API Key")
        new_key = typer.prompt("New API Key")
        updateAPIKey(old_key, new_key)
        print("API key updated successfully.")

    elif choice == "5":
        apikeys = getAPIKeys()

        print("\nAvailable API Keys")
        print("-" * 50)
        for api in apikeys:
            print(api)

        api_id = int(typer.prompt("Enter API ID"))
        selectAPIKey(api_id)

        print("API key selected successfully.")

    else:
        print("Invalid choice.")
def modelMenu():
    print("Model Management")
    print("1. List Models")
    print("2. Add Model")
    print("3. Remove Model")
    print("4. Select Model")

    choice = typer.prompt("Choice")

    if choice == "1":
        models = getModels()

        print("\nID\tModel Name")
        print("-" * 30)

        for model in models:
            print(model)

    elif choice == "2":
        modelname = typer.prompt("Enter Model Name")
        addModel(modelname)

        print("Model added successfully.")

    elif choice == "3":
        modelname = typer.prompt("Enter Model Name to remove")
        removeModel(modelname)

        print("Model removed successfully.")

    elif choice == "4":
        models = getModels()

        print("\nAvailable Models")
        print("-" * 30)

        for model in models:
            print(model)

        model_id = int(typer.prompt("Enter Model ID"))

        try:
            selectModel(model_id)
            print(" Model selected successfully.")
        except Exception as e:
            print(f" {e}")
            print("Please add an API key for this model before selecting it.")

    else:
        print("Invalid choice.")
from rich import print
import typer
def ResponseFromatterBugsageCommunity(response):
    responseCode = response.status_code
    response = response.json()
    if responseCode== 200:
        print("[bold green]Successful [/bold green]")  
        print(response)
def ResponseFromatterAI(response):
    print(response)
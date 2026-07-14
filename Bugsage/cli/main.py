import typer
from rich import print,console
from ..analyzer.parser import parser
from .response import ResponseFromatterBugsageCommunity,ResponseFromatterAI
from .bugsagecommunity import AiToBugsageCommunity
from .menu import apiManagementMenu
app = typer.Typer()  
consol = console.Console()
@app.command()
def run(filename: str, ai: bool = False):
    """
    This tool use prev errors and provide explanation and possible fix
    """
    if ai:
        print("[bold red]Ai being used[/bold red]")
        with consol.status("[bold cyan]🤖 Asking AI ... ", spinner="dots"):
            Ai, status, result = parser(filename=filename,ai=True)
        ResponseFromatterAI(result,status)
        AiToBugsageCommunity(result)
    else:
        with consol.status("Starting...", spinner="dots") as status:
            def update(message, spinner="dots"):
                status.update(message, spinner=spinner)
            Ai, status, result = parser(filename=filename,statusCallBack=update)
        if not Ai:
            ResponseFromatterBugsageCommunity(result)
        else:
            AiToBugsageCommunity(result)
            ResponseFromatterAI(result,status)
        
@app.command()
def menu():
    while True:
        print("[bold green]======== Welcome To Bugsage ========[/bold green]")
        typer.echo("1. API Management")
        typer.echo("2. AI Models")
        typer.echo("3. Local Storage")
        typer.echo("4. Exit")

        choice = typer.prompt("Choice")

        if choice == "1":
            apiManagementMenu()
            break
        elif choice == "2":
            # model_menu()
            print(2)
            break
        elif choice == "3":
            print(3)
            break
        elif choice == "4":
            break
        else:
            typer.echo("Invalid choice")
if __name__ == "__main__":
    app()
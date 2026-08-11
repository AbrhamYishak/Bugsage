import typer
from rich import print,console
from Bugsage.analyzer.parser import parser
from Bugsage.cli.response import ResponseFromatterBugsageCommunity,ResponseFromatterAI
from Bugsage.cli.bugsagecommunity import AiToBugsageCommunity
from Bugsage.cli.menu import apiManagementMenu,modelMenu
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
            Ai, status, result, model_version = parser(filename=filename,ai=True)
        ResponseFromatterAI(result,status)
        AiToBugsageCommunity(result,model_version)
    else:
        with consol.status("Starting...", spinner="dots") as status:
            def update(message, spinner="dots"):
                status.update(message, spinner=spinner)
            Ai, status, result, model_version = parser(filename=filename,statusCallBack=update)
        if not Ai:
            ResponseFromatterBugsageCommunity(result)
        else:
            AiToBugsageCommunity(result,model_version)
            ResponseFromatterAI(result,status)
        
@app.command()
def menu():
    """

    """
    while True:
        print("[bold green]======== Welcome To Bugsage ========[/bold green]")
        typer.echo("1. API Management")
        typer.echo("2. AI Models")
        typer.echo("3. Exit")

        choice = typer.prompt("Choice")

        if choice == "1":
            apiManagementMenu()
            break
        elif choice == "2":
            modelMenu()
            break
        elif choice == "3":
            break
        else:
            typer.echo("Invalid choice")
if __name__ == "__main__":
    app()
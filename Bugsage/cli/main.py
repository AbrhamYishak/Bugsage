import typer
from rich import print
from ..analyzer.parser import parser
from .response import ResponseFromatterBugsageCommunity,ResponseFromatterAI
from .bugsagecommunity import Upvote,Downvote
from .menu import apiManagementMenu
app = typer.Typer()  

@app.command()
def run(filename: str, ai: bool = False):
    """
    This tool use prev errors and provide explanation and possible fix
    """
    if ai:
        print("[bold red]Ai being used[/bold red]")
        Ai,result = parser(filename=filename,ai=True)
        ResponseFromatterAI(result)
        typer.echo("""Rate this result:\n    [up]👍 Helpful\n    [down]👎 Not Helpful\n    [Enter] Skip""")
        vote = input("> ").strip().lower()
    else:
        Ai,result = parser(filename)
        if not Ai:
            ResponseFromatterBugsageCommunity(result)
        else:
            ResponseFromatterAI(result)
        typer.echo("""Rate this result:\n    [up]👍 Helpful\n    [down]👎 Not Helpful\n    [Enter] Skip""")
        vote = input("> ").strip().lower()
        print(isinstance(result))
        id = result.json()[0].get('id')
        if vote == "up":
            Upvote(id)
        if vote == "down":
            Downvote(id)
@app.command()
def menu():
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
            # model_menu()
            print(2)
        elif choice == "3":
            break
        else:
            typer.echo("Invalid choice")
if __name__ == "__main__":
    app()
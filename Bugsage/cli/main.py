import typer
from rich import print
from ..analyzer.parser import parser
from .response import ResponseFromatterBugsageCommunity,ResponseFromatterAI
app = typer.Typer()  

@app.command()
def main(filename: str, ai: bool = False):
    """
    This tool use prev errors and provide explanation and possible fix
    """
    if ai:
        print("[bold red]Ai being used[/bold red]")
        Ai,result = parser(filename=filename,ai=True)
        ResponseFromatterAI(result)
        typer.echo("""Rate this result:\n    [up]👍 Helpful\n    [down]👎 Not Helpful\n    [Enter] Skip""")
        vote = input("> ").strip().lower()
        print(vote)
    else:
        Ai,result = parser(filename)
        if not Ai:
            ResponseFromatterBugsageCommunity(result)
        else:
            ResponseFromatterAI(result)
        typer.echo("""Rate this result:\n    [up]👍 Helpful\n    [down]👎 Not Helpful\n    [Enter] Skip""")
        vote = input("> ").strip().lower()
        print(vote)
if __name__ == "__main__":
    app()
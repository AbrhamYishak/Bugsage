import typer
from rich import print
from ..analyzer.parser import parser
app = typer.Typer()  

@app.command()
def main(filename: str, ai: bool = False):
    """
    This tool use prev errors and provide explanation and possible fix
    """
    if ai:
        print("[bold red]Ai being used[/bold red]")
        parser(filename=filename,ai=True)
    else:
        parser(filename)


if __name__ == "__main__":
    app()
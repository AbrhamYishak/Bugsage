import typer
from ..analyzer.parser import parser
app = typer.Typer()  

@app.command()
def main(filename: str, ai: bool = False):
    """
    This tool use prev errors and provide explanation and possible fix
    """
    if ai:
        print("ai wanted to be used")
    parser(filename)


if __name__ == "__main__":
    app()
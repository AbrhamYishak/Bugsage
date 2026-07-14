from rich import print
from .bugsagecommunity import Upvote,Downvote,AiToBugsageCommunity,next,prev
import typer
def ResponseFromatterBugsageCommunity(response):
    responseCode = response.status_code
    responseResults = response.json()['results']
    prevpresent = response.json()['previous']
    if responseCode== 200:
        print("[bold green]Successful [/bold green]")  
        print(responseResults)
    typer.echo(f"""Rate this result:\n    [u]👍 Helpful\n    [d]👎 Not Helpful\n    [n] Next Response\n    {"[p] Previous Response\n    " if prevpresent else ""}[Enter] Skip""")
    vote = input("> ").strip().lower()
    id = response.json()['results'][0].get('id')
    if vote == 'u':
        Upvote(id)
    elif vote == 'd':
        Downvote(id)
    elif vote == 'n':
        nextresponse = next(response)
        ResponseFromatterBugsageCommunity(nextresponse)
    elif vote == 'p':
        prevresponse = prev(response)
        ResponseFromatterBugsageCommunity(prevresponse)
def ResponseFromatterAI(response,status):
    if not status:
        print(f"[bold red] {response} [/bold red]")
    else:
        print(response)
from rich import print
from Bugsage.cli.bugsagecommunity import Upvote,Downvote,next,prev
from Bugsage.templates.reponse import formatResponse
from Bugsage.exceptions import NextPageError, PrevPageError
import typer
def ResponseFromatterBugsageCommunity(response):
    responseCode = response.status_code
    responseResults = response.json()['results']
    prevpresent = response.json()['previous']
    if responseCode== 200:
        print()
        print("[bold green]Successful [/bold green]")  
        formatResponse(responseResults)
    typer.echo(f"""Rate this result:\n    [u]👍 Helpful\n    [d]👎 Not Helpful\n    [n] Next Response\n    {"[p] Previous Response\n    " if prevpresent else ""}[Enter] Skip""")
    vote = input("> ").strip().lower()
    id = response.json()['results'][0].get('id')
    if vote == 'u':
        Upvote(id)
    elif vote == 'd':
        Downvote(id)
    elif vote == 'n':
        try:
            nextresponse = next(response)
            ResponseFromatterBugsageCommunity(nextresponse)
        except NextPageError as e:
            print(e)
    elif vote == 'p':
        try:
            prevresponse = prev(response)
            ResponseFromatterBugsageCommunity(prevresponse)
        except PrevPageError as e:
            print(e)
def ResponseFromatterAI(response,status):
    if not status:
        print(f"[bold red] {response} [/bold red]")
    else:
        print(response)
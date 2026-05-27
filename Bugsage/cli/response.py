from rich import print
def ResponseFromatter(response):
    responseCode = response.status_code
    response = response.json()
    if responseCode== 200:
        print("[bold green]Successful [/bold green]")  
        print(response)
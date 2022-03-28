# ? Choose subreddit method
from cmd import PROMPT
from time import sleep
from functions.RedditReqScrapper import reddit_req_scrapper

# Cool Terminal Colors
from rich import print


def subreddit_prompt():
    subreddit = PROMPT.ask(
        ">> [blue]Choose a subreddit?[/blue]", default="AbruptChaos")

    attempts = 10

    while attempts >= 0:
        if reddit_req_scrapper(subreddit):
            print(">> [bold green]See ya later![/bold green]")
            break
        else:
            print(f'>> Trying again. ({str(attempts)} attempts left)\n')

            timeout = 3
            while timeout > 0:
                print(f'>> [italic]Trying again in[/italic] {str(timeout)}.')
                sleep(1)
                timeout -= 1
            attempts -= 1
    else:
        print('\n>> [bold red]Enough trying, we have a problem![/bold red]')

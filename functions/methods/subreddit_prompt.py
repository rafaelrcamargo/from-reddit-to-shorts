"""FRTS"""

# ? Choose subreddit method
from time import sleep

# Cool Terminal Colors
from rich import print
from rich.prompt import Prompt

from functions.reddit_request import reddit_request


def subreddit_prompt():
    """Subreddit prompt"""

    subreddit = Prompt.ask(">> [blue]Choose a subreddit?[/blue]", default="AbruptChaos")

    attempts = 10

    while attempts >= 0:
        if reddit_request(subreddit):
            print(">> [bold green]See ya later![/bold green]")
            break
        else:
            print(f"\n>> Trying again. ({str(attempts)} attempts left)")

            timeout = 3
            while timeout > 0:
                print(f">> [italic]Trying again in[/italic] {str(timeout)}.")
                sleep(1)
                timeout -= 1
            attempts -= 1
    else:
        print("\n>> [bold red]Enough trying, we have a problem![/bold red]")

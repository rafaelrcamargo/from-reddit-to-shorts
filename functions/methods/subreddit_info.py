"""Subreddits list method"""

# Cool Terminal Colors
from rich import print

# Custom functions
from functions.reddit_request import reddit_request
from functions.utils.separator import separator
from functions.utils.timeout import timeout


def subreddit_info(subreddit):
    """Requesting the subreddit data"""

    print(f">> [blue]Scrapping [bold]{subreddit}[/bold]...[/blue]\n")
    attempts = 10
    while attempts >= 0:
        # ? Requesting the subreddit data
        req_resp = reddit_request(subreddit)

        # ! Error in request response
        if req_resp is not None:
            return req_resp
        else:
            print(f">> Trying again. ({str(attempts)} attempts left)")
            timeout(3, 1, "request")
            print("\n", separator(), "\n")
            attempts -= 1

    print(">> [bold red]Enough trying, we have a problem![/bold red]")
    print("\n", separator(), "\n")

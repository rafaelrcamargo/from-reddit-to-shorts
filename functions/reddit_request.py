"""Reddit request"""

# Cool Terminal Colors
from rich import print

# Requests
from functions.api_request import api_request


def reddit_request(subreddit):
    """Requesting the subreddit data"""

    # Making a get request
    response = api_request(subreddit)

    if response.status_code == 200:
        return response

    print(f"\n>> [red]Error [bold]{response.status_code}![/bold][/red]")
    return None

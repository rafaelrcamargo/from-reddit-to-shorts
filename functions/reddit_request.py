"""Reddit request"""

# Cool Terminal Colors
from rich import print

# HTTP Req
import requests


def reddit_request(subreddit):
    """Requesting the subreddit data"""

    # Making a get request
    response = requests.get("https://www.reddit.com/r/" + subreddit + "/hot/.json", headers={"User-agent": "your bot 0.1"})

    if response.status_code == 200:
        return response

    print(f">> [red]Error [bold]{response.status_code}![/bold][/red]")
    return None

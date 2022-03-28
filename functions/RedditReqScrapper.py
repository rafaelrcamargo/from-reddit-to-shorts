# ? Main - Requests + Reddit Scrapper
from functions.ApiRequest import api_request

# Cool Terminal Colors
from rich import print


def reddit_req_scrapper(subreddit):
    # Making a get request
    r = api_request(subreddit)

    if r.status_code == 200:
        return r
    else:
        print(f'\n>> [red]Error [bold]{r.status_code}![/bold][/red]')
        return False

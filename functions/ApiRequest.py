# FRTS
# ? Reddit Api + Downloader

# * Imports
# HTTP Req
import requests

# Cool Terminal Colors
from rich import print


def api_request(subreddit):
    # Making a get request
    r = requests.get('https://www.reddit.com/r/' + subreddit + '/hot/.json')
    print("\n>>", r.status_code, "\n")
    return r

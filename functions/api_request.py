"""Reddit api request"""

# * Imports
# HTTP Req
import requests


def api_request(subreddit):
    """Reddit api requester"""

    # Making a get request
    response = requests.get("https://www.reddit.com/r/" + subreddit + "/hot/.json")
    return response

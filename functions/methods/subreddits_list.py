"""Subreddits list method"""

# ? Subreddits list method
from time import sleep

# Cool Terminal Colors
from rich import print

# Custom functions
from functions.bake_video import bake_video
from functions.reddit_request import reddit_request
from functions.reddit_scrapper import reddit_scrapper


def subreddits_list(subreddit):
    """Requesting the subreddit data"""

    print(f"\n>> [blue]Scraping [bold]{subreddit}[/bold]...[/blue]")
    attempts = 10
    while attempts >= 0:
        # ? Requesting the subreddit data
        req_resp = reddit_request(subreddit)

        # ! Error in request response
        if req_resp is not None:
            # * Scrapping video
            video_location = reddit_scrapper(req_resp)

            # ! Error in video scraping
            if video_location is False or video_location is None:
                break

            return bake_video(video_location, subreddit)
        else:
            print(f"\n>> Trying again. ({str(attempts)} attempts left)")
            timeout = 3
            while timeout > 0:
                print(f">> [italic]Trying again in[/italic] {str(timeout)}.")
                sleep(timeout)
                timeout -= 1
            attempts -= 1
    print("\n>> [bold red]Enough trying, we have a problem![/bold red]")

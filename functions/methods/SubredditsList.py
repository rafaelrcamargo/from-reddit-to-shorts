# ? Subreddits list method
import json
from time import sleep
from functions.BakeVideo import bake_video

from functions.RedditReqScrapper import reddit_req_scrapper
from functions.RedditScraper import reddit_scraper

# Cool Terminal Colors
from rich import print


def subreddits_list(subreddit):
    print(f'\n>> [blue]Scraping [bold]{subreddit}[/bold]...[/blue]')
    attempts = 10
    while attempts >= 0:
        req_resp = reddit_req_scrapper(subreddit)

        if req_resp != False:
            video_location = reddit_scraper(req_resp)

            if video_location != False:
                return bake_video(video_location, subreddit)
            else:
                print('>> [bold red]Error![/bold red]')
                return False
        else:
            print(f'>> Trying again. ({str(attempts)} attempts left)\n')

            timeout = 3
            while timeout > 0:
                print(
                    f'>> [italic]Trying again in[/italic] {str(timeout)}.')
                sleep(1)
                timeout -= 1
            attempts -= 1
    else:
        print(
            '\n>> [bold red]Enough trying, we have a problem![/bold red]')

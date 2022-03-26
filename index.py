
# FRTS
# ? Reddit Api + Downloader

# * Imports
# Delay
from time import sleep
# Datetime
from datetime import datetime

# OS
import os
# JSON
import json
# Path
from pathlib import Path

# Cool Terminal Colors
from rich import print
# Cool Prompt
from rich.prompt import Prompt

# Api request
from functions.ApiRequest import api_request
# Reddit scraper
from functions.RedditScraper import reddit_scraper

# Uploads
from functions.uploads.instagram.InstagramUpload import instagram_upload
from functions.uploads.youtube.YouTubeUpload import youtube_upload

# Remove SIG Error
from signal import signal, SIGPIPE, SIG_DFL
# Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
signal(SIGPIPE, SIG_DFL)

"""
* * * Starting dialog * * *
"""

print("\n--- [yellow]FR[/yellow][bold red]TS[/bold red] - [bold]From Reddit to Shorts[/bold] ---")
print("\nA simple script to scrape reddit content,")
print("and turn it into shorts content.\n")

"""
* * * Functions * * *
"""


# ? Main - Requests + Reddit Scrapper
def main(subreddit):
    # Making a get request
    r = api_request(subreddit)

    if r.status_code == 200:
        reddit_scraper(r)
        return True
    else:
        print('>> [bold red]Error![/bold red]')
        return False


# ? Choose subreddit method
def subreddit_promt():
    subreddit = Prompt.ask(
        ">> [blue]Choose a subreddit?[/blue]", default="AbruptChaos")

    attempts = 10

    while attempts >= 0:
        if main(subreddit):
            print(">> [bold green]See ya later![/bold green]")
            break
        else:
            print('>> Trying again. (' +
                  str(attempts) + ' attempts left)\n')

            timeout = 3
            while timeout > 0:
                print('>> [italic]Trying again in[/italic] ' +
                      str(timeout) + '.')
                sleep(1)
                timeout -= 1
            attempts -= 1
    else:
        print('>> [bold red]Enough trying, we have a problem![/bold red]')


# ? Subreddits list method
def subreddits_list():
    # Opening JSON file
    f = open('subreddits.json')
    subreddits = json.load(f)

    for subreddit in subreddits['list']:
        print('>> [blue]Scraping [bold]' + subreddit + '[/bold]...[/blue]')
        attempts = 10
        while attempts >= 0:
            if main(subreddit):
                print(">> [bold green]See ya later![/bold green]")
                break
            else:
                print('>> Trying again. (' +
                      str(attempts) + ' attempts left)\n')

                timeout = 3
                while timeout > 0:
                    print('>> [italic]Trying again in[/italic] ' +
                          str(timeout) + '.')
                    sleep(1)
                    timeout -= 1
                attempts -= 1
        else:
            print(
                '\n>> [bold red]Enough trying, we have a problem![/bold red]\n')
    else:
        # Closing file
        f.close()

        # Uploads
        # instagram_upload()
        youtube_upload()


"""
* * * Main loop * * *
"""

while True:
    if os.path.exists(str(Path(__file__).cwd()) + "/assets/build/" + datetime.today().strftime('%d_%m_%Y')) == False:
        subreddits_list()
    else:
        print("\n>> [bold yellow]Done for today, waiting![/bold yellow]")
        total = 3600
        while total > 0:
            print("\n>> [red]Waiting for the next day![/red]")
            print(">> [red]Time left: " + str(total) + " seconds[/red]")
            sleep(60)
            total -= 60

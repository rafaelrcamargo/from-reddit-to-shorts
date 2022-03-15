# FRTS
# ? Reddit Api + Downloader

# * Imports
# Delay
import json
from time import sleep
# Cool Terminal Colors
from rich import print
# Cool Prompt
from rich.prompt import Prompt

# Api request
from functions.ApiRequest import api_request
# Reddit scraper
from functions.RedditScraper import reddit_scraper
from functions.uploads.instagram.InstagramUpload import instagram_upload

print("\n--- [yellow]FR[/yellow][bold red]TS[/bold red] - [bold]From Reddit to Shorts[/bold] ---")
print("\nA simple script to scrape reddit content,")
print("and turn it into shorts content.\n")


def main():
    # Making a get request
    r = api_request(subreddit)

    if r.status_code == 200:
        reddit_scraper(r)
        return True
    else:
        print('>> [bold red]Error![/bold red]')
        return False


# ? Choose subreddit prompt
""" subreddit = Prompt.ask(
    ">> [blue]Choose a subreddit?[/blue]", default="AbruptChaos")

attempts = 10

while attempts >= 0:
    if main():
        print(">> [bold green]See ya later![/bold green]\n")
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
"""

# ? Subreddits list scrapping
# Opening JSON file
f = open('subreddits.json')
subreddits = json.load(f)

for subreddit in subreddits['list']:
    print('>> [blue]Scraping [bold]' + subreddit + '[/bold]...[/blue]')
    attempts = 10
    while attempts >= 0:
        if main():
            print(">> [bold green]See ya later![/bold green]\n")
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
        print('\n>> [bold red]Enough trying, we have a problem![/bold red]\n')
else:
    # Closing file
    f.close()
    instagram_upload()

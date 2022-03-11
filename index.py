# FRTS
# ? Reddit Api + Downloader

# * Imports
# Requests
import requests
# Reddit downloader
from functions.RedditDownloader import reddit_downloader

# Cool Terminal Colors
from rich import print

print("\n--- [yellow]FR[/yellow][bold red]TS[/bold red] - [bold]From Reddit to Shorts[/bold] ---")
print("\nA simple script to scrape reddit content,")
print("and turn it into shorts content.\n")
subreddit = input("Choose a subreddit: ")

# Making a get request
r = requests.get('https://www.reddit.com/r/Unexpected/hot/.json')

print("\n>>", r.status_code, "\n")

duration = 0

if r.status_code == 200:
    posts = r.json()['data']['children']
    for post in posts:
        if post['data']['secure_media'] is not None:
            duration += int(post['data']['secure_media']
                            ['reddit_video']['duration'])
            print(">> [bold]Total Duration:[/bold]", duration, "seconds\n")

            url = post['data']['permalink']
            reddit_downloader(url)
            print("--- [yellow]FR[/yellow][bold red]TS[/bold red] --- [yellow]FR[/yellow][bold red]TS[/bold red] --- [yellow]FR[/yellow][bold red]TS[/bold red] ---\n")


else:
    print('>> [bold red]Api Error![/bold red]')
    print('>> [bold]Try Again Later.[/bold]\n')

# FRTS
# ? Reddit Api + Downloader

# * Imports
# Cool Terminal Colors
from datetime import datetime
from pathlib import Path
from rich import print
from rich.prompt import Prompt
from functions.BakeVideo import bake_video

# Reddit Downloader
from functions.RedditDownloader import reddit_downloader

# FRTS "Transition"
transition = "--- [yellow]FR[/yellow][bold red]TS[/bold red] --- [yellow]FR[/yellow][bold  red]TS[/bold red] --- [yellow]FR[/yellow][bold red]TS[/bold red] ---\n"

duration = 0


def reddit_scraper(r):
    global duration

    posts = r.json()['data']['children']
    for post in posts:
        try:
            # Post url
            url = post['data']['permalink']
            # Downloading
            if reddit_downloader(url, duration) == False:
                break
            else:
                print(transition)

        except AttributeError:
            print("Error!\n")

    isBuild = Prompt.ask(">> [blue]Do you want to build the video?", choices=[
                         "Yes", "No"], default="Yes")
    if isBuild == "Yes":
        print("\n>> [bold blue]Building the video...[/bold blue]")
        bake_video(str(Path(__file__).cwd()) + "\\assets\\videos\\" +
                   post['data']['subreddit'] + "\\" + datetime.today().strftime('%d-%m-%Y'), post['data']['subreddit'], duration)

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


def reddit_scraper(r):
    posts = r.json()['data']['children']
    for post in posts:
        try:
            # Post url
            url = post['data']['permalink']
            # Downloading
            if reddit_downloader(url) == False:
                break
            else:
                print(transition)

        except AttributeError:
            print("Error!\n")

    # Optional baking prompt
    """ isBuild = Prompt.ask(">> [blue]Do you want to build the video?", choices=[
                         "Yes", "No"], default="Yes")
    if isBuild == "Yes": """

    print(">> [bold blue]Building the video...[/bold blue]")
    bake_video(str(Path(__file__).cwd()) + "\\assets\\videos\\" +
               post['data']['subreddit'] + "\\" + datetime.today().strftime('%d_%m_%Y'), post['data']['subreddit'])

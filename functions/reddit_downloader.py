"""Reddit video downloader"""

# * Imports
# Sys os
import os

# Sys Path
from pathlib import Path

# Date
from datetime import datetime

# Reddit Downloader
from redvid import Downloader

# Cool Terminal Colors
from rich import print

from functions.utils.separator import separator

DURATION = 0


def reddit_downloader(post):
    """Reddit downloader"""

    global DURATION

    path = (
        str(Path(__file__).cwd())
        + "/assets/videos/"
        + post.split("/")[2]
        + "/"
        + datetime.today().strftime("%d_%m_%Y")
    )

    path_exists = os.path.exists(path)

    if DURATION >= 40:
        # * General Stats
        print("\n>> [green]We already have enough videos![/green]")
        print(">> [bold yellow]Let's build it?[/bold yellow]\n")
        return False

    if not path_exists:
        DURATION = 0
        os.makedirs(path)
        print(">> [italic blue]The new directory is created![/italic blue]")

    print(separator(21))
    print()

    # * Basics
    # Redvid setup
    reddit = Downloader()
    # Video path
    reddit.path = path
    # Video url
    reddit.url = "https://www.reddit.com" + post + "_/"

    # * Props
    # Auto max video quality based on the file size
    reddit.auto_max = True
    reddit.max = "1080p"

    # Video overwrite method
    reddit.overwrite = True

    try:
        # * Get Videos Stats
        reddit.check()

        DURATION += int(reddit.duration)

        # * General Stats
        print("\n>> [bold yellow]General Stats:[/bold yellow]")
        print(f"- Duration: [bold blue]{str(DURATION)}[/bold blue] seconds")

        # * Video Stats
        print("\n>> [bold blue]Video Stats:[/bold blue]")
        print(f"- Duration: [blue]{str(reddit.duration)}[/blue] seconds")
        print(f"- Size: [blue]{str(reddit.size)}[/blue] bytes\n")

        # * Downloading
        if reddit.duration < 20 and reddit.duration > 2:
            reddit.download()
            print("\n>> [green]Video downloaded![/green]")
        else:
            print(">> [red]Not that good for shorts! [bold]:([/bold][/red]")

        return True
    except:
        print("\n>> [red]Video not found![/red]")
        return None

"""Reddit video downloader"""

# * Imports
# Sys os
import os

# Date
from datetime import datetime

# Sys Path
from pathlib import Path

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
        + "/temp/videos/"
        + post.split("/")[2]
        + "/"
        + datetime.today().strftime("%d_%m_%Y")
    )

    path_exists = os.path.exists(path)

    if not path_exists:
        DURATION = 0
        os.makedirs(path)
        print(">> [blue]The new directory was created successfully![/blue]\n")

    if DURATION >= 30:
        # * General Stats
        print(">> [bold green]We already have enough videos![/bold green]")
        print(">> [italic yellow]Let's build it?[/italic yellow]\n")
        return False

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

        # * Downloading
        if reddit.duration < 10 and reddit.duration > 1:
            DURATION += int(reddit.duration)

            # * Video Stats
            print("\n>> [bold blue]Video Stats:[/bold blue]")
            print(f"- Duration: [blue]{str(reddit.duration)}[/blue] seconds")
            print(f"- Size: [blue]{str(reddit.size)}[/blue] bytes\n")

            # * General Stats
            print("\n>> [bold yellow]General Stats:[/bold yellow]")
            print(f"- Duration: [bold blue]{str(DURATION)}[/bold blue] seconds")

            reddit.download()
            print("\n>> [blink green]Video downloaded![/blink green]\n")
            print(separator(), "\n")
            return True
        else:
            print("\n>> [red]Not that good for shorts! [bold]:([/bold][/red]")
            return None

    except:
        print("\n>> [red]Video not found![/red]")
        return None

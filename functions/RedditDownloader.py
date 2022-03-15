# FRTS
# ? Reddit Api + Downloader

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

duration = 0


def reddit_downloader(post):
    global duration

    path = str(Path(__file__).cwd()) + "\\assets\\videos\\" + \
        post.split("/")[2] + "\\" + datetime.today().strftime('%d_%m_%Y')

    isExist = os.path.exists(path)
    if not isExist:
        duration = 0
        os.makedirs(path)
        print(">> [italic blue]The new directory is created![/italic blue]\n")

    # * Basics
    # Redvid setup
    reddit = Downloader()
    # Video path
    reddit.path = path
    # Video url
    reddit.url = 'https://www.reddit.com' + post + '_/'

    # * Props
    # Auto max video quality based on the file size
    reddit.auto_max = True
    reddit.max = '1080p'

    # Video overwrite method
    reddit.overwrite = True

    try:
        # * Get Videos Stats
        reddit.check()

        duration += int(reddit.duration)

        if duration <= 40:
            # * General Stats
            print("\n>> [bold yellow]General Stats:[/bold yellow]")
            print("- Duration: [bold blue]" +
                  str(duration) + "[/bold blue] seconds")

            # * Video Stats
            print("\n>> [bold blue]Video Stats:[/bold blue]")
            print("- Duration: [blue]" +
                  str(reddit.duration) + "[/blue] seconds")
            print("- Size: [blue]" + str(reddit.size) + "[/blue] bytes\n")

            # * Downloading
            if reddit.duration < 20 and reddit.duration > 2 and reddit.size <= 24 * (1 << 20):
                reddit.download()
                print('\n>> [green]Video downloaded![/green]\n')
            else:
                print(
                    '>> [red]Not that good for shorts![/red] [red bold]:([/red bold]\n')

            return True
        else:
            # * General Stats
            print("\n>> [bold yellow]General Stats:[/bold yellow]")
            print("- Duration: [bold blue]" +
                  str(duration) + "[/bold blue] seconds\n")
            print('>> [green]We already have enough videos![/green]')
            print('>> [bold yellow]Let\'s build it?[/bold yellow]\n')
            return False
    except:
        print('\n>> [red]Video not found![/red]\n')

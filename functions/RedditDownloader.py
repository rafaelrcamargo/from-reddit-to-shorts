# FRTS
# ? Reddit Api + Downloader

# * Imports
# Sys Path
from pathlib import Path
# Reddit Downloader
from redvid import Downloader

# Cool Terminal Colors
from rich import print


def reddit_downloader(post):
    # * Basics
    # Redvid setup
    reddit = Downloader()
    # Video path
    reddit.path = str(Path(__file__).cwd()) + "\\videos"
    # Video url
    reddit.url = 'https://www.reddit.com' + post + '_/'

    # * Defs
    # Max size of the file in MB
    reddit.max_s = 24 * (1 << 20)

    # * Props
    # Auto max video quality based on the file size
    reddit.auto_max = True
    # Video overwrite method
    reddit.overwrite = True

    # * Get Videos Stats
    reddit.check()

    # * Video Stats
    print("\n>> [bold blue]Stats:[/bold blue]")
    print("- Duration: [blue]" + str(reddit.duration) + "[/blue] seconds")
    print("- Size: [blue]" + str(reddit.size) + "[/blue] bytes\n")

    # * Downloading
    if reddit.duration < 90 and reddit.duration > 8 and reddit.size <= 24 * (1 << 20):
        reddit.download()
        print('\n>> [green]Video downloaded![/green]\n')
    else:
        print('\n>> [red]Video too long, not that good for shorts![/red] :(\n')

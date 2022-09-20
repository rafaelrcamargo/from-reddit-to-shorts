"""Reddit scraper"""

# * Imports
# Cool Terminal Colors
from datetime import datetime
from pathlib import Path
from rich import print

# Reddit Downloader
from functions.reddit_downloader import reddit_downloader

# FRTS "Transition"
TRANSITION = "--- [yellow]FR[/yellow][bold red]TS[/bold red] "
TRANSITION += "--- [yellow]FR[/yellow][bold red]TS[/bold red] "
TRANSITION += "--- [yellow]FR[/yellow][bold red]TS[/bold red] ---"


def reddit_scrapper(response):
    """Reddit scrapping"""

    posts = response.json()["data"]["children"]
    for post in posts:
        if (
            post.get("data") is not None
            and post.get("data")["is_video"] is True
            and post["data"].get("secure_media") is not None
        ):
            try:
                # Post url
                url = post["data"]["permalink"]
                # Downloading
                download_status = reddit_downloader(url)

                if download_status is None:
                    print(f">> [red]Error downloading [bold]{url}[/bold]")
                elif download_status is False:
                    print(TRANSITION)
                    return (
                        str(Path(__file__).cwd())
                        + "/temp/videos/"
                        + post["data"]["subreddit"]
                        + "/"
                        + datetime.today().strftime("%d_%m_%Y")
                    )
            except AttributeError:
                print("Error!\n")

    return None

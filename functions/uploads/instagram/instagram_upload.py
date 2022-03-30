"""Instagram upload"""

# * Imports
# System
from datetime import datetime
import os

# Dir Path
from pathlib import Path

# Regex
import re

# Sleep
from time import sleep

# .env file
from dotenv import load_dotenv

# Instagram API
from instagrapi import Client

# Cool Terminal Colors
from rich import print

build_path = (
    str(Path(__file__).cwd()) + "/assets/build/" + datetime.today().strftime("%d_%m_%Y")
)


def instagram_upload():
    """Instagram uploader"""

    load_dotenv()

    USERNAME = os.getenv("INSTAGRAM_USERNAME")
    PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    cl = Client()
    cl.login(USERNAME, PASSWORD)

    filenames = next(os.walk(build_path), (None, None, []))[2]

    print(
        "\n>> [yellow]Success logging in[/yellow], starting the [blue]uploads![/blue]"
    )

    for filename in filenames:
        if filename.split(".")[1] == "jpg":
            name = filename.split(".")[0]
            subreddit = "r/" + filename.split("_")[0]
            title = " ".join(re.findall("[A-Z][^A-Z]*", filename.split("_")[0]))

            print(f"\n>> Name: {name}")
            print(f">> Subreddit: {subreddit}")
            print(f">> Title: {title}")

            media = cl.clip_upload(
                path=build_path + "/" + name + ".mp4",
                caption=title
                + " ("
                + subreddit
                + ") - trending goes brrr #reels\n\n\n#Entertainment #fun #funny   #comedy #meme #trending #memes #nonsense #reddit #viral #reel",
                thumbnail=build_path + "/" + name + ".jpg",
                extra_data={
                    "custom_accessibility_caption": "reels Entertainment fun funny comedy meme trending memes nonsense reddit viral reel",
                    "like_and_view_counts_disabled": 1,
                    "disable_comments": 1,
                },
            )

            print(media)
            if media is not None:
                print("\n>> [blue]Uploaded![/blue]")
        else:
            total = 3600
            while total > 0:
                print("\n>> [red]Waiting for the next upload![/red]")
                print(f">> [red]Time left: {str(total)} seconds[/red]")
                sleep(60)
                total -= 60
    else:
        print("\n>> [italic green]All upload done![/italic green] 🥳")

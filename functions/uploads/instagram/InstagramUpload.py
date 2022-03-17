# FRTS
# ? Reddit Api + Downloader

# * Imports
# System
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

build_path = str(Path(__file__).cwd()) + "\\assets\\build"


def instagram_upload():
    load_dotenv()

    USERNAME = os.getenv("INSTAGRAM_USERNAME")
    PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

    cl = Client()
    cl.login(USERNAME, PASSWORD)

    filenames = next(os.walk(build_path), (None, None, []))[2]

    print(">> [yellow]Successful login, starting the uploads![/yellow]")

    for filename in filenames:
        if filename.split(".")[1] == "jpg":
            name = filename.split(".")[0]
            subreddit = "r/" + filename.split("_")[0]
            title = " ".join(re.findall(
                '[A-Z][^A-Z]*', filename.split("_")[0]))

            print("\n>> Name: " + name)
            print(">> Subreddit: " + subreddit)
            print(">> Title: " + title)

            media = cl.clip_upload(
                path=build_path + "\\" + name + ".mp4",
                caption=title +
                " (" + subreddit + ") - trending goes brrr #reels\n\n\n#Entertainment #fun #funny   #comedy #meme #trending #memes #nonsense #reddit #viral #reel",
                thumbnail=build_path + "\\" + name + ".jpg",
                extra_data={
                    "custom_accessibility_caption": "fun funny comedy meme trending memes Entertainment     nonsense reddit viral reel reels",
                    "like_and_view_counts_disabled": 1,
                    "disable_comments": 1,
                }
            )

            print(media)
            if media is not None:
                print("\n>> [blue]Uploaded![/blue]")
        else:
            sleep(120)
    else:
        print("\n>> [italic green]All upload done![/italic green] 🥳")
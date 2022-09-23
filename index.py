"""
FRTS - From Reddit To Shorts

A fully automated project that loops over a list of the TOP video subreddits, and transforms the content into various formats, then uploads it.

- - - - - - - - - - - - - - - - TODOs - - - - - - - - - - - - - - - -

TODO: Think about a plataform agnostic CTA.
TODO: Fast paced videos, think about a way to make them more dynamic.
TODO: Create a system for longer videos, 4+ minutes. (16:9)

TODO: Add a way to upload to Instagram.
TODO: Add a way to upload to Twitter.
TODO: Add a way to upload to TikTok.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

Author: @rafaelrcamargo
"""

import json

# Base
import os
import shutil

# Misc
from datetime import datetime
from pathlib import Path
from time import sleep

from rich import print

# Logs
from rich.console import Console

from functions.bake_video import bake_video

# Methods
from functions.methods.subreddit_info import subreddit_info
from functions.reddit_scrapper import reddit_scrapper

# Plataforms
from functions.uploads.youtube.youtube_upload import youtube_upload

# Utils
from functions.utils.separator import separator
from functions.utils.timeout import timeout

# Constants
DATE = datetime.today().strftime("%d_%m_%Y")

# * Greeting dialog
dialogs = (
    "\n" + separator(),
    f"\n{separator(3)} [yellow]FR[/yellow][bold red]TS[/bold red] - [bold]From Reddit to Shorts[/bold] {separator(3)}\n",
    "A fully automated project that loops over a list of the TOP video subreddits,",
    "and transforms the content into various formats, then uploads it. :smile:",
    "\n" + separator() + "\n",
)

console = Console(width=80)
for dialog in dialogs:
    console.print(dialog, justify="center")

# * Main loop
def main():
    """Main loop"""
    while True:
        if not os.path.exists(f"{str(Path(__file__).cwd())}/temp/build/{DATE}"):
            # Opening JSON file
            subreddits_file = open("subreddits.json", encoding="utf-8")
            subreddits = json.load(subreddits_file)

            for subreddit in subreddits["list"]:
                # * Methods
                # subreddit_prompt()
                info = subreddit_info(subreddit)

                # ! Error in info scrapping
                if info is False or info is None:
                    continue

                # * Scrapping video
                videos = reddit_scrapper(info)

                # ! Error in video scrapping
                if videos is False or videos is None:
                    continue

                final = bake_video(videos, subreddit)

                if bool(final):
                    youtube_upload(final)

                    try:
                        shutil.rmtree(f"{str(Path(__file__).cwd())}/temp/videos")
                    except FileNotFoundError:
                        pass

                    timeout(14400, 1800, "upload")
                else:
                    print(">> [bold red]Error, no such video![/bold red]")

            # Closing file
            subreddits_file.close()
        else:
            print(">> [bold yellow]Done for today.[/bold yellow]")
            timeout(14400, 1800, "day")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # ? Delete temp folder
        print("\n", separator(), "\n")
        with console.status(
            "[bold red]Exiting...[/bold red]\n", spinner="moon"
        ) as status:
            if os.path.exists(f"{str(Path(__file__).cwd())}/temp"):
                print(">> [bold red]Deleting temp folder...[/bold red]")
                for file in os.listdir(f"{str(Path(__file__).cwd())}/temp"):
                    print(f">>> [bold red]Deleting {file}...[/bold red]")
                    shutil.rmtree(f"{str(Path(__file__).cwd())}/temp/{file}")
                    sleep(1)

                os.rmdir(f"{str(Path(__file__).cwd())}/temp")

        # * Exit
        print(
            "\n>> Exiting [bold]without [red]errors[/red], [green]temps[/green] deleted[/bold], Seya! :wave:\n"
        )
        pass

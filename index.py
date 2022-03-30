"""FRTS - From reddit to shorts"""

# * Imports
# Delay
import json
from time import sleep

# Datetime
from datetime import datetime

# OS
import os

# Path
from pathlib import Path

# Cool Terminal Colors
from rich import print

# Methods
from functions.methods.subreddits_list import subreddits_list
from functions.methods.subreddit_prompt import subreddit_prompt

# Uploads
from functions.uploads.instagram.instagram_upload import instagram_upload
from functions.uploads.youtube.youtube_upload import youtube_upload
from functions.utils.separator import separator

# Remove SIG Error
# from signal import signal, SIGPIPE, SIG_DFL
# Ignore SIG_PIPE and don't throw exceptions on it... (http://docs.python.org/library/signal.html)
# signal(SIGPIPE, SIG_DFL)

"""
* * * Starting dialog * * *
"""

print(separator(21))
print(
    "\n--- [yellow]FR[/yellow][bold red]TS[/bold red] - [bold]From Reddit to Shorts[/bold] ---"
)
print("\nA simple script to scrape reddit content,")
print("and turn it into shorts content.")
print(separator(21))

"""
* * * Main loop * * *
"""


def timeout(time, steps, action):
    total = time
    while total > 0:
        print(f"\n>> [red]Waiting for the next [bold]{action}[/bold]![/red]")
        print(f">> [red]Time left: {str(total)} seconds[/red]")
        sleep(steps)
        total -= steps


def main():
    while True:
        if (
            os.path.exists(
                str(Path(__file__).cwd())
                + "/assets/build/"
                + datetime.today().strftime("%d_%m_%Y")
            )
            == False
        ):
            # Opening JSON file
            f = open("subreddits.json")
            subreddits = json.load(f)

            for subreddit in subreddits["list"]:
                # * Methods
                # subreddit_prompt()
                video_path = subreddits_list(subreddit)

                if video_path != False and video_path != None:
                    youtube_upload(video_path)
                    timeout(60, 10, "upload")
                else:
                    print(">> [bold red]Error, no such video![/bold red]")
            else:
                # Closing file
                f.close()

        else:
            print("\n>> [bold yellow]Done for today, waiting![/bold yellow]")
            timeout(7200, 600, "day")


if __name__ == "__main__":
    main()

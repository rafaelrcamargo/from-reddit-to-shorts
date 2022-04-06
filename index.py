"""FRTS - From reddit to shorts"""

# * * * Imports * * *
# JSON files
import json

# Dates
from datetime import datetime

# Sys Paths
from pathlib import Path

# Os - For File System
import os

# Cool Terminal Colors
from rich import print

# Methods
from functions.methods.subreddits_list import subreddits_list
from functions.uploads.youtube.youtube_upload import youtube_upload

# Uploads
from functions.utils.separator import separator
from functions.utils.timeout import timeout

# * * * Constants * * *
DATE = datetime.today().strftime("%d_%m_%Y")

# * * * Starting dialog * * *
print(separator(21))
print(
    "\n--- [yellow]FR[/yellow][bold red]TS[/bold red] - [bold]From Reddit to Shorts[/bold] ---"
)
print("\nA simple script to scrape reddit content,")
print("and turn it into shorts content.")
print(separator(21))

# * * * Main loop * * *
def main():
    """Main loop"""
    while True:
        if not os.path.exists(f"{str(Path(__file__).cwd())}/assets/build/{DATE}"):
            # Opening JSON file
            subreddits_file = open("subreddits.json", encoding="utf-8")
            subreddits = json.load(subreddits_file)

            for subreddit in subreddits["list"]:
                # * Methods
                # subreddit_prompt()
                video_path = subreddits_list(subreddit)

                if bool(video_path):
                    youtube_upload(video_path)
                    timeout(10800, 1800, "upload")
                else:
                    print(">> [bold red]Error, no such video![/bold red]")

            # Closing file
            subreddits_file.close()

        else:
            print("\n>> [bold yellow]Done for today, waiting![/bold yellow]")
            timeout(14400, 1800, "day")


if __name__ == "__main__":
    main()

from datetime import datetime
import os
from pathlib import Path
import re
from time import sleep
from googleapiclient.http import MediaFileUpload

# Cool Terminal Colors
from rich import print

from functions.uploads.youtube.Google import Create_Service

CLIENT_SECRET_FILE = str(Path(__file__).cwd()) + \
    '/functions/uploads/youtube/client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

build_path = str(Path(__file__).cwd()) + "/assets/build/" + \
    datetime.today().strftime('%d_%m_%Y')

SEPARATOR = "\n"
for i in range(0, 18):
    if i % 2 == 0:
        SEPARATOR += "[red]-[/red] "
    else:
        SEPARATOR += "[yellow]-[/yellow] "


def youtube_upload(filename):
    print(
        "\n>> [yellow]Success logging in[/yellow], starting the [blue]upload![/blue]")

    if filename.split(".")[1] == "mp4":
        print(f"\n>> [yellow]File[/yellow]: {filename}")
        # get last item from array

        name = filename.split("/")[-1].split(".")[0]
        subreddit = "r/" + filename.split("/")[-1].split("_")[0]
        title = " ".join(re.findall(
            '[A-Z][^A-Z]*', filename.split("/")[-1].split("_")[0]))

        print(f"\n>> [bold]Name[/bold]: {name}")
        print(f">> [bold]Subreddit[/bold]: {subreddit}")
        print(f">> [bold]Title[/bold]: {title}")
        try:
            """ request_body = {
                    'snippet': {
                        'categoryId': 24,

                        'title': title + " (" + subreddit + ") - trending goes brrr #Shorts",

                        'description': title + " (" + subreddit + ") - trending goes brrr #Shorts\n\n\n#Entertainment, #fun, #funny, #comedy, #meme, #trending, #memes, #nonsense, #reddit, #viral, #reel.",

                        'tags': ['fun', 'funny', 'comedy', 'meme', 'trending', 'memes', 'Entertainment', 'nonsense', 'reddit', 'youtube', 'subscribe', 'viral', 'reel', 'reels', 'Shorts', 'Youtubeshorts']
                    },
                    'status': {
                        'privacyStatus': 'public',
                        'selfDeclaredMadeForKids': False,
                    },
                    'notifySubscribers': True
                }
                mediaFile = MediaFileUpload(
                    build_path + "/" + name + ".mp4")
                response_upload = service.videos().insert(
                    part='snippet,status',
                    body=request_body,
                    media_body=mediaFile
                ).execute()

                print("\n>> ", response_upload) """
            print("\n>> [blue]Uploaded![/blue]")
        except Exception as e:
            print(f"\n>> [red]Error: {str(e)}[/red]")
    else:
        print(SEPARATOR)
        print(
            f"\n>> [red]Why [bold]TF[/bold] is this file here?[/red]\n>> [red]File[/red]:{filename}")
        print(SEPARATOR)

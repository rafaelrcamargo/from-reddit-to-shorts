from datetime import datetime
import os
from pathlib import Path
import re
from time import sleep
from googleapiclient.http import MediaFileUpload

from functions.uploads.youtube.Google import Create_Service

CLIENT_SECRET_FILE = str(Path(__file__).cwd()) + \
    '\\functions\\uploads\\youtube\\client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

build_path = str(Path(__file__).cwd()) + "\\assets\\build"


def youtube_upload():
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

            request_body = {
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

            mediaFile = MediaFileUpload(build_path + "\\" + name + ".mp4")

            response_upload = service.videos().insert(
                part='snippet,status',
                body=request_body,
                media_body=mediaFile
            ).execute()

            service.thumbnails().set(
                videoId=response_upload.get('id'),
                media_body=MediaFileUpload(build_path + "\\" + name + ".jpg")
            ).execute()

            print("\n>> [blue]Uploaded![/blue]")
            os.remove(build_path + "\\" + name + ".mp4")
            os.remove(build_path + "\\" + name + ".jpg")
            print(
                "\n>> [green]Video + Thumb removed, ready for another![/green]")
        else:
            sleep(1800)
    else:
        print("\n>> [italic green]All upload done![/italic green] 🥳")

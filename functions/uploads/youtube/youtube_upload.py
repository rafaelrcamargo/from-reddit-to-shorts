from datetime import datetime
from pathlib import Path
import re
from googleapiclient.http import MediaFileUpload

# Cool Terminal Colors
from rich import print

from functions.uploads.youtube.google import Create_Service
from functions.utils.separator import separator

CLIENT_SECRET_FILE = (
    str(Path(__file__).cwd()) + "/functions/uploads/youtube/client_secret.json"
)
API_NAME = "youtube"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

build_path = (
    str(Path(__file__).cwd()) + "/assets/build/" + datetime.today().strftime("%d_%m_%Y")
)


def youtube_upload(filename):
    print("\n>> [yellow]Success logging in[/yellow], starting the [blue]upload![/blue]")

    if filename.split(".")[1] == "mp4":
        print(f"\n>> [yellow]File[/yellow]: {filename}")
        # get last item from array

        name = filename.split("/")[-1].split(".")[0]
        subreddit = "r/" + filename.split("/")[-1].split("_")[0]
        title = " ".join(
            re.findall("[A-Z][^A-Z]*", filename.split("/")[-1].split("_")[0])
        )

        print(f"\n>> [bold]Name[/bold]: {name}")
        print(f">> [bold]Subreddit[/bold]: {subreddit}")
        print(f">> [bold]Title[/bold]: {title}")

        try:
            print(">> Try:")
            request_body = {
                "snippet": {
                    "categoryId": 24,
                    "title": title
                    + " ("
                    + subreddit
                    + ") - trending goes brrr #Shorts",
                    "description": title
                    + " ("
                    + subreddit
                    + ") - trending goes brrr #Shorts\n\n\n#Entertainment, #fun, #funny, #comedy, #meme, #trending, #memes, #nonsense, #reddit, #viral, #reel.",
                    "tags": [
                        "fun",
                        "funny",
                        "comedy",
                        "meme",
                        "trending",
                        "memes",
                        "Entertainment",
                        "nonsense",
                        "reddit",
                        "youtube",
                        "subscribe",
                        "viral",
                        "reel",
                        "reels",
                        "Shorts",
                        "Youtubeshorts",
                    ],
                },
                "status": {
                    "privacyStatus": "public",
                    "selfDeclaredMadeForKids": False,
                },
                "notifySubscribers": True,
            }
            print(">>", request_body)
            mediaFile = MediaFileUpload(build_path + "/" + name + ".mp4")
            print(">>", mediaFile)
            response_upload = (
                service.videos()
                .insert(part="snippet,status", body=request_body, media_body=mediaFile)
                .execute()
            )
            print("\n>> ", response_upload)
            print("\n>> [blue]Uploaded![/blue]")
        except Exception as e:
            print(f"\n>> [red]Error![/red]")
            print(f"\n>> [red]Error: {str(e)}[/red]")

        print(">> Uploaded?")
    else:
        print(separator(21))
        print(
            f"\n>> [red]Why [bold]TF[/bold] is this file here?[/red]\n>> [red]File[/red]:{filename}"
        )
        print(separator(21))

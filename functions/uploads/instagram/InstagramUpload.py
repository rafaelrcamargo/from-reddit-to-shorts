import os
from pathlib import Path
from dotenv import load_dotenv
from instagrapi import Client

load_dotenv()

USERNAME = os.getenv("INSTAGRAM_USERNAME")
PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

cl = Client()
cl.login(USERNAME, PASSWORD)

media = cl.clip_upload(
    path=str(Path(__file__).cwd()) + "\\assets\\build\\" +
    "AnimalsBeingDerps_14_03_2022.mp4",
    caption="Animals Being Derps (r/AnimalsBeingDerps) - trending goes brrr #reels\n\n\n#Entertainment #fun #funny #comedy #meme #trending #memes #nonsense #reddit #viral #reel",
    thumbnail=str(Path(__file__).cwd()) + "\\assets\\build\\" +
    "AnimalsBeingDerps_14_03_2022.jpg",
    extra_data={
        "custom_accessibility_caption": "fun funny comedy meme trending memes Entertainment nonsense reddit viral reel reels",
        "like_and_view_counts_disabled": 1,
        "disable_comments": 1,
    }
)

print(media)

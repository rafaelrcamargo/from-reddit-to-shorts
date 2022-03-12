from datetime import datetime
from pathlib import Path
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = str(Path(__file__).cwd()) + \
    '\\functions\\client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

request_body = {
    'snippet': {
        'categoryId': 24,
        'title': 'trending goes brrr #Shorts',
        'description': 'trending goes brrr #Shorts\n\nfun, funny, comedy, meme, trending, memes, Entertainment, nonsense, reddit, youtube, subscribe, viral, reel, reels, Shorts, Youtubeshorts.',
        'tags': [
            'fun', 'funny', 'comedy', 'meme', 'trending', 'memes', 'Entertainment', 'nonsense', 'reddit', 'youtube', 'subscribe', 'viral', 'reel', 'reels', 'Shorts', 'Youtubeshorts'
        ]
    },
    'status': {
        'privacyStatus': 'unlisted',
        'selfDeclaredMadeForKids': False,
    },
    'notifySubscribers': True
}

mediaFile = MediaFileUpload(
    str(Path(__file__).cwd()) + '\\assets\\build\\AbruptChaos-12-03-2022.mp4')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()

"""
service.thumbnails().set(
    videoId=response_upload.get('id'),
    media_body=MediaFileUpload('thumbnail.png')
).execute()
"""

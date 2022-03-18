from pathlib import Path
import twitter
import json
import time

build_path = str(Path(__file__).cwd()) + "\\assets\\build"

# TWITTER KEYS
# https://developer.twitter.com/en/portal/dashboard

# Opening JSON file
f = open('client_secret.json')
secret = json.load(f)

consumer_key = secret['consumer_key']
consumer_secret = secret['consumer_secret']
access_token = secret['access_token']
access_token_secret = secret['access_token_secret']

# Closing file
f.close()


def get_status(media_id, api):

    url = '%s/media/upload.json' % api.upload_url

    parameters = {
        'command': 'STATUS',
        'media_id': media_id
    }

    resp = api._RequestUrl(url, 'GET', data=parameters)
    data = resp.content.decode('utf-8')
    json_data = json.loads(data)
    print(json_data)
    return json_data['processing_info']['state']


api = twitter.Api(consumer_key, consumer_secret,
                  access_token, access_token_secret)

video_filename = build_path + '\\AnimalsBeingDerps_17_03_2022.mp4'

# start uploading video
video_media_id = api.UploadMediaChunked(
    video_filename, media_category='TweetVideo')

# check status every 3 seconds until success
while True:
    video_status = get_status(video_media_id, api)
    print(video_status)
    if video_status == 'succeeded':
        break
    time.sleep(3)

# Tweet text with video attached
api.PostUpdate("Here's where you put the actual tweet text",
               media=video_media_id)

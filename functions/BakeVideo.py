# FRTS
# ? Reddit Api + Downloader

# * Imports
# Moviepy Video Editor
from moviepy.editor import *
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

# Random number
from random import randint
# Moviepy VFX
import moviepy.video.fx.all as vfx

# Sys os
import os
# Sys os walk method
from os import walk
# Sys Path
from pathlib import Path
# Date
from datetime import datetime

# Image
from PIL import Image

# Cool Terminal Colors
from rich import print

# * Consts
build_path = str(Path(__file__).cwd()) + "\\assets\\build"


def bake_video(data_path, subreddit):
    isExist = os.path.exists(build_path)
    if not isExist:
        os.makedirs(build_path)
        print(">> [italic blue]The new directory is created![/italic blue]\n")

    # * Clips
    filenames = next(walk(data_path), (None, None, []))[2]

    clips = []

    for filename in filenames:
        clips.append(VideoFileClip(str(Path(__file__).cwd(
        )) + "\\assets\\constants\\videos\\transition.mp4").resize(height=1920).set_position("center"))
        clips.append(VideoFileClip(str(data_path) +
                                   "\\{}".format(filename)).resize(width=1080).set_position("center").crossfadein(0.1).crossfadeout(0.1))

    print(">> We're about to start concatenating together", len(clips), "clips.\n")

    if len(clips) > 1:
        # Concatenate videos
        final_clip = concatenate_videoclips(
            [clip for clip in clips], method='compose')

        # Set Size
        final_clip = final_clip.resize((1080, 1920))
        # Set VFX
        final_clip = final_clip.fx(vfx.colorx, 1.1)

        # Music
        music = AudioFileClip(str(Path(__file__).cwd()) +
                              "\\assets\\constants\\audio\\music_" + str(randint(1, 5)) + ".mp3").subclip(20, int(final_clip.duration) + 20)
        music = music.volumex(0.1).audio_fadein(0.4)

        # Set Music
        if(final_clip.audio is not None):
            audioclip = final_clip.audio.volumex(1).audio_fadein(0.4)
            new_audioclip = CompositeAudioClip([audioclip, music])
        else:
            new_audioclip = CompositeAudioClip([music])

        final_clip.audio = new_audioclip

        # Bake thumb
        clips[1].save_frame(str(build_path) + "\\frame.png", t=2)

        img = Image.open(str(Path(__file__).cwd()) +
                         "\\assets\\constants\\img\\thumb_frame.png")
        background = Image.open(str(build_path) + "\\frame.png")

        # resize the image
        size = (1080, 1920)
        img = img.resize(size, Image.ANTIALIAS)
        background = background.resize(size, Image.ANTIALIAS)

        background.paste(img, (0, 0), img)

        background = background.convert('RGB')
        background.save(str(Path(__file__).cwd()) +
                        "\\assets\\build\\" + subreddit + "_" + datetime.today().strftime('%d_%m_%Y') + ".jpg", "JPEG")

        os.remove(str(build_path) + "\\frame.png")

        # Build video
        final_clip.write_videofile(
            str(build_path) + "\\" + subreddit + "_" + datetime.today().strftime('%d_%m_%Y') + ".mp4", fps=30)

        print("\n>> [italic blue]New video ready![/italic blue] 🥳")
    else:
        print(">> [bold red]You need to add more than one video![/bold red]")
# FRTS
# ? Reddit Api + Downloader

# * Imports
# Moviepy Video Editor
from moviepy.editor import *
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips

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

# Cool Terminal Colors
from rich import print

# * Consts
build_path = str(Path(__file__).cwd()) + "\\assets\\build"


def bake_video(data_path, subreddit):
    isExist = os.path.exists(build_path)
    if not isExist:
        os.makedirs(build_path)
        print(">> [italic blue]The new directory is created![/italic blue]\n")

    # * Music
    music = AudioFileClip(str(Path(__file__).cwd()) +
                          "\\assets\\audio\\music.mp3").subclip(20, 80)
    music = music.volumex(0.05).audio_fadein(0.4).audio_fadeout(0.4)

    # * Clips
    filenames = next(walk(data_path), (None, None, []))[2]

    clips = []

    for filename in filenames:
        clips.append(VideoFileClip(str(data_path) +
                     "\\{}".format(filename)).resize(width=1080).set_position("center").crossfadein(0.2).crossfadeout(0.2))

    print(">> We're about to start concatenating together", len(clips), "clips.\n")

    if len(clips) > 1:
        # Concatenate videos
        final_clip = concatenate_videoclips(
            [clip for clip in clips], method='compose')

        # Set Size
        final_clip = final_clip.resize((1080, 1920))
        # Set VFX
        final_clip = final_clip.fx(vfx.colorx, 1.1)
        # Set Music
        new_audioclip = CompositeAudioClip([final_clip.audio, music])
        final_clip.audio = new_audioclip

        # Build video
        final_clip.write_videofile(
            str(build_path) + "\\" + subreddit + "-" + datetime.today().strftime('%d-%m-%Y') + ".mp4", fps=30)

        print("\n>> [italic blue]New video ready![/italic blue] 🥳")
    else:
        print("\n>> [bold red]You need to add more than one video![/bold red]\n")

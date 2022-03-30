"""Bake reddit video"""

# * Imports
# Sys os
import os

# Sys os walk method
from os import walk

# Sys Path
from pathlib import Path

# Random number
from random import randint

# Date
from datetime import datetime

# Moviepy Video Editor
from moviepy.editor import (
    VideoFileClip,
    AudioFileClip,
    CompositeAudioClip,
)

# Moviepy VFX
from moviepy.editor import *

# Image
from PIL import Image

# Cool Terminal Colors
from rich import print

# * Consts
build_path = (
    str(Path(__file__).cwd()) + "/assets/build/" + datetime.today().strftime("%d_%m_%Y")
)


def bake_video(data_path, subreddit):
    """Bakes the video from the downloaded ones."""

    # * Variables
    dir_exists = os.path.exists(build_path)

    # * Clips
    filenames = next(walk(data_path), (None, None, []))[2]
    clips = []

    for filename in filenames:
        clips.append(
            VideoFileClip(
                str(Path(__file__).cwd()) + "/assets/constants/videos/transition.mp4",
                target_resolution=(1920, None),
            ).set_position("center")
        )
        clips.append(
            VideoFileClip(
                str(data_path) + f"/{filename}", target_resolution=(None, 1080)
            )
            .set_position("center")
            .crossfadein(0.1)
            .crossfadeout(0.1)
        )

    print("\n>> Clips:", len(clips))

    # ? Check quantity of clips
    if len(clips) <= 1:
        print(">> [bold red]You need to add more than one video![/bold red]")
        return False

    # ? Check if the directory exists
    if not dir_exists:
        os.makedirs(build_path)
        print(">> [italic blue]The new directory is created![/italic blue]\n")

    # * * * Build the video * * *
    print(">> [bold blue]Building the video...[/bold blue]")
    print(f">> We're about to start concatenating together {len(clips)} clips.")
    # Concatenate videos
    final_clip = concatenate_videoclips([clip for clip in clips], method="compose")

    # Set Size
    final_clip = final_clip.resize((1080, 1920))
    # Set VFX
    final_clip = final_clip.fx(vfx.colorx, 1.1)

    # Music
    music = AudioFileClip(
        str(Path(__file__).cwd())
        + "/assets/constants/audio/music_"
        + str(randint(1, 5))
        + ".mp3",
    )
    music = music.volumex(0.1).audio_fadein(0.4)

    # Composite Audio Clips
    if final_clip.audio is not None:
        audioclip = final_clip.audio.volumex(1).audio_fadein(0.4)
        new_audioclip = CompositeAudioClip([audioclip, music])
    else:
        new_audioclip = CompositeAudioClip([music])

    new_audioclip = new_audioclip.set_duration(final_clip.duration)
    final_clip.audio = new_audioclip
    new_audioclip.close()

    # Bake thumb
    print("\n>> [bold blue]Building the thumbnail...[/bold blue]")

    clips[1].save_frame(str(build_path) + "/frame.png", t=2)

    img = Image.open(
        str(Path(__file__).cwd()) + "/assets/constants/img/thumb_frame.png"
    )
    background = Image.open(str(build_path) + "/frame.png")

    # Resize the image
    size = (1080, 1920)
    img = img.resize(size, Image.ANTIALIAS)
    background = background.resize(size, Image.ANTIALIAS)

    background.paste(img, (0, 0), img)

    background = background.convert("RGB")
    background.save(
        str(Path(__file__).cwd())
        + "/assets/build/"
        + datetime.today().strftime("%d_%m_%Y")
        + "/"
        + subreddit
        + "_"
        + datetime.today().strftime("%d_%m_%Y")
        + ".jpg",
        "JPEG",
    )

    os.remove(str(build_path) + "/frame.png")

    # Build video
    final_clip.write_videofile(
        filename=str(build_path)
        + "/"
        + subreddit
        + "_"
        + datetime.today().strftime("%d_%m_%Y")
        + ".mp4",
        fps=30,
        codec="mpeg4",
        preset="fast",
    )

    final_clip.close()

    print("\n>> [italic blue]New video ready![/italic blue] 🥳")
    return (
        str(build_path)
        + "/"
        + subreddit
        + "_"
        + datetime.today().strftime("%d_%m_%Y")
        + ".mp4"
    )

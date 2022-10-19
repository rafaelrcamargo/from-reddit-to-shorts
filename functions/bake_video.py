"""Bake reddit video"""

# * Imports
# Sys os
import os

# Date
from datetime import datetime

# Sys os walk method
from os import walk

# Sys Path
from pathlib import Path

# Random number
from random import randint
import shutil

# Moviepy Video Editor
from moviepy.editor import (
    AudioFileClip,
    CompositeAudioClip,
    VideoFileClip,
    concatenate_videoclips,
)

# Image
from PIL import Image

# Cool Terminal Colors
from rich import print

# Moviepy VFX
from moviepy.audio.fx.volumex import volumex

# * Consts
DATE = datetime.today().strftime("%d_%m_%Y")
BUILD_PATH = str(Path(__file__).cwd()) + "/temp/build/" + DATE


def bake_video(data_path, subreddit):
    """Bakes the video from the downloaded ones."""

    # * Variables
    dir_exists = os.path.exists(BUILD_PATH)

    # * Clips
    filenames = next(walk(data_path), (None, None, []))[2]
    clips = []

    for filename in filenames:
        clips.append(
            VideoFileClip(
                str(data_path) + f"/{filename}", target_resolution=(None, 1080)
            ).set_position(("center", "center"))
        )

    # ? Check quantity of clips
    if len(clips) <= 1:
        print(">> [bold red]You need to add more than one video![/bold red]")
        return False

    # ? Check if the directory exists
    if not dir_exists:
        os.makedirs(BUILD_PATH)
        print(">> [italic blue]The new directory is created![/italic blue]\n")

    # * * * Build the video * * *
    print(">> [bold blue]Building the video...[/bold blue]")
    print(f">> We're about to start concatenating together {len(clips)} clips.")

    # Get transition
    transition = VideoFileClip(
        str(Path(__file__).cwd()) + f"/assets/videos/{str(randint(1, 9))}.mp4",
        target_resolution=(1920, 1080),
    ).set_position(("center", "center"))

    transition = transition.fx(volumex, 0.2)

    # Concatenate videos
    final_clip = concatenate_videoclips(
        clips, method="compose", transition=transition, bg_color=(26, 26, 26)
    )

    # Get music
    music_path = f"/assets/audios/{str(randint(1, 9))}.mp3"
    music = AudioFileClip(f"{str(Path(__file__).cwd())}{music_path}")
    music = music.fx(volumex, 0.2)

    # Set audio clips
    if final_clip.audio is not None:
        new_audioclip = CompositeAudioClip([final_clip.audio, music])
    else:
        new_audioclip = CompositeAudioClip([music])

    new_audioclip = new_audioclip.set_duration(final_clip.duration)
    final_clip.audio = new_audioclip
    new_audioclip.close()

    # Bake thumb
    print("\n>> [bold blue]Building the thumbnail...[/bold blue]")

    clips[1].save_frame(str(BUILD_PATH) + "/frame.png", t=2)

    img = Image.open(
        str(Path(__file__).cwd()) + "/assets/images/thumb_frame.png"
    ).convert("RGBA")

    background = Image.open(str(BUILD_PATH) + "/frame.png").convert("RGBA")

    # Resize the image
    size = (1080, 1920)
    img = img.resize(size, Image.ANTIALIAS)
    background = background.resize(size, Image.ANTIALIAS)

    background.paste(img, (0, 0), img)

    img.close()

    background = background.convert("RGB")
    background.save(
        f"{str(Path(__file__).cwd())}/temp/build/{DATE}/{subreddit}_{DATE}.jpg",
        "JPEG",
    )

    os.remove(str(BUILD_PATH) + "/frame.png")

    # Build video
    final_clip.write_videofile(
        filename=f"{str(BUILD_PATH)}/{subreddit}_{DATE}.mp4",
        fps=30,
        codec="libx264",
        preset="fast",
        threads=4,
    )

    final_clip.close()

    shutil.rmtree(path=data_path, ignore_errors=True)

    print("\n>> [blink blue]New video ready![/blink blue] 🥳")
    return f"{str(BUILD_PATH)}/{subreddit}_{DATE}.mp4"

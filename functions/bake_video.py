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
    concatenate_videoclips,
)

# Moviepy VFX
from moviepy.audio.fx import volumex, audio_fadein

# Image
from PIL import Image

# Cool Terminal Colors
from rich import print

# * Consts
DATE = datetime.today().strftime("%d_%m_%Y")
BUILD_PATH = str(Path(__file__).cwd()) + "/assets/build/" + DATE


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
    # Concatenate videos
    final_clip = concatenate_videoclips(clips, method="compose")

    # Set Size
    # final_clip = final_clip.size((1080, 1920))
    # Set VFX
    final_clip = final_clip.vfx.fx.colorx(10)

    # Music
    music = AudioFileClip(
        f"{str(Path(__file__).cwd())}/assets/constants/audio/music_{str(randint(1, 5))}.mp3"
    )
    music = music.fx(volumex, 0.1).audio_fadein(0.4)
    music = music.fx(audio_fadein, 0.4)

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

    clips[1].save_frame(str(BUILD_PATH) + "/frame.png", t=2)

    img = Image.open(
        str(Path(__file__).cwd()) + "/assets/constants/img/thumb_frame.png"
    )
    background = Image.open(str(BUILD_PATH) + "/frame.png")

    # Resize the image
    size = (1080, 1920)
    img = img.resize(size, Image.ANTIALIAS)
    background = background.resize(size, Image.ANTIALIAS)

    background.paste(img, (0, 0), img)

    background = background.convert("RGB")
    background.save(
        f"{str(Path(__file__).cwd())}/assets/build/{DATE}/{subreddit}_{DATE}.jpg",
        "JPEG",
    )

    os.remove(str(BUILD_PATH) + "/frame.png")

    # Build video
    final_clip.write_videofile(
        filename=f"{str(BUILD_PATH)}/{subreddit}_{DATE}.mp4",
        fps=30,
        codec="mpeg4",
        preset="fast",
    )

    final_clip.close()

    print("\n>> [italic blue]New video ready![/italic blue] 🥳")
    return f"{str(BUILD_PATH)}/{subreddit}_{DATE}.mp4"

from moviepy.editor import VideoFileClip, concatenate_videoclips
from os import walk

filenames = next(walk("./videos"), (None, None, []))[2]

clips = []

for filename in filenames:
    clips.append(VideoFileClip("./videos/{}".format(filename)))

print(clips)

final_clip = concatenate_videoclips([clip for clip in clips])
final_clip.write_videofile("./build/final_clip.mp4")

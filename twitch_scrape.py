import os
import ffmpeg

print(os.popen(f"python3 twitch-dl.pyz download https://www.twitch.tv/videos/2106156151 -q 360p30 -w 20").read())
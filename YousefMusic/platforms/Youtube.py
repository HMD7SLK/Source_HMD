import asyncio
import os
import re
import json
import glob
import random
import yt_dlp

from youtubesearchpython.__future__ import VideosSearch
from YousefMusic.utils.database import is_on_off
from YousefMusic.utils.formatters import time_to_seconds


# -----------------------------
# ✔ COOKIE HANDLER FIXED
# -----------------------------
def cookie_txt_file():
    folder_path = os.path.join(os.getcwd(), "cookies")

    try:
        txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

        if not txt_files:
            return None

        cookie = random.choice(txt_files)

        return cookie  # 🔥 مهم: رجّع المسار الكامل

    except:
        return None


# -----------------------------
# ✔ BASE OPTIONS FIXED
# -----------------------------
def base_opts():
    opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "no_warnings": True,
        "geo_bypass": True,
        "extractor_args": {
            "youtube": {
                "player_client": ["android"]
            }
        }
    }

    cookie = cookie_txt_file()
    if cookie:
        opts["cookiefile"] = cookie  # 🔥 هنا التصحيح الحقيقي

    return opts


# -----------------------------
# ✔ YOUTUBE CLASS FIXED
# -----------------------------
class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="
        self.regex = r"(?:youtube\.com|youtu\.be)"
        self.listbase = "https://youtube.com/playlist?list="

    async def url(self, message):
        try:
            if not getattr(message, "text", None):
                return None

            if len(message.command) < 2:
                return None

            query = " ".join(message.command[1:]).strip()

            if query.startswith(("http://", "https://")):
                return query

            results = VideosSearch(query, limit=1)
            data = await results.next()

            if not data.get("result"):
                return None

            return data["result"][0]["link"]

        except:
            return None

    # -------------------------
    async def video(self, link, videoid=None):
        if videoid:
            link = self.base + link

        cmd = [
            "yt-dlp",
            "--cookies", cookie_txt_file() if cookie_txt_file() else "",
            "-g",
            "-f",
            "best[height<=720]",
            link
        ]

        if "" in cmd:
            cmd.remove("")

        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        stdout, stderr = await proc.communicate()

        if stdout:
            return 1, stdout.decode().split("\n")[0]

        return 0, stderr.decode()

    # -------------------------
    async def download(self, link, video=None, songaudio=None, songvideo=None, videoid=None):
        if videoid:
            link = self.base + link

        loop = asyncio.get_running_loop()

        def audio_dl():
            opts = base_opts()
            opts.update({
                "format": "bestaudio/best",
                "outtmpl": "downloads/%(id)s.%(ext)s",
            })

            ydl = yt_dlp.YoutubeDL(opts)
            info = ydl.extract_info(link, False)
            path = f"downloads/{info['id']}.{info['ext']}"

            if not os.path.exists(path):
                ydl.download([link])

            return path

        def video_dl():
            opts = base_opts()
            opts.update({
                "format": "best[height<=720]",
                "outtmpl": "downloads/%(id)s.%(ext)s",
            })

            ydl = yt_dlp.YoutubeDL(opts)
            info = ydl.extract_info(link, False)
            path = f"downloads/{info['id']}.{info['ext']}"

            if not os.path.exists(path):
                ydl.download([link])

            return path

        if songaudio:
            return await loop.run_in_executor(None, audio_dl), True

        if songvideo or video:
            return await loop.run_in_executor(None, video_dl), True

        return await loop.run_in_executor(None, audio_dl), True

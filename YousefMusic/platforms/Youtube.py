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
        self.regex = r"(?:youtube.com|youtu.be)"
        self.listbase = "https://youtube.com/playlist?list="

    async def exists(self, url):
        return True

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

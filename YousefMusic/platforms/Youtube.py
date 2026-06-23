import asyncio
import os
import re
import json
import glob
import random
from typing import Union

import yt_dlp
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from youtubesearchpython.__future__ import VideosSearch

from YousefMusic.utils.database import is_on_off
from YousefMusic.utils.formatters import time_to_seconds


# -----------------------------
# ✔ SAFE COOKIE HANDLER (FIXED)
# -----------------------------
def cookie_txt_file():
    folder_path = f"{os.getcwd()}/cookies"
    filename = f"{os.getcwd()}/cookies/logs.csv"

    try:
        txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

        # لو ما في cookies → لا تكسر البوت
        if not txt_files:
            return None

        cookie = random.choice(txt_files)

        os.makedirs(folder_path, exist_ok=True)
        with open(filename, "a") as file:
            file.write(f"Chosen File: {cookie}\n")

        return f"cookies/{os.path.basename(cookie)}"

    except:
        return None


# -----------------------------
# ✔ SAFE YT-DLP SIZE CHECK
# -----------------------------
async def check_file_size(link):
    async def get_format_info(link):
        cmd = ["yt-dlp", "-J", link]

        cookie = cookie_txt_file()
        if cookie:
            cmd.insert(1, "--cookies")
            cmd.insert(2, cookie)

        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await proc.communicate()
        if proc.returncode != 0:
            return None

        return json.loads(stdout.decode())

    def parse_size(formats):
        return sum(f.get("filesize", 0) or 0 for f in formats)

    info = await get_format_info(link)
    if not info:
        return None

    formats = info.get("formats", [])
    return parse_size(formats) if formats else None


# -----------------------------
# ✔ SHELL SAFE COMMAND
# -----------------------------
async def shell_cmd(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    out, err = await proc.communicate()
    return out.decode() if out else err.decode()


# -----------------------------
# ✔ YOUTUBE CLASS (FIXED FULL)
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

        except Exception:
            return None

    # -------------------------
    async def exists(self, link, videoid=None):
        if videoid:
            link = self.base + link
        return bool(re.search(self.regex, link))

    # -------------------------
    async def video(self, link, videoid=None):
        if videoid:
            link = self.base + link

        cmd = [
            "yt-dlp",
            "-g",
            "-f",
            "best[height<=720]"
        ]

        cookie = cookie_txt_file()
        if cookie:
            cmd.insert(1, "--cookies")
            cmd.insert(2, cookie)

        cmd.append(link)

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
    async def playlist(self, link, limit, user_id, videoid=None):
        if videoid:
            link = self.listbase + link

        cmd = [
            "yt-dlp",
            "-i",
            "--get-id",
            "--flat-playlist",
            f"--playlist-end={limit}",
            "--skip-download",
        ]

        cookie = cookie_txt_file()
        if cookie:
            cmd.extend(["--cookies", cookie])

        cmd.append(link)

        return (await shell_cmd(" ".join(cmd))).split()

    # -------------------------
    async def track(self, link, videoid=None):
        if videoid:
            link = self.base + link

        results = VideosSearch(link, limit=1)
        r = (await results.next())["result"][0]

        return {
            "title": r["title"],
            "link": r["link"],
            "vidid": r["id"],
            "duration_min": r["duration"],
            "thumb": r["thumbnails"][0]["url"].split("?")[0],
        }, r["id"]

    # -------------------------
    async def slider(self, link, query_type, videoid=None):
        if videoid:
            link = self.base + link

        a = VideosSearch(link, limit=10)
        r = (await a.next())["result"][query_type]

        return (
            r["title"],
            r["duration"],
            r["thumbnails"][0]["url"].split("?")[0],
            r["id"],
        )

    # -------------------------
    async def download(
        self,
        link,
        *args,
        video=None,
        songaudio=None,
        songvideo=None,
        format_id=None,
        title=None,
        videoid=None,
    ):
        if videoid:
            link = self.base + link

        loop = asyncio.get_running_loop()

        def base_opts():
            return {
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
                opt["cookiefile"] = cookie

            return opt

        def audio_dl():
            opts = base_opts()
            opts.update({
                "format": "bestaudio/best",
                "outtmpl": "downloads/%(id)s.%(ext)s",
            })
            x = yt_dlp.YoutubeDL(opts)
            info = x.extract_info(link, False)
            path = f"downloads/{info['id']}.{info['ext']}"
            if not os.path.exists(path):
                x.download([link])
            return path

        def video_dl():
            opts = base_opts()
            opts.update({
                "format": "best[height<=720]",
                "outtmpl": "downloads/%(id)s.%(ext)s",
            })
            x = yt_dlp.YoutubeDL(opts)
            info = x.extract_info(link, False)
            path = f"downloads/{info['id']}.{info['ext']}"
            if not os.path.exists(path):
                x.download([link])
            return path

        if songaudio:
            return await loop.run_in_executor(None, audio_dl), True

        if songvideo:
            return await loop.run_in_executor(None, video_dl), True

        if video:
            return await loop.run_in_executor(None, video_dl), True

        return await loop.run_in_executor(None, audio_dl), True

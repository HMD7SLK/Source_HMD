import yt_dlp
import asyncio
import os


class YouTubeAPI:

    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="

    async def url(self, message):
        try:
            if len(message.command) < 2:
                return None

            query = " ".join(message.command[1:])

            if query.startswith("http://") or query.startswith("https://"):
                return query

            result = await self.search(query)

            if result:
                return result["url"]

            return None
        except Exception:
            return None

    # 🔍 بحث يوتيوب
    async def search(self, query: str):
        loop = asyncio.get_event_loop()

        def run():
            ydl_opts = {
                "quiet": True,
                "default_search": "ytsearch1",
                "skip_download": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)
                video = info["entries"][0]

                return {
                    "title": video.get("title"),
                    "duration": video.get("duration"),
                    "id": video.get("id"),
                    "url": video.get("webpage_url"),
                    "thumbnail": video.get("thumbnail"),
                }

        return await loop.run_in_executor(None, run)

    # 🎧 رابط الصوت
    async def stream_url(self, url: str):
        loop = asyncio.get_event_loop()

        def run():
            ydl_opts = {
                "format": "bestaudio/best",
                "quiet": True,
                "nocheckcertificate": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info["url"]

        return await loop.run_in_executor(None, run)

    # 🎬 معلومات الفيديو
    async def get_info(self, url: str):
        loop = asyncio.get_event_loop()

        def run():
            ydl_opts = {
                "quiet": True,
                "nocheckcertificate": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                return {
                    "title": info.get("title"),
                    "duration": info.get("duration"),
                    "id": info.get("id"),
                    "thumbnail": info.get("thumbnail"),
                }

        return await loop.run_in_executor(None, run)

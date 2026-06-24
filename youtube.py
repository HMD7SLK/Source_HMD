import asyncio
import yt_dlp


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="

    # 🔍 البحث عن فيديو
    async def search(self, query: str):
        loop = asyncio.get_event_loop()

        def run():
            ydl_opts = {
                "quiet": True,
                "format": "bestaudio/best",
                "noplaylist": True,
                "default_search": "ytsearch1",
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(query, download=False)

                video = info["entries"][0]

                return {
                    "title": video.get("title"),
                    "url": video.get("webpage_url"),
                    "id": video.get("id"),
                    "duration": video.get("duration"),
                    "thumbnail": video.get("thumbnail"),
                    "uploader": video.get("uploader"),
                }

        return await loop.run_in_executor(None, run)

    # 🎧 تحويل اسم أو رابط إلى URL مباشر
    async def url(self, message):
        try:
            if len(message.command) < 2:
                return None

            query = " ".join(message.command[1:])

            # إذا رابط مباشر
            if query.startswith("http"):
                return query

            result = await self.search(query)

            if result:
                return result["url"]

            return None

        except Exception:
            return None

    # 🎵 رابط الصوت المباشر
    async def stream_url(self, url: str):
        loop = asyncio.get_event_loop()

        def run():
            ydl_opts = {
                "format": "bestaudio/best",
                "quiet": True,
                "noplaylist": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                return info["url"]

        return await loop.run_in_executor(None, run)

    # 📌 معلومات الفيديو
    async def get_info(self, url: str):
        loop = asyncio.get_event_loop()

        def run():
            ydl_opts = {
                "quiet": True,
                "noplaylist": True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)

                return {
                    "title": info.get("title"),
                    "duration": info.get("duration"),
                    "id": info.get("id"),
                    "thumbnail": info.get("thumbnail"),
                    "uploader": info.get("uploader"),
                }

        return await loop.run_in_executor(None, run)

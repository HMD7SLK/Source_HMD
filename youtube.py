import asyncio
import yt_dlp


class YouTubeAPI:
    def __init__(self):
        self.base = "https://www.youtube.com/watch?v="

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

    async def url(self, message):
        try:
            if len(message.command) < 2:
                return None

            query = " ".join(message.command[1:])

            if query.startswith("http"):
                return query

            result = await self.search(query)

            if result:
                return result["url"]

            return None

        except Exception:
            return None

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

    async def exists(self, url):
        try:
            if not url:
                return False

            return "youtube.com" in str(url) or "youtu.be" in str(url)
        except:
            return False

    async def track(self, query):
        try:
            if query.startswith(("http://", "https://")):
                info = await self.get_info(query)

                details = {
                    "title": info["title"],
                    "duration": info["duration"],
                    "dur": info["duration"],
                    "thumb": info["thumbnail"],
                    "thumbnail": info["thumbnail"],
                    "videoid": info["id"],
                    "id": info["id"],
                    "url": query,
                }

                return details, info["id"]

            result = await self.search(query)

            details = {
                "title": result["title"],
                "duration": result["duration"],
                "dur": result["duration"],
                "thumb": result["thumbnail"],
                "thumbnail": result["thumbnail"],
                "videoid": result["id"],
                "id": result["id"],
                "url": result["url"],
            }

            return details, result["id"]

        except Exception as e:
            raise Exception(str(e))

import os
import requests
import config
import yt_dlp
from yt_dlp import YoutubeDL
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from youtube_search import YoutubeSearch

from YousefMusic import app
from YousefMusic.plugins.play.filters import command
from YousefMusic.platforms.Youtube import cookie_txt_file


def remove_if_exists(path):
    if path and os.path.exists(path):
        os.remove(path)


channel = config.CHANNEL_SUDO
lnk = config.CHANNEL_LINK
Nem = config.BOT_NAME + " ابحث"


@app.on_message(command(["يوت", "نزل", "بحث", Nem]))
async def song_downloader(client, message: Message):

    query = " ".join(message.command[1:])
    if not query:
        return await message.reply_text("اكتب اسم الأغنية 🎵")

    m = await message.reply_text("<b>⇜ جـارِ البحث ..</b>")

    ydl_opts = {
        "format": "bestaudio[ext=m4a]",
        "keepvideo": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quiet": True,
        "cookiefile": cookie_txt_file(),
    }

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()

        if not results:
            return await m.edit("- لم يتم العثور على نتائج")

        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:60]
        thumbnail = results[0]["thumbnails"][0]
        duration = results[0].get("duration", "0:00")

        thumb_name = f"{title}.jpg"

        with open(thumb_name, "wb") as f:
            f.write(requests.get(thumbnail).content)

    except Exception as e:
        await m.edit("- خطأ أثناء البحث")
        print(e)
        return

    await m.edit("<b>جاري التحميل 🎵</b>")

    audio_file = None

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            audio_file = ydl.prepare_filename(info_dict)

        rep = f"ᏟᎻᎪΝΝᎬᏞ 𓏺 @{channel}"
        host = info_dict.get("uploader", "Unknown")

        # تحويل الوقت إلى ثواني
        dur = 0
        try:
            parts = duration.split(":")
            for i in range(len(parts)):
                dur = dur * 60 + int(parts[i])
        except:
            dur = 0

        await message.reply_audio(
            audio=audio_file,
            caption=rep,
            title=title,
            performer=host,
            thumb=thumb_name,
            duration=dur,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="كِتابات خَارج السرب",
                            url="https://t.me/cecrr"
                        ),
                    ],
                ]
            ),
        )

        await m.delete()

    except Exception as e:
        await m.edit("❌ صار خطأ أثناء التحميل")
        print(e)

    # تنظيف الملفات
    try:
        remove_if_exists(audio_file)
        remove_if_exists(thumb_name)
    except Exception as e:
        print(e)

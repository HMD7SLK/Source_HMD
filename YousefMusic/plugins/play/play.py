import random
import string
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto, Message
from pyrogram import filters
from pytgcalls.exceptions import NoActiveGroupCall

from config import YAFA_NAME, YAFA_CHANNEL, CHANNEL_SUDO
import config

from YousefMusic import Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app
from YousefMusic.core.call import Zoro
from YousefMusic.utils import seconds_to_min, time_to_seconds
from YousefMusic.utils.channelplay import get_channeplayCB
from YousefMusic.utils.decorators.language import languageCB
from YousefMusic.utils.decorators.play import PlayWrapper
from YousefMusic.utils.formatters import formats
from YousefMusic.utils.inline import (
    botplaylist_markup,
    livestream_markup,
    playlist_markup,
    slider_markup,
    track_markup,
)
from YousefMusic.utils.logger import play_logs
from YousefMusic.utils.stream.stream import stream
from config import BANNED_USERS, lyrical


force_btn = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text=YAFA_NAME, url=YAFA_CHANNEL)]]
)


async def check_is_joined(message):
    try:
        if message.sender_chat and "CHANNEL" in str(message.sender_chat.type):
            return True
    except:
        pass

    try:
        userid = message.from_user.id
        await app.get_chat_member(CHANNEL_SUDO, userid)
        return True
    except:
        await app.send_message(
            message.chat.id,
            "**⚠️ يجب الاشتراك بالقناة أولاً**",
            reply_markup=force_btn
        )
        return False


@app.on_message(
    filters.command([
        "play","تشغيل","شغل","vplay","فديو","cplay","cvplay",
        "playforce","vplayforce","cplayforce","cvplayforce"
    ], "")
    & ~BANNED_USERS
)
@PlayWrapper
async def play_commnd(client, message: Message, _, chat_id, video, channel, playmode, url, fplay):

    if not await check_is_joined(message):
        return

    mystic = await message.reply_text(_["play_2"].format(channel) if channel else _["play_1"])

    user_id = message.from_user.id if message.from_user else 0
    user_name = message.from_user.first_name if message.from_user else "None"

    audio = message.reply_to_message.audio if message.reply_to_message else None
    video_msg = message.reply_to_message.video if message.reply_to_message else None

    # ================= AUDIO =================
    if audio:
        try:
            file_path = await Telegram.get_filepath(audio=audio)
            await Telegram.download(_, message, mystic, file_path)

            details = {
                "title": audio.file_name,
                "path": file_path,
                "dur": audio.duration,
            }

            await stream(_, mystic, user_id, details, chat_id, user_name,
                         message.chat.id, streamtype="telegram", forceplay=fplay)

            await mystic.delete()
            return

        except Exception as e:
            return await mystic.edit_text(f"Audio Error: {e}")

    # ================= VIDEO =================
    if video_msg:
        try:
            file_path = await Telegram.get_filepath(video=video_msg)
            await Telegram.download(_, message, mystic, file_path)

            details = {
                "title": video_msg.file_name,
                "path": file_path,
                "dur": video_msg.duration,
            }

            await stream(_, mystic, user_id, details, chat_id, user_name,
                         message.chat.id, video=True, streamtype="telegram", forceplay=fplay)

            await mystic.delete()
            return

        except Exception as e:
            return await mystic.edit_text(f"Video Error: {e}")

    # ================= URL =================
    if url:

        try:
            if await YouTube.exists(url):
                details, track_id = await YouTube.track(url)
                streamtype = "youtube"
                img = details["thumb"]
                cap = details["title"]

            elif await Spotify.valid(url):
                details, track_id = await Spotify.track(url)
                streamtype = "youtube"
                img = details["thumb"]
                cap = details["title"]

            elif await SoundCloud.valid(url):
                details, path = await SoundCloud.download(url)

                await stream(_, mystic, user_id, details, chat_id, user_name,
                             message.chat.id, streamtype="soundcloud", forceplay=fplay)
                await mystic.delete()
                return

            else:
                # 🔥 FIX HERE (was Anony - broken)
                await Zoro.stream_call(url)

                await stream(_, mystic, user_id, url, chat_id, user_name,
                             message.chat.id, video=video, streamtype="index",
                             forceplay=fplay)
                await mystic.delete()
                return

            await stream(_, mystic, user_id, details, chat_id, user_name,
                         message.chat.id, video=video, streamtype=streamtype,
                         forceplay=fplay)

            await mystic.delete()

        except NoActiveGroupCall:
            return await mystic.edit_text("⚠️ افتح مكالمة في القروب أولاً")

        except Exception as e:
            return await mystic.edit_text(f"URL Error: {e}")

        return


    # ================= SEARCH =================
    if len(message.command) < 2:
        return await mystic.edit_text("اكتب اسم الأغنية")

    query = message.text.split(None, 1)[1]

    try:
        details, track_id = await YouTube.track(query)
    except Exception as e:
        return await mystic.edit_text(f"YouTube Error: {e}")

    await stream(_, mystic, user_id, details, chat_id, user_name,
                 message.chat.id, video=video, streamtype="youtube",
                 forceplay=fplay)

    await mystic.delete()
    return await play_logs(message, streamtype="youtube")

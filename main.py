import web

import asyncio
import importlib
import logging
import traceback

from pyrogram import idle

import config
from YousefMusic import LOGGER, app, userbot
from YousefMusic.core.call import Zoro
from YousefMusic.misc import sudo
from YousefMusic.plugins import ALL_MODULES
from YousefMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

logging.basicConfig(level=logging.INFO)


async def init():

    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("كود جلسة الحساب المساعد غير موجود")
        return

    await sudo()

    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)

        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)

    except Exception as e:
        print("DB ERROR:", e)
        traceback.print_exc()

    await app.start()

    for all_module in ALL_MODULES:
        importlib.import_module("YousefMusic.plugins." + all_module)

    LOGGER("YousefMusic").info("تم تحميل الإضافات ✓")

    try:
        await userbot.start()
        await Zoro.start()
        await Zoro.decorators()

        LOGGER("YousefMusic").info("تم تشغيل البوت بنجاح ✓")

    except Exception as e:
        print("START ERROR:", e)
        traceback.print_exc()

    await idle()

    LOGGER("YousefMusic").info("جاري إيقاف البوت...")

    try:
        await app.stop()
        await userbot.stop()

    except Exception as e:
        print("STOP ERROR:", e)
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())

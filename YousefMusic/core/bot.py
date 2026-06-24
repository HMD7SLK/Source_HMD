from pyrogram import Client, errors

import config
from ..logging import LOGGER


class Zoro(Client):
    def __init__(self):
        LOGGER("ميــوزك بحر").info("جارِ بدء تشغيل البوت . . .")
        super().__init__(
            name="YousefMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()

        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            print(f"LOGGER_ID = {config.LOGGER_ID}")

            chat = await self.get_chat(config.LOGGER_ID)
            print(f"LOGGER CHAT = {chat.title}")

            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"» تم تشغيل الميوزك\n\n"
                    f"ID : {self.id}\n"
                    f"NAME : {self.name}\n"
                    f"USERNAME : @{self.username}"
                ),
            )

        except (errors.ChannelInvalid, errors.PeerIdInvalid) as ex:
            print(f"LOGGER WARNING => {ex}")
            LOGGER(__name__).warning(
                f"Logger group not accessible: {ex}"
            )

        except Exception as ex:
            print(f"LOGGER WARNING => {ex}")
            LOGGER(__name__).warning(
                f"Bot can't access LOGGER_ID: {ex}"
            )

        LOGGER("ميــوزك بحر").info(
            f"تم بدء تشغيل البوت {self.name} ...✓"
        )

    async def stop(self):
        await super().stop()

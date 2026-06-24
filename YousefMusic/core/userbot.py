from pyrogram import Client

import config
from ..logging import LOGGER

assistants = []
assistantids = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            name="VeGaOAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
            no_updates=True,
        )

        self.two = Client(
            name="VeGaOAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
            no_updates=True,
        )

        self.three = Client(
            name="VeGaOAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
            no_updates=True,
        )

        self.four = Client(
            name="VeGaOAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
            no_updates=True,
        )

        self.five = Client(
            name="MatrixAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
            no_updates=True,
        )

    async def start(self):
        LOGGER("ميــوزك بحر").info("جارِ تشغيل الحسابات المساعدة . . .")

        # Assistant 1
        if config.STRING1:
            try:
                await self.one.start()

                assistants.append(1)

                me = await self.one.get_me()

                self.one.id = me.id
                self.one.username = me.username

                if me.last_name:
                    self.one.name = f"{me.first_name} {me.last_name}"
                else:
                    self.one.name = me.first_name

                assistantids.append(me.id)

                LOGGER("ميــوزك بحر").info(
                    f"تم تشغيل الحساب المساعد الأول: {self.one.name}"
                )

            except Exception as e:
                LOGGER(__name__).error(f"Assistant 1 Error: {e}")

        # Assistant 2
        if config.STRING2:
            try:
                await self.two.start()

                assistants.append(2)

                me = await self.two.get_me()

                self.two.id = me.id
                self.two.username = me.username
                self.two.name = me.first_name

                assistantids.append(me.id)

                LOGGER("ميــوزك بحر").info(
                    f"تم تشغيل الحساب المساعد الثاني: {self.two.name}"
                )

            except Exception as e:
                LOGGER(__name__).error(f"Assistant 2 Error: {e}")

        # Assistant 3
        if config.STRING3:
            try:
                await self.three.start()

                assistants.append(3)

                me = await self.three.get_me()

                self.three.id = me.id
                self.three.username = me.username
                self.three.name = me.first_name

                assistantids.append(me.id)

                LOGGER("ميــوزك بحر").info(
                    f"تم تشغيل الحساب المساعد الثالث: {self.three.name}"
                )

            except Exception as e:
                LOGGER(__name__).error(f"Assistant 3 Error: {e}")

        # Assistant 4
        if config.STRING4:
            try:
                await self.four.start()

                assistants.append(4)

                me = await self.four.get_me()

                self.four.id = me.id
                self.four.username = me.username
                self.four.name = me.first_name

                assistantids.append(me.id)

                LOGGER("ميــوزك بحر").info(
                    f"تم تشغيل الحساب المساعد الرابع: {self.four.name}"
                )

            except Exception as e:
                LOGGER(__name__).error(f"Assistant 4 Error: {e}")

        # Assistant 5
        if config.STRING5:
            try:
                await self.five.start()

                assistants.append(5)

                me = await self.five.get_me()

                self.five.id = me.id
                self.five.username = me.username
                self.five.name = me.first_name

                assistantids.append(me.id)

                LOGGER("ميــوزك بحر").info(
                    f"تم تشغيل الحساب المساعد الخامس: {self.five.name}"
                )

            except Exception as e:
                LOGGER(__name__).error(f"Assistant 5 Error: {e}")

    async def stop(self):
        LOGGER("ميــوزك بحر").info("Stopping Assistants...")

        try:
            if config.STRING1:
                await self.one.stop()

            if config.STRING2:
                await self.two.stop()

            if config.STRING3:
                await self.three.stop()

            if config.STRING4:
                await self.four.stop()

            if config.STRING5:
                await self.five.stop()

        except Exception:
            pass

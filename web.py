import asyncio
from YousefMusic import app
from YousefMusic.core.call import Zoro

async def main():
    await app.start()
    await Zoro.start()
    print("Bot is running...")
    await asyncio.Event().wait()

asyncio.run(main())

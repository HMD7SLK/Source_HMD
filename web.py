import asyncio
from YousefMusic import app
from YousefMusic.core.call import Zoro

async def main():
    await app.start()
    await Zoro.start()
    print("Bot is running...")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())

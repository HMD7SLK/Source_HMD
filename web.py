from aiohttp import web
import os

async def home(request):
    return web.Response(text="Bot is running")

app = web.Application()
app.router.add_get("/", home)

web.run_app(app, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

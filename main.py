import os
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer

# =========================
# Render Web Server (IMPORTANT)
# =========================

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")

    def log_message(self, format, *args):
        return  # يمنع spam في logs


def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()


Thread(target=run_web).start()


# =========================
# BOT START (ضع كود البوت هنا)
# =========================

print("Bot is starting...")

# 🔻 هنا تحط كود البوت الحقيقي تبعك
# مثال:
# from pyrogram import Client
# app = Client(...)
# app.run()

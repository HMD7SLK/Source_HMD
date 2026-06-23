import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

super_sudoers = [6094238403]

load_dotenv()

API_ID = int(getenv("API_ID", 37718149))
API_HASH = getenv("API_HASH", "aa15df4d0ddaa70a3c109ed6cdb12277")

BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "")

MONGO_DB_URI = getenv(
    "MONGO_DB_URI",
    "mongodb+srv://toxi:toxiiiic1234@atlascluster.dk5l1pm.mongodb.net/?retryWrites=true&w=majority",
)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 2000))

# ===== عدل هذا الجزء =====

LOGGER_ID = int(getenv("LOGGER_ID", "-1004356471881"))

OWNER_ID = int(getenv("OWNER_ID", "8282175722"))

# =========================

YAFA_CHANNEL = getenv("YAFA_CHANNEL", "https://t.me/QQHMDQ")
YAFA_NAME = getenv("YAFA_NAME", "• اضغط هنا للاشتراك •")

CHANNEL_SUDO = getenv("CHANNEL_SUDO", "QQHMDQ")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Q_0_R")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Q_0_R")
CHANNEL_NAME = getenv("CHANNEL_NAME", "كِتابات خَارج السرب")
CHANNEL_LINK = getenv("CHANNEL_LINK", "cecrr")
OWNER_CHANNEL = getenv("OWNER_CHANNEL", "https://t.me/Q_0_R")


FAILED = "https://graph.org/file/cd2bf6082397483175f17.jpg"

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/HMD7SLK/Source_HMD",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Yousef")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private


# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}



START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/cd2bf6082397483175f17.jpg"
)
START_video_URL = getenv(
    "START_video_URL", "https://graph.org/file/c8e6ba128c7f4bf3e911b.mp4"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/cd2bf6082397483175f17.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
STATS_IMG_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
STREAM_IMG_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/cd2bf6082397483175f17.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

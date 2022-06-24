import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

API_ID = int(getenv("APP_ID", "6435225"))
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = getenv("BOT_TOKEN", "")
STRING_SESSION = getenv("STRING_SESSION")
STRING_SESSION2 = getenv("STRING_SESSION2")
STRING_SESSION3 = getenv("STRING_SESSION3")
STRING_SESSION4 = getenv("STRING_SESSION4")
STRING_SESSION5 = getenv("STRING_SESSION5")
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
HEROKU_MODE = getenv("HEROKU_MODE", None)
MANAGEMENT_MODE = getenv("MANAGEMENT_MODE", None)
BOT_USERNAME = getenv("BOT_USERNAME", "Zaid2_Robot")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
SUPPORT = getenv("SUPPORT", "TheSupportChat")
CHANNEL = getenv("CHANNEL", "TheUpdatesChannel")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
DEFAULT_ASS = int(getenv("DEFAULT_ASS")

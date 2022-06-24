import os
from os import getenv

class Config(object):
API_ID = int(os.environ.get("APP_ID", "6435225"))
API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
STRING_SESSION = os.environ.get("STRING_SESSION", "")
if str(getenv("STRING_SESSION2")).strip() == "":
    STRING_SESSION2 = str(None)
else:
    STRING_SESSION2 = str(getenv("STRING_SESSION2"))
if str(getenv("STRING_SESSION3")).strip() == "":
    STRING_SESSION3 = str(None)
else:
    STRING_SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING_SESSION4 = str(None)
else:
    STRING_SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING_SESSION5 = str(None)
else:
    STRING_SESSION5 = str(getenv("STRING_SESSION5"))
    MONGO_DB_URL = os.environ.get("MONGO_DB_URL", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Zaid2_Robot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")

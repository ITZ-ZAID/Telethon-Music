import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16715400"))
    API_HASH = os.environ.get("API_HASH", "2de611a73f73b8da8b0bcee9f855c815")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5442486445:AAGzz1Zk4sJDOiodkIbbEnnXK2G3rm_ftrg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ygabutkanbot")
    SUPPORT = os.environ.get("SUPPORT", "ygabutkan")
    CHANNEL = os.environ.get("CHANNEL", "ygabutkan")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b167d1dce40b9011892d7.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/b167d1dce40b9011892d7.jpg")

import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Zaid2_Robot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat")
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel")
    BOT_NAME = os.environ.get("BOT_NAME", "Zaid Robot")

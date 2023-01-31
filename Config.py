import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@L2F_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/TheLove2Forever") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/TheLove2Forever") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/dde7614dbd1c3f078612f.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/dde7614dbd1c3f078612f.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5749926510")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6382823660:AAGXCzbGAem48W-6rkW322yqrHS1tpR6Azo")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLoBuxWqsmbuthtchCIFGgN16q2Y642ME-pv0NBMCt12xiKJYjEGTzfKZgsnkofgNEPLUvDjfd3FzK9Z66E5z9Nf6bkpjFXBzYs5hvEJbJRvLZt5sfg0S89K-qF1OwBHh-m3jpj3VnRivppbEjxhZ9DzvdwjVIm4HEz6lrYykUiZbQ5yd7Ez1vgH-oWMcnRyaAXzSHajhijRRPc7IG5qjfus8_r3KtyYUhJOQPQfx1CQa4KzzPGWKMyZrEFttgfAshHHRRn1jjVrt5kzUy3EzZnN5mEeCP8m56HQBe_TXRrARU9wzMpahy4Z7A_2jbt7JrnUwBOkLXxbzCZYVAt3-DDP2CE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

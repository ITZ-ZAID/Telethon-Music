import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "13909391"))
    API_HASH = os.environ.get("API_HASH", "19d0868bb18965eb6eb2e34ec5778310")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5594836549:AAG0sYTMuq5_gr5X9XwknoGonChcC3vLxmU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCwh2NWPba5LmwH4wcyPqI6aU7HcnS3PRbk_J7g7S98HTQbfGAWYn7DOw_swopi9pjV_yDa35GGJe5R80aYsCG31YgRrFGEor0ERaZt79mZ7XpKgYK5UMbeQmPP9-w8Xh_BVSJZe9vSVDRpW56G21U0OIm933kBQY55H6SV84FSNM9ZEki8YF4KiV0B95SNPsv8GwJUL_QyaAEXWaQMdXms6M3emWKTNa3BZR2lwXP0_UhMyfmb-6s_Ss2fjHwU7dx44MiGjd5OVlPgaXwDhlolq3aIHWR2oZ54evk0R40ySvbapG_szSYp1SFRzJ7SgrD6GIq7w_6JdscADj0KKJuyaZgpsAA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@NJ_OP_MUSIC_BOT")
    SUPPORT = os.environ.get("SUPPORT", "AJ_NJ_SOS")
    CHANNEL = os.environ.get("CHANNEL", "AJ_NJ_SOS")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1771579824"))
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True")

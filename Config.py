import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6141992820:AAH0OEOZMzV7MU47ZdvlW-VNHtGkpslGg4s")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AZWarzUBuzFL8xcRiAGcEmY4bX3TgD3_DqczTyyK8w8CFnXM8mJxB1IlgXIXgGkMaGsfZ8z26GnmdUIWwkhgbZPKoz-gtON1M0C24_YPK3_yBFeGaZ474HJ6P4-hhamCmYdSXK0na0t4ONsWxQVLWoL4GaJO4CSYgXqMJdmcERhh7c6NFDCajyOVdOz_jSV_kmkbxUTldHUwV7W5Zn6HHSzezLooQZasw01b1RGyWU-R4mF4eF1Tr9zifONhmzeHNK8N4-34BRQv28_CnnC5oiardnHpvYETLqP2Jwc_rNt1wFj0bavrGaJu2ZwXdGcDmHJdrtNzbYeekELObrDh1HrtBYNfj1s=") #pastw string Sess
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "musicxzreaswe_bot")
    SUPPORT = os.environ.get("SUPPORT", "papokm") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "cvxzasoe") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6088000501")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"


from telethon.sessions import StringSession
from telethon.sync import TelegramClient

print(
    """Please go-to my.telegram.org
Login using your Telegram account
Click on API Development Tools
Create a new application, by entering the required details"""
)
APP_ID = int(6435225)
API_HASH = "4e984ea35f854762dcde906dce426c2d"

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    print(client.session.save())
    client.sendmessage("me", client.session.save())

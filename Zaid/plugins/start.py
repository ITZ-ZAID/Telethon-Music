from Zaid import Zaid
from telethon import events, Button

@Zaid.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hey!\nLet's Try to be a Different \nThis Bot Based on Telethon So it's Stable more.",
                    buttons=[
                        [Button.url("⚙️Support", url="https://t.me/TheSupportChat")],
                        [Button.url("🤖Repo", url="https://github.com/ITZ-ZAID/Telethon-Music")],
                    ])

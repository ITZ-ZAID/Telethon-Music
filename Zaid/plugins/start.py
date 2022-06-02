from Zaid import Zaid
from telethon import events, Button

@Zaid.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello! Welcome To Music Bot Based On Telethon",
                    buttons=[
                        [Button.url("⚙️Support", url="https://t.me/TheSupportChat")],
                        [Button.url("🤖Repo", url="https://github.com/ITZ-ZAID/Telethon-Music")],
                    ])

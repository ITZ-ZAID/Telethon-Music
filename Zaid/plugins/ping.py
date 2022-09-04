import os

from telethon import Button, events

from Zaid import *


@Zaid.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("⚜ Cԋαɳɳҽʅ ⚜", "https://t.me/TheUpdatesChannel")]]
    await event.reply("Pong", buttons=UMM)

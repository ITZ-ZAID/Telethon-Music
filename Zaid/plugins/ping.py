import os

from telethon import Button, events

from Zaid import *

IMG = os.environ.get(
    "PING_PIC", "https://te.legra.ph/file/e2fc6a4398f35c4113604.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "[❤️‍🔥𝗦𝗨𝗠𝗜𝗧❤️‍🔥](https://t.me/ab_sumit)"
)

CAPTION = f"☃︎𝗣𝚒𝚗𝚐☃︎**\n\n   ⚜ {ms}\n   ⚜ °𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁★ ~『{ALIVE}』"


@Zaid.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("⚜ Cԋαɳɳҽʅ ⚜", "https://t.me/TheUpdatesChannel")]]
    await Zaid.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)

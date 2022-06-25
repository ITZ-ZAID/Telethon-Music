import os

from telethon import Button, events

from Zaid import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/51ff101dd2e233be286a6.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@Timesisnotwaiting"
)

CAPTION = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『{ALIVE}』"


@Zaid.on(events.NewMessage(pattern="^/mping"))
async def _(event):
    UMM = [[Button.url("⚜ Cԋαɳɳҽʅ ⚜", "https://t.me/w0_69")]]
    await Zaid.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)

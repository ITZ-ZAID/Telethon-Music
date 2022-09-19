import os
import sys
import asyncio
from time import time
from datetime import datetime


from telethon import Button, events

from Zaid import *

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Zaid.on(events.NewMessage(pattern="^/ping"))
async def _(event):
   start = time()
   current_time = datetime.utcnow()
   delta_ping = time() - start
   UMM = [[Button.url("⚜ Cԋαɳɳҽʅ ⚜", "https://t.me/TheUpdatesChannel")]]
   await event.reply(f"╰☞ 𝗣𝗢𝗡𝗚™╮\n☞ `{delta_ping * 1000:.3f}`", buttons=UMM)

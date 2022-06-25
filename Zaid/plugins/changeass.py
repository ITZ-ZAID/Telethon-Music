from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *


import random

from Zaid.Database.clientdb import get_assistant, save_assistant



ass_num_list = ["1", "2", "3", "4", "5"]


@Zaid.on(events.NewMessage(pattern=r"^[?!/]changeassistant"))
@is_admin
async def assis_change(event, perm):
    usage = f"**Usage:**\n/changeassistant [ASS_NO]\n\nSelect from them\n{' | '.join(ass_num_list)}"
    num = event.text.split(None, 1)[1].strip()
    if num not in ass_num_list:
        return await event.reply(usage)
    ass_num = int(event.text.strip().split()[1])
    _assistant = await get_assistant(event.chat_id, "assistant")
    if not _assistant:
        return await event.reply(
            "No Pre-Saved Assistant Found.\n\nYou can set Assistant Via /setassistant"
        )
    else:
        ass = _assistant["saveassistant"]
    assis = {
        "saveassistant": ass_num,
    }
    await save_assistant(event.chat_id, "assistant", assis)
    await event.reply(
        f"**Changed Assistant**\n\nChanged Assistant Account from **{ass}** to Assistant Number **{ass_num}**"
    )


ass_num_list2 = ["1", "2", "3", "4", "5", "Random"]


@Zaid.on(events.NewMessage(pattern=r"^[?!/]setassistant"))
@is_admin
async def set_assi(event, perm):
    usage = f"**Usage:**\n/setassistant [ASS_NO or Random]\n\nSelect from them\n{' | '.join(ass_num_list2)}\n\nUse 'Random' to set random Assistant"
    query = event.text.split(None, 1)[1].strip()
    if query not in ass_num_list2:
        return await event.reply(usage)
    if str(query) == "Random":
        ran_ass = random.choice(random_assistant)
    else:
        ran_ass = int(event.text.strip().split()[1])
    _assistant = await get_assistant(event.chat_id, "assistant")
    if not _assistant:
        await event.reply(
            f"**__Music Bot Assistant Alloted__**\n\nAssistant No. **{ran_ass}**"
        )
        assis = {
            "saveassistant": ran_ass,
        }
        await save_assistant(event.chat_id, "assistant", assis)
    else:
        ass = _assistant["saveassistant"]
        return await event.reply(
            f"Pre-Saved Assistant Number {ass} Found.\n\nYou can change Assistant Via /changeassistant"
        )

from typing import *
import random
from typing import Dict, List, Union

from Zaid import *
from telethon import *
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotParticipantError
)
from telethon.tl.types import PeerChannel,InputChannel
from telethon.tl.functions.channels import *
from telethon.tl.functions.channels import GetParticipantsRequest
from Config import DEFAULT_ASS
from telethon.tl.types import ChannelParticipantsSearch
import telethon
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Zaid import random_assistant
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
from Zaid.Database.clientdb import get_assistant, save_assistant


def AssistantAdd(mystic):
    async def wrapper(event):
        _assistant = await get_assistant(event.chat_id, "assistant")
        if not _assistant:
            if DEFAULT_ASS:
               ran_ass = DEFAULT_ASS
            else:
               ran_ass = random.choice(random_assistant)
            assis = {
                "saveassistant": ran_ass,
            }
            await save_assistant(event.chat_id, "assistant", assis)
        else:
            ran_ass = _assistant["saveassistant"]
        if ran_ass not in random_assistant:
            if DEFAULT_ASS:
               ran_ass = DEFAULT_ASS
            else:
               ran_ass = random.choice(random_assistant)
            assis = {
                "saveassistant": ran_ass,
            }
            await save_assistant(event.chat_id, "assistant", assis)
        assistant = _assistant['saveassistant'][0]
        try:
            permissions = await event.client(GetParticipantRequest(int(event.chat_id), 5154917043))
        except UserNotParticipantError:
            if event.is_group:
                try:
                    link = await event.client(ExportChatInviteRequest(event.chat_id))
                    invitelink = link.link
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace(
                            "https://t.me/+", ""
                        )
                    if int(assistant) == 1:
                       await client(ImportChatInviteRequest(invitelink))
                    if int(assistant) == 2:
                       await client2(ImportChatInviteRequest(invitelink))
                    if int(assistant) == 3:
                       await client3(ImportChatInviteRequest(invitelink))
                    if int(assistant) == 4:
                        await client4(ImportChatInviteRequest(invitelink))
                    if int(assistant) == 5:
                        await client5(ImportChatInviteRequest(invitelink))
                    if int(assistant) == 6:
                        await client(ImportChatInviteRequest(invitelink))
                    await event.reply(
                        f"Joined Successfully",
                    )
                except UserAlreadyParticipantError:
                    pass
                except Exception as e:
                    await event.reply(
                        f"__Assistant Failed To Join__\n\n**Reason**: {e}"
                    )
                    return
        return await mystic(event)

    return wrapper

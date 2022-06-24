import random
from typing import Dict, List, Union

ASSIDS = []
from Zaid import *
from telethon import *
from Zaid.helpers.assistant import get_assistant_details
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotParticipantError
)
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
            ran_ass = random.choice(random_assistant)
            assis = {
                "saveassistant": ran_ass,
            }
            await save_assistant(event.chat_id, "assistant", assis)
        else:
            ran_ass = _assistant["saveassistant"]
        if ran_ass not in random_assistant:
            ran_ass = random.choice(random_assistant)
            assis = {
                "saveassistant": ran_ass,
            }
            await save_assistant(event.chat_id, "assistant", assis)
        try:
            if int(assistant) == 1:
               b = await event.client(telethon.tl.functions.channels.GetParticipantRequest(event.chat_id, ASSID))
            if int(assistant) == 2:
               b = await event.client(telethon.tl.functions.channels.GetParticipantRequest(event.chat_id, ASSID2))
            if int(assistant) == 3:
               b = await event.client(telethon.tl.functions.channels.GetParticipantRequest(event.chat_id, ASSID3))
            if int(assistant) == 4:
               b = await event.client(telethon.tl.functions.channels.GetParticipantRequest(event.chat_id, ASSID4))
            if int(assistant) == 5:
               b = await event.client(telethon.tl.functions.channels.GetParticipantRequest(event.chat_id, ASSID5))
        except UserNotParticipantError:
            if event.chat_username:
                try:
                    await client1(functions.channels.JoinChannelRequest(channel=event.chat_username))
                except UserAlreadyParticipantError:
                    pass
                except Exception as e:
                    await event.reply(
                        f"__Assistant Failed To Join__\n\n**Reason**: {e}"
                    )
                    return
            else:
                try:
                    link = await event.client(ExportChatInviteRequest(event.chat_id))
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace(
                            "https://t.me/+", "https://t.me/joinchat/"
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
                        await cli1(ImportChatInviteRequest(invitelink))
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
        return await mystic(_, message)

    return wrapper

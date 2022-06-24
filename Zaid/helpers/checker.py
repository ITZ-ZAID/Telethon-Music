import random
from typing import Dict, List, Union

ASSIDS = []
from Zaid import Zaid as app
from telethon import *
from Zaid.helpers.assistant import get_assistant_details
from Zaid import random_assistant 
from Zaid.Database.clientdb import getassistant, save_assistant


def AssistantAdd(mystic):
    async def wrapper(event):
        _assistant = await getassistant(event.chat_id, "assistant")
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
            b = await app.get_chat_member(event.chat_id, ASS_ID)
        except UserNotParticipant:
            if event.chat_username:
                try:
                    await ASS_ACC.join_chat(message.chat.username)
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await event.reply(
                        f"__Assistant Failed To Join__\n\n**Reason**: {e}"
                    )
                    return
            else:
                try:
                    invitelink = await app.export_chat_invite_link(
                        message.chat.id
                    )
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace(
                            "https://t.me/+", "https://t.me/joinchat/"
                        )
                    if int(assistant) == 1:
                       await cli1(ImportChatInviteRequest(invitelink))
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
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await event.reply(
                        f"__Assistant Failed To Join__\n\n**Reason**: {e}"
                    )
                    return
        return await mystic(_, message)

    return wrapper

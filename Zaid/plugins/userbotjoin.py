
import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
from Config import SUDO_USERS
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Zaid.Database.clientdb import *
from Zaid import *


@Zaid.on(events.NewMessage(incoming=True, pattern=r"\[/!?]pjoin"))
@Zaid.on(events.NewMessage(incoming=True, pattern=r"\[/!?]privatejoin"))        
async def _(e):
    chat_id = e.chat_id
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.is_group:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            invitelink = umm[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
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
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
        
@Zaid.on(events.NewMessage(incoming=True, pattern=r"\[!?/]leave"))        
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SUDO_USERS:
        umm = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = umm[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

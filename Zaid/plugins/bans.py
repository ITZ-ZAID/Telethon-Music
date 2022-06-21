from Zaid import Zaid
from Zaid.status import *
from telethon import events, Button
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

BANS_TEXT = """
**✘ Some people need to be publicly banned; spammers, annoyances, or just trolls.**

‣ `?kickme` - To self Kick you from a chat.
‣ `?kick` - To kick someone from a chat.
‣ `?unban` - To unban a member from the chat.
‣ `?ban` - To Ban Someone from a chat.
‣ `?dban` - To delete the replied msg and bans the user.
‣ `?sban` - To delete the replied msg and kicks the user.
‣ `?skick` - To Delete Your msg and kicks the user 
‣ `?dkick` - To delete your msg and and kicks the replied user.
"""

@Zaid.on(events.NewMessage(pattern="^[!?/]kick ?(.*)"))
@is_admin
async def kick(event, perm):

    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to kick him")
        return

    replied_user = msg.sender_id
    us = msg.sender.username
    info = await Zaid.get_entity(us)
    await Zaid.kick_participant(event.chat_id, input_str or replied_user)
    await event.reply(f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@Zaid.on(events.NewMessage(pattern="^[!?/]kickme"))
async def kickme(event):

    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return

    check = await Zaid.get_permissions(event.chat_id, event.sender_id)
    if check.is_admin:
        await event.reply("Sorry but I can't kick admins!")
        return

    await event.reply("Ok, as your wish")
    await Zaid.kick_participant(event.chat_id, event.sender_id)

@Zaid.on(events.NewMessage(pattern="^[!?/]ban ?(.*)"))
@is_admin
async def ban(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply("You are missing the following rights to use this command:CanBanUsers!")
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to ban him")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await Zaid.get_entity(us)
    await Zaid(EditBannedRequest(event.chat_id, replied_user, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply(f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) in {event.chat.title}")

@Zaid.on(events.NewMessage(pattern="^[!?/]unban ?(.*)"))
@is_admin
async def unban(event, perm):
    if event.is_private:
        await event.reply("This cmd is made to be used in groups not PM")
        return
    if not perm.ban_users:
        await event.reply("You are missing the following rights to use this command:CanBanUsers!")
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("Reply to a user or give its username to unban him")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await Zaid.get_entity(us)
    await Zaid(EditBannedRequest(event.chat_id, replied_user, ChatBannedRights(until_date=None, view_messages=False)))
    await event.reply(f"Succesfully Unbanned [{info.first_name}](tg://user?id={replied_user}) in {event.chat.title}")

@Zaid.on(events.NewMessage(pattern="^[!?/]skick"))
@is_admin
async def skick(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete it and kick the user!")
        return

    us = reply_msg.sender.username
    info = await Zaid.get_entity(us)   
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await event.delete()
    await Zaid.kick_participant(event.chat_id, x)
    await event.reply(f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@Zaid.on(events.NewMessage(pattern="^[!?/]dkick"))
@is_admin
async def dkick(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete it and kick the user!")
        return
    us = reply_msg.sender.username
    info = await Zaid.get_entity(us) 
    x = await event.get_reply_message()
    await x.delete()
    await Zaid.kick_participant(event.chat_id, x.sender_id)
    await event.reply(f"Succesfully Kicked [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@Zaid.on(events.NewMessage(pattern="^[!?/]dban"))
@is_admin
async def dban(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete the message and ban the user!")
        return
    us = reply_msg.sender.username
    info = await Zaid.get_entity(us) 
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await zx.delete()
    await Zaid(EditBannedRequest(event.chat_id, x, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply("Successfully Banned!")
    await event.reply(f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@Zaid.on(events.NewMessage(pattern="^[!?/]sban"))
@is_admin
async def sban(event, perm):
    if not perm.ban_users:
         await event.reply("You are missing the following rights to use this command:CanBanUsers!")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("Reply to someone to delete the message and ban the user!")
        return
    us = reply_msg.sender.username
    info = await Zaid.get_entity(us) 
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await event.delete()
    await Zaid(EditBannedRequest(event.chat_id, x, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply(f"Succesfully Banned [{info.first_name}](tg://user?id={replied_user}) from {event.chat.title}")

@Zaid.on(events.callbackquery.CallbackQuery(data="bans"))
async def banhelp(event):
    await event.edit(BANS_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

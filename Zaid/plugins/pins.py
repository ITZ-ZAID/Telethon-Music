from telethon import events, Button, types
from Zaid import Zaid
from Zaid.status import *
import Config

PINS_TEXT = """
**✘ All the pin related commands can be found here; keep your chat up to date on the latest news with a simple pinned message!**

‣ `?pin` - To pinned a reply msg.
‣ `?unpin` - To Unpin the latest pinned msg.
‣ `?unpinall` - To unpinall all pinned msgs at once.
‣ `?pinned` - To get current pinned msg.

**➥Note:** __Add `notify` after ?pin to notify all chat members.__
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]pinned"))
async def get_pinned(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    chat_id = (str(event.chat_id)).replace("-100", "")

    Ok = await Zaid.get_messages(event.chat_id, ids=types.InputMessagePinned()) 
    tem = f"The pinned message in {event.chat.title} is <a href=https://t.me/c/{chat_id}/{Ok.id}>here</a>."
    await event.reply(tem, parse_mode="html", link_preview=False)

@Zaid.on(events.NewMessage(pattern="^[!?/]pin ?(.*)"))
@is_admin
async def pin(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("Reply to a msg to pin it!")
       return
    input_str = event.pattern_match.group(1)
    if "notify" in input_str:
       await Zaid.pin_message(event.chat_id, msg, notify=True)
       return
    await Zaid.pin_message(event.chat_id, msg)   

@Zaid.on(events.NewMessage(pattern="^[!?/]unpin ?(.*)"))
@is_admin
async def unpin(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    chat_id = (str(event.chat_id)).replace("-100", "")
    ok = await Zaid.get_messages(event.chat_id, ids=types.InputMessagePinned())
    await Stark.unpin_message(event.chat_id, ok)
    await event.reply(f"Successfully unpinned [this](t.me/{event.chat.username}/{ok.id}) message.", link_preview=False)

@Zaid.on(events.NewMessage(pattern="^[!?/]permapin"))
@is_admin
async def permapin(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs.")
       return
    msg = await event.get_reply_message()
    if not msg:
       await event.reply("Reply to a msg to permapin it.")
       return
    hn = await Zaid.send_message(event.chat_id, msg.message)
    await Zaid.pin_message(event.chat_id, hn, notify=True)


@Zaid.on(events.NewMessage(pattern="^[!?/]unpinall"))
async def unpinall(event, perm):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.pin_messages:
       await event.reply("You are missing the following rights to use this command:CanPinMsgs!")
       return
    UNPINALL = """
Are you sure you want to 
unpin all msgs?
This action can't be undone!
"""

    await Zaid.send_message(event.chat_id, UNPINALL, buttons=[
    [Button.inline("Confirm", data="unpin")], 
    [Button.inline("Cancel", data="cancel")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="unpin"))
async def confirm(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await Zaid.unpin_message(event.chat_id)
        await event.edit("Unpinned All Msgs!")
        return 

    await event.answer("Group Creator Required!")

@Zaid.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    check = await event.client.get_permissions(event.chat_id, event.sender_id)
    if check.is_creator:
        await event.edit("Unpinning of all msgs has been cancelled!")
        return 

    await event.answer("Group Creator Required!")


@Zaid.on(events.callbackquery.CallbackQuery(data="pins"))
async def _(event):

    await event.edit(PINS_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

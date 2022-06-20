from telethon import events, Button, types
from Zaid import Zaid
from Zaid.status import *
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import timedelta
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest


MISC_HELP = """
**✘ An "odds and ends" module for small, simple commands which don't really fit anywhere.**

‣ `?id` - To get current chat id or replied user id.
‣ `?info` - To get info of a user.
"""

@Zaid.on(events.NewMessage(pattern="^[!?/]id"))
async def id(event):

    if event.is_private:
       await event.reply(f"Your id is `{event.sender_id}`.")
       return

    ID = """
**Chat-ID:** `{}`
**User-ID:** `{}`
"""

    msg = await event.get_reply_message()
    if not msg:
      await event.reply(ID.format(event.chat_id, event.sender_id))
      return

    await event.reply(f"User {msg.sender.first_name} id is `{msg.sender_id}`.")
 
@Zaid.on(events.NewMessage(pattern="^[!?/]info ?(.*)"))
async def info(event):

    sed = await Stark(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    hn = await Stark(GetFullUserRequest(event.sender_id))
    text = "**✘ UserInfo:**\n\n"
    text += "**» Fɪʀsᴛ Nᴀᴍᴇ:** {}\n"
    text += "**» Lᴀsᴛ Nᴀᴍᴇ:** {}\n"
    text += "**» Usᴇʀ-ID:** `{}`\n"
    text += "**» Usᴇʀɴᴀᴍᴇ:** @{}\n"
    text += "**» Nᴏ. Oғ Pғᴘs:** `{}`\n"
    text += "**» Usᴇʀ-Bɪᴏ:** `{}`\n"
    text += "**» PᴇʀᴍᴀLɪɴᴋ:** [Link](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
          await Stark.send_message(event.chat_id, text.format(hn.user.first_name, hn.user.last_name, event.sender_id, event.sender.username, sed.count, hn.about, event.sender_id))
          return
 
    input_str = event.pattern_match.group(1)
    ha = await Stark.get_entity(input_str)
    hu = await Stark(GetFullUserRequest(id=input_str))
    sedd = await Stark(P(user_id=input_str, offset=42, max_id=0, limit=80))

    textn = "**✘ UserInfo:**\n\n"
    textn += "**» Fɪʀsᴛ Nᴀᴍᴇ:** {}\n"
    textn += "**» Lᴀsᴛ Nᴀᴍᴇ:** {}\n"
    textn += "**» Usᴇʀ-ID:** `{}`\n"
    textn += "**» Usᴇʀɴᴀᴍᴇ:** @{}\n"
    textn += "**» Nᴏ. Oғ Pғᴘs:** `{}`\n"
    textn += "**» Usᴇʀ-Bɪᴏ:** `{}`\n"
    textn += "**» PᴇʀᴍᴀLɪɴᴋ:** [Link](tg://user?id={})\n"

    await event.reply(textn.format(ha.first_name, ha.last_name, ha.id, ha.username, sedd.count, hu.about, ha.id))
   

@Zaid.on(events.callbackquery.CallbackQuery(data="misc"))
async def _(event):
    await event.edit(MISC_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

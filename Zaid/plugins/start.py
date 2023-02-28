from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}

• ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ʙᴏᴛ.
• ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ.
• ᴛʜɪꜱ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ. ꜱᴏ ɪᴛ'ꜱ ᴘʀᴏᴠɪᴅᴇ ᴍᴏʀᴇ ꜱᴛᴀʙɪʟɪᴛʏ ꜰʀᴏᴍ ᴏᴛʜᴇʀ ʙᴏᴛꜱ!
• ɪ ᴄᴀɴ ᴅᴏ ᴏᴛʜᴇʀ ᴛʜɪɴɢꜱ ʟɪᴋᴇ ᴘɪɴꜱ ᴇᴛᴄꜱ.

➻ **ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ**.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("✨ ᴀᴅᴅ ᴍᴇ", f"https://t.me/{BOT_USERNAME}?startgroup=true"), Button.inline("🥀 ʜᴇʟᴘ", data="help")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ ✅**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if Config.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("✨ ᴀᴅᴅ ᴍᴇ", f"https://t.me/{BOT_USERNAME}?startgroup=true"), Button.inline("🥀 ʜᴇʟᴘ", data="help")]])
       return

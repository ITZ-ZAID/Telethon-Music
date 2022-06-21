from Zaid import Zaid, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
Heya! {} ✅
✘ I'm a Simple Telegram Music And Management Bot.
‣ I can Play Songs in your Voice.
‣ I can Ban, mute every users.
‣ I have Almost all features which needs a music bot
‣ This Bot Based On Telethon. So It's provide more stability from other bots!
‣ I can Do other things like pins etcs.
‣ Click on help button 🔘 for more information ℹ️.
"""

@Zaid.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.reply(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ Add me To Your Chats", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Source Code", "https://github.com/ITZ-ZAID/Telethon-Music")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 Channel", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("Help And Commands", data="help")]])
       return

    if event.is_group:
       await event.reply("**I am alive 24/7!**")
       return



@Zaid.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ Add me To Your Chats", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("👨‍💻 Source Code", "https://github.com/ITZ-ZAID/Telethon-Music")],
        [Button.url("🗣️ Support", f"https://t.me/{Config.SUPPORT}"), Button.url("📣 Channel", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("Help And Commands", data="help")]])
       return

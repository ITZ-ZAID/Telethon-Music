from telethon import events, Button
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from Zaid import Zaid
from Zaid.status import *


CLEANER_HELP = """
**✘ This is A Module To Remove Deleted Accounts From Your Groups!**

‣ `?zombies` - To find zombies accounts in your chat.
‣ `?zombies clean` - To remove the deleted accounts from your chat.
"""


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@Zaid.on(events.NewMessage(pattern="^[!?/]zombies ?(.*)"))
@is_admin
async def clean(event, perm):
    if not perm.ban_users:
      await event.reply("You don't have enough rights")
      return
    input_str = event.pattern_match.group(1)
    stats = "Group is clean."
    deleted = 0

    if "clean" not in input_str:
      zombies = await event.respond("Searching For Zombies/Deleted Accounts...")
      async for user in event.client.iter_participants(event.chat_id):

            if user.deleted:
                deleted += 1
      if deleted > 0:
            stats = f"Found **{deleted}** Zombies In This Group.\
            \nClean Them By Using - `/zombies clean`"
      await zombies.edit(stats)
      return

    cleaning_zombies = await event.respond("Cleaning Zombies/Deleted Accounts...")
    del_u = 0
    del_a = 0

    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            try:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await cleaning_zombies.edit("I Don't Have Ban Rights In This Group.")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        stats = f"Cleaned `{del_u}` Zombies"

    if del_a > 0:
        stats = f"Cleaned `{del_u}` Zombies \
        \n`{del_a}` Zombie Admin Accounts Are Not Removed!"

    await cleaning_zombies.edit(stats)

@Zaid.on(events.callbackquery.CallbackQuery(data="zombies"))
async def _(event):
    await event.edit(CLEANER_HELP, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

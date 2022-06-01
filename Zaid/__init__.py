import os

from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from pytgcalls import PyTgCalls
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

STRING_SESSION = os.environ.get("STRING_SESSION", None)
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

bot = TelegramClient('Zaid', api_id=API_ID, api_hash=API_HASH)
Zaid = bot.start(bot_token=BOT_TOKEN)
client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
call_py = PyTgCalls(client)
client.start()
call_py.start()

from pytgcalls import PyTgCalls
from requests import get
from telethon import Button
from telethon.sync import TelegramClient, custom, events
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.tl.functions.channels import JoinChannelRequest as GetSec
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, custom, events
from telethon import Button, events, functions, types
from telethon.tl.types import InputWebDocument
from telethon.utils import get_display_name
from telethon import version
from math import ceil
from pathlib import Path
from datetime import datetime
import os

STRING_SESSION = os.environ.get("STRING_SESSION", None)
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)


telethon = TelegramClient(
    session=STRING_SESSION,
    api_id=API_ID,
    api_hash=API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
)
call_py = PyTgCalls(telethon)
call_py.start()

Zaid = TelegramClient(
    "Telethon",
    api_id=API_ID,
    api_hash=API_HASH,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=BOT_TOKEN)

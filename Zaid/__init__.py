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


from Config import *
BOT_USERNAME = BOT_USERNAME

bot = TelegramClient('Zaid', api_id=API_ID, api_hash=API_HASH)
Zaid = bot.start(bot_token=BOT_TOKEN)
client = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)

if STRING_SESSION2:
   client2 = TelegramClient(StringSession(STRING_SESSION2), API_ID, API_HASH)
   call_py2 = PyTgCalls(client2)
else:
   client2 = None
   call_py2 = PyTgCalls

if STRING_SESSION3:
   client3 = TelegramClient(StringSession(STRING_SESSION3), API_ID, API_HASH)
   call_py3 = PyTgCalls(client3)
else:
   client3 = None
   call_py3 = PyTgCalls(None)

if STRING_SESSION4:
   client4 = TelegramClient(StringSession(STRING_SESSION4), API_ID, API_HASH)
   call_py4 = PyTgCalls(client4)
else:
   client4 = None
   call_py4 = PyTgCalls(None)

if STRING_SESSION5:
   client5 = TelegramClient(StringSession(STRING_SESSION5), API_ID, API_HASH)
   call_py5 = PyTgCalls(client5)
else:
   client5 = None
   call_py5 = PyTgCalls(None)


call_py = PyTgCalls(client)

random_assistant = []
client.start()
call_py.start()
random_assistant.append(1)
random_assistant.append(6)

if client2:
   client2.start()
   call_py2.start()
   random_assistant.append(2)

if client3:
   client3.start()
   call_py3.start()
   random_assistant.append(3)

if client4:
   client4.start()
   call_py4.start()
   random_assistant.append(4)

if client5:
   client5.start()
   call_py5.start()
   random_assistant.append(5)

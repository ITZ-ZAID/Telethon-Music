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


from Config import Config
BOT_USERNAME = Config.BOT_USERNAME

bot = TelegramClient('Zaid', api_id=Config.API_ID, api_hash=Config.API_HASH)
Zaid = bot.start(bot_token=Config.BOT_TOKEN)
client = TelegramClient(StringSession(Config.STRING_SESSION), Config.API_ID, Config.API_HASH)

if not Config.STRING_SESSION2:
   client2 = None
else:
   client2 = TelegramClient(StringSession(Config.STRING_SESSION2), Config.API_ID, Config.API_HASH)

if not Config.STRING_SESSION3:
   client3 = None
else:
   client3 = TelegramClient(StringSession(Config.STRING_SESSION3), Config.API_ID, Config.API_HASH)

if not Config.STRING_SESSION4:
   client4 = None
else:
   client4 = TelegramClient(StringSession(Config.STRING_SESSION4), Config.API_ID, Config.API_HASH)

if not Config.STRING_SESSION5:
   client5 = None
else:
   client5 = TelegramClient(StringSession(Config.STRING_SESSION5), Config.API_ID, Config.API_HASH)


call_py = PyTgCalls(client)
call_py2 = PyTgCalls(client2)
call_py3 = PyTgCalls(client3)
call_py4 = PyTgCalls(client4)
call_py5 = PyTgCalls(client5)
random_assistant = []
client.start()
call_py.start()
random_assistant.append(1)
random_assistant.append(6)

if Config.STRING_SESSION2 != "None":
   client2.start()
   call_py2.start()
   random_assistant.append(2)

if Config.STRING_SESSION3 != "None":
   client3.start()
   call_py3.start()
   random_assistant.append(3)

if Config.STRING_SESSION4 != "None":
   client4.start()
   call_py4.start()
   random_assistant.append(4)

if Config.STRING_SESSION5 != "None":
   client5.start()
   call_py5.start()
   random_assistant.append(5)

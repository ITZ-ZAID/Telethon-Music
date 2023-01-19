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
ASSISTANT_ID = Config.ASSISTANT_ID

Zaid = TelegramClient('Zaid', api_id=Config.API_ID, api_hash=Config.API_HASH)


client = TelegramClient(StringSession(Config.STRING_SESSION), Config.API_ID, Config.API_HASH)
call_py = PyTgCalls(client)


class Bot(TelegramClient):
    def __init__(self):
        super().__init__(
        "shortener",
        api_id=API_ID,
        api_hash=API_HASH,
        )
    async def start(self): 
        await super().start(bot_token=Config.BOT_TOKEN) 
        await Zaid.start(bot_token=Config.BOT_TOKEN)
        await client.start()
        await call_py.start()
        print('Bot started')


    async def stop(self, *args):
        await super().stop()
        print('Bot Stopped Bye')

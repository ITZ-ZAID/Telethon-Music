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
Zaid.start(bot_token=Config.BOT_TOKEN)

client = TelegramClient(StringSession(Config.STRING_SESSION), Config.API_ID, Config.API_HASH)
call_py = PyTgCalls(client)
client.start()
call_py.start()

class Bot():
    async def start():
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"       
        await web.TCPSite(app, bind_address, PORT).start()     
        print(f"🕸️ Web 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 ⚡️⚡️⚡️")


    async def stop(*args):
        print('Bot Stopped Bye')

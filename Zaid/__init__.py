

from telethon import TelegramClient
import logging

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

STRING_SESSION = os.environ.get("STRING_SESSION", None)
API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

bot = TelegramClient('Zaid', api_id=Config.APP_ID, api_hash=Config.API_HASH)
Zaid = bot.start(bot_token=BOT_TOKEN)

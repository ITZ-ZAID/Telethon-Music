from motor.motor_asyncio import AsyncIOMotorClient as Bot
import Config

tmo = Config.MONGO_DB_URL


MONGODB_CLI = Bot(tmo)
db = MONGODB_CLI.program

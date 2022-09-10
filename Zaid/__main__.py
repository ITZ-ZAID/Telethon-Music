import asyncio
import telethon
import glob
from pathlib import Path
from Zaid.utils import load_plugins
import logging
from Zaid import Zaid
from Zaid import client, ASSISTANT_ID

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Zaid/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
async def start_bot():
     print("[INFO]: LOADING ASSISTANT DETAILS")
     botme = await client.get_me()
     botid = telethon.utils.get_peer_id(botme)
     ASSISTANT_ID.append(botid)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())

print("[INFO]: SUCCESSFULLY STARTED BOT!")
print("[INFO]: VISIT @TheUpdatesChannel")

if __name__ == "__main__":
    Zaid.run_until_disconnected()

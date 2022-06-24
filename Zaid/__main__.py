
import asyncio
import glob
import telethon
from pathlib import Path
from Zaid.utils import load_plugins
import logging
from Zaid import * 

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
    print("[INFO]: STARTING BOT CLIENT")
    if client:
       botme = await client.get_me()
       botid = telethon.utils.get_peer_id(botme)
       ASSID.append(botid)
    if client2:
       botme2 = await client2.get_me()
       botid2 = telethon.utils.get_peer_id(botme2)
       ASSID2.append(botid2)
    if client3:
       botme3 = await client3.get_me()
       botid3 = telethon.utils.get_peer_id(botme3)
       ASSID3.append(botid3)
    if client4:
       botme4 = await client4.get_me()
       botid4 = telethon.utils.get_peer_id(botme4)
       ASSID4.append(botid4)
    if client5:
       botme5 = await client5.get_me()
       botid5 = telethon.utils.get_peer_id(botme5)
       ASSID5.append(botid5)
    
print("Successfully Started Bot!")
print("Visit @TheUpdatesChannel")

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
if __name__ == "__main__":
    Zaid.run_until_disconnected()

import asyncio
import telethon
import glob
from pathlib import Path
from Zaid.utils import load_plugins
import logging
from Zaid import Bot, Zaid
from Zaid import client, ASSISTANT_ID
from Zaid.plugins.autoleave import leave_from_inactive_call


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "Zaid/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))




print("[INFO]: SUCCESSFULLY STARTED BOT!")
print("[INFO]: VISIT @TheUpdatesChannel")


if __name__ == "__main__":
    Bot()
    Zaid.run_until_disconnected()

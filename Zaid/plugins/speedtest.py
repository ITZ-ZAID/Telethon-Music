from telethon import Button, events

from Zaid import *

import asyncio
import speedtest

# Commands

def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        test.download()
        test.upload()
        test.results.share()
        result = test.results.dict()
    except Exception as e:
        return
    return result

@Zaid.on(events.NewMessage(pattern="^/speedtest"))
async def speedtest_function(message):
    m = await message.reply("Running Speed test")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**Speedtest Results**
    
**Client:**
**__ISP:__** {result['client']['isp']}
**__Country:__** {result['client']['country']}
  
**Server:**
**__Name:__** {result['server']['name']}
**__Country:__** {result['server']['country']}, {result['server']['cc']}
**__Sponsor:__** {result['server']['sponsor']}
**__Latency:__** {result['server']['latency']}  
**__Ping:__** {result['ping']}"""
    await Zaid.send_file(message.chat.id, result["share"], caption=output)
    await m.delete()

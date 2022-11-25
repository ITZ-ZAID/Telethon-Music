import os
import random

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont
import os
from os import path
import aiohttp
import aiofiles
from typing import Union
from asyncio import QueueEmpty
from PIL import (Image, ImageDraw, ImageEnhance, ImageFilter,
                 ImageFont, ImageOps)
from PIL import ImageGrab
from typing import Callable
import numpy as np

colour = ["red", "pink", "white", "black", "orange", "yellow", "green"]

def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def truncate(text):
    list = text.split(" ")
    text1 = ""
    text2 = ""    
    for i in list:
        if len(text1) + len(i) < 27:        
            text1 += " " + i
        elif len(text2) + len(i) < 25:        
            text2 += " " + i

    text1 = text1.strip()
    text2 = text2.strip()     
    return [text1,text2]


async def gen_thumb(thumbnail, title, userid, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open("background.png", mode="wb")
                await f.write(await resp.read())
                await f.close()

    img = Image.open(f"./background.png")
    image1 = changeImageSize(1280, 720, img)
    image = ImageOps.expand(image1, border=20, fill="blue")    
    image.save(f"final.png")
    os.remove(f"background.png")
    final = f"final.png" 
    return final

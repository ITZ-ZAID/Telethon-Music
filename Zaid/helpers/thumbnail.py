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

    image = Image.open(f"./background.png")
    black = Image.open("resources/black.jpg")
    img = Image.open("resources/robot.png")
    theme = random.choice(colour)
    imsg = Image.open(f"resources/IMG_20220914_192313_722.jpg")
    image6 = changeImageSize(1280, 720, imsg)
    image5 = changeImageSize(1280, 720, img)
    image1 = changeImageSize(1280, 720, image)
    image1 = image1.filter(ImageFilter.BoxBlur(10))
    image11 = changeImageSize(1280, 720, image)
    image1 = image11.filter(ImageFilter.BoxBlur(10))
    image2 = Image.blend(image1,black,0.6)

    # Cropping circle from thubnail
    youtube = image11
    # image3 = image11.crop((280,0,1000,720))
    #lum_img = Image.new('L', [720,720] , 0)
    #draw = ImageDraw.Draw(lum_img)
    #draw.pieslice([(0,0), (720,720)], 0, 360, fill = 255, outline = "white")
    #img_arr =np.array(image3)
    #lum_img_arr =np.array(lum_img)
    #final_img_arr = np.dstack((img_arr,lum_img_arr))
    #image3 = Image.fromarray(final_img_arr)
    Xcenter = youtube.width / 2
    Ycenter = youtube.height / 2
    x1 = Xcenter - 250
    y1 = Ycenter - 250
    x2 = Xcenter + 250
    y2 = Ycenter + 250
    image3 = youtube.crop((x1, y1, x2, y2))
    image3.thumbnail((340, 340), Image.ANTIALIAS)
    image3 = ImageOps.expand(image3, border=10, fill=f"{theme}")    
    image2.paste(image6)
    image2.paste(image3, (40,355))

    # fonts
    font1 = ImageFont.truetype(r'resources/robot.otf', 30)
    font2 = ImageFont.truetype(r'resources/robot.otf', 60)
    font3 = ImageFont.truetype(r'resources/robot.otf', 40)
    font4 = ImageFont.truetype(r'resources/Mukta-ExtraBold.ttf', 35)

    image4 = ImageDraw.Draw(image2)

    # title
    title1 = truncate(title)
    image4.text((10, 10), text=title1[0], fill=f"{theme}", font = font3, align ="left") 

    # description
    views = f"Requester id: {userid}"
    channel = f"Playing on: {ctitle}"
    my = "Powered By Zaid"  

    
    image2.save(f"final.png")
    os.remove(f"background.png")
    final = f"final.png" 
    return final

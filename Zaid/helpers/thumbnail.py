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
from PIL import Image, ImageFont, ImageDraw, ImageFilter
from PIL import ImageGrab
from typing import Callable
import numpy as np


themes = ["rrc", "hejo", "black"]


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
    black = Image.open("resources/square.jpeg")
    img = Image.open("resources/robot.png")
    image5 = changeImageSize(1280, 720, img)
    image1 = changeImageSize(1280, 720, image)
    image1 = image1.filter(ImageFilter.BoxBlur(10))
    image11 = changeImageSize(1280, 720, image)
    image1 = image11.filter(ImageFilter.BoxBlur(10))
    image2 = changeImageSize(1280, 720, black)

    # Cropping circle from thubnail
    image3 = image11.crop((280,0,1000,720))
    #lum_img = Image.new('L', [720,720] , 0)
    #draw = ImageDraw.Draw(lum_img)
    #draw.pieslice([(0,0), (720,720)], 0, 360, fill = 255, outline = "white")
    #img_arr =np.array(image3)
    #lum_img_arr =np.array(lum_img)
    #final_img_arr = np.dstack((img_arr,lum_img_arr))
    #image3 = Image.fromarray(final_img_arr)
    image3 = image3.resize((475,475))
    

    image2.paste(image3, (405,120))

    # fonts
    font1 = ImageFont.truetype(r'resources/robot.otf', 30)
    font2 = ImageFont.truetype(r'resources/robot.otf', 60)
    font3 = ImageFont.truetype(r'resources/robot.otf', 49)
    font4 = ImageFont.truetype(r'resources/Mukta-ExtraBold.ttf', 35)

    image4 = ImageDraw.Draw(image2)

    # title
    views = f"Now Streaming"
    channel = f"Playing on : {ctitle}"
    my = "Powered By Zaid"  

    image4.text((10, 10), text=views, fill="yellow", font = font2, align ="left") 
    image4.text((880, 670), text=my, fill="blue", font = font3, align ="left")
    
    image2.save(f"final.png")
    os.remove(f"background.png")
    final = f"final.png" 
    return final

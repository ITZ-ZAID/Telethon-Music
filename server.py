import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, Telethon Music Bot Is Running!'

os.system("ls && python3 -m Zaid")

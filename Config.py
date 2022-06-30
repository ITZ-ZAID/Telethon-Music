import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "10271892"))
    API_HASH = os.environ.get("API_HASH", "e37ec7877d9dcaeaa59e9864bf1476db")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5417392757:AAFt3O1iesTxa44Vi5xR7x9Qow_HjQfF1nI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLEBu24_FjOfkRmjz8sJRtjE6ttZECcL_keOi6j_mUp3UGNZT-t4sGXteiMR64RNKtPJz9IqAIY4C-5Wsqcnv4VSBUksGq6nbtrFBwjy_woPbYqfuvl_LTj5XjAXuGy2FzHhhseTwPCJIvxMvYRmxDkwU-HnqkGSbua1ar0F5Mx9hwjvRRsEDrG5oLOEAh4OZ5MVpGnkw8J7U8h5wx9OrLoZSmWcJ6hCn9tNIiKTBGDI1XOpaFsP9IAJ5O2fVees1eXSTgJQqLSLN-_O2LJZddFxmZXCcDIK2IR5zKON7E45QfJ8YU6asv5c1DjizVoU8P9aO-aoMY3r_gdNPKLxZ1LZ3-o=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", ENABLE)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ultramanre_bot")
    SUPPORT = os.environ.get("SUPPORT", "ygabutkan")
    CHANNEL = os.environ.get("CHANNEL", "ygabutkan")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b167d1dce40b9011892d7.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/b167d1dce40b9011892d7.jpg")

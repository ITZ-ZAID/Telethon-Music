import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17699977"))
    API_HASH = os.environ.get("API_HASH", "c79893218b48242a5b0239c490e98b6f")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5747704377:AAGrviWJEB7iq355NN5dPCb_hCGNADVU4aI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQAO8iU2daU7PD9Gzdg5mXWkbylqTZMI6Df1ot4NYBgQF7PdOGc7vQKrtMpcL8LJuZXftifOtlJmQkvfBBJgBZYW6hOxQn0FapNGsSI2n6pZlo2qxQ_ejn9yUcFaq39i773SMwWX6tUN6cDlCyx33jIZWA9ArhhIpK0u6p9ha5hULakMNYO-kBEVDBuceVuLpnmR4nBKTJ4nh6N1wu9jO-b_XUULfJOQrtgt-JMrjNcz0iCCDDCDMfSea-pVKfXKtJ8utCWdk4qIiYQqLk2jqt_jRcM8A-7pxsUe2-VqVnxlbWyxdMBA33w_f4GjypFhviC-gycoVhfJ2c1120j0TBgLAAAAAUgr-_wA")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Lebanon1bot")
    SUPPORT = os.environ.get("SUPPORT", "https://t.me/U_2_6")
    CHANNEL = os.environ.get("CHANNEL", "https://t.me/U_2_6")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/e2b093bec37daa011537a.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/e2b093bec37daa011537a.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "17699977"))

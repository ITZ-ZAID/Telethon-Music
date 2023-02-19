import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6122404059:AAG7Mw9RtMSxl7TT3H3uU2Fj1K2bgz9Ywwc")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOGkBuxv5nutJBM-SkeB52igR6bGSOWdkL1fTrOlOkRGdTL064LBO6T4rLpS1RQFWQrtbNgJfh1JeW-Em1ERv0i9FE-hSlZrFcE_uKCBA1urYinwhGlRfN5zcck8QYvYTqWW7GDdmuysSMAmv8J3JfvwdRjMuWh_Sye9vj7vhnPT1NuG2BAL5hJ8nwKZQhKqgFjzWdnBIKCbYM_Ng7k_del-WF912pONbutM5xe02ve2zFdVZB03-Wv-kytb-33bN7bkclwubwUCwsdEgDojn1O0_VR3IqcxT-dloD0I-BgCPQvx5TGtY3TXWeGGtbgFkmOngvxaARgzEk4jpKdYD7lI4Sq4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

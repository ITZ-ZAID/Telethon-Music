import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "16715400"))
    API_HASH = os.environ.get("API_HASH", "2de611a73f73b8da8b0bcee9f855c815")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5417392757:AAFt3O1iesTxa44Vi5xR7x9Qow_HjQfF1nI")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLEBuy9P--UOAa1qJnEakRAZtpIBLlO9xgIvDraX_aKze9wNAHPEfsOqgIHyr1_JiqWbbUt0nx9wBYnnHfAw9JFB3CqVGuqxp4tam0xh2puIFb9pmVSZsjuSCx42od-Fj-G98Uby6TxKEON8-RiM2JvNRkeRMvG86kNU_BY_AX2i9iIilDwbzm6NeEPpNmB2GvbhzS8J4s6yABfk0ACM4avHjTnhcdDR_RVUk6LI24IGGumzyYlwzmH0KSfKqPiuwH9hStFPPcn2aTvG3Ax6lqCM8GcM_WmZCORNKwGujxZEURNdSs43Rp9ttV8e8HWwyB0LO9Jjeiv9uawDQ4x8Ox0QV8c=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", ENABLE)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "ultramanre_bot")
    SUPPORT = os.environ.get("SUPPORT", "ygabutkan")
    CHANNEL = os.environ.get("CHANNEL", "ygabutkan")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b167d1dce40b9011892d7.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/b167d1dce40b9011892d7.jpg")

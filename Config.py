import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5638976866:AAHfN7aRo1-9AUkaqQ8suauN33YcD2HkWV8")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQC4sGYAh3emE-gnr2dFULcWrtecrdNriWi2SoLkup6HemQhc5Z-waNCtukHYVSZor1cDTrYyq1pu81MKHRV0_VvRUNDuyyqeqpdh0BNigiwnc08zzd3XO8ZCMCzE_yt2mu6FxDDn1x-pUHvtbgdSeYVecXEt-wEgBAsgPbVvstO9zSVqtK8s8U_8KichwuOPX9r1GIlpEheu_ZWlt0PpcuRHz3xde6aQk5aCuDvgsbXqy_0fzdOdiWUDokP_Uh_29sOTpfCXEtC_o5c-phfn0crtYjZOtv3zZBNUrwgomp7Hj8_EyrlJLpQTFTrfThfc_KNJKr6bPgU_XdINV1Q_gGNby8t-gAAAAFU_2aVAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

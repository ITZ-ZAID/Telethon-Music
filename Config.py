import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22933157"))
    API_HASH = os.environ.get("API_HASH", "6d2cc7ff042b759b47d5b67a9efaecdc")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5800281444:AAESBRyIEpilLGpjCM46Mks09fJuPMhBIpg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCe9BUpjYVgrC6jRS4Nky0BsNNYjTBQnOfNXfgAMSHWZCMuxk98TcQu5MYvhXAePEQINGekmoWH-kBPq4o6UZ8CiruCoXETd0H8RaAOpZ6yiCDnK6TKWerTUjTbtqo2i49cb1_PXfd3SCwawFfaxE73Fx8T-gbnkPoDRNbuxbYMOwJSSl7S3xxerkTGcWZJ7emTNUbUFD2AEUEKVBrWJNPMzpfr4ddrGwDm7vHRwsLMBdcLNebBkGcbiCGXYdCSyNDQJMTmH9OaS5MPPAx4esKq7BbuBKNX77WazUfDVbCdv3GUCCaLfOMmV6d8Of6Ec-bDbQdqOFU2EnRgyYusYaT4LAkD5gA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Youngster_musix_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "738788326")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

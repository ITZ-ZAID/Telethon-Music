import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "23132894"))
    API_HASH = os.environ.get("API_HASH", "086ce7d5bfe47ee79ec819d452afd096")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6512188836:AAG1gzYAeCsoPfyuFI-g8W4lnq0WwsEozh0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu3qYwAptO3xpQShu4w2gH0_MVjHLJMGdVVb_r9F27t61AhCOtZRQPz6GF0wqZhjifNLiPXTJIACgRZCJZswTVA8hJwbsQUc3vHajbkVMTYvpifek2MSYWMGi09pw4MQbjD2nK03WD6-WFeJL4h7h--LeYGzGPdJh45HCDeMmfPuCrJvf76JFJlsv5Na4Ee0WphC0cG375rZ55eonNdDIbR6y7j-xQm9zeM5r04rBQzhfiPrrY9OSu23qPbtf-cU1dz1uhBQ-qPf4IwWKdwvvnDvMvINSqHzO_ApAhuXNLpaQRrdeStpMA6sHVYuFM20dtFpQ7dgltRKWf5tm0GOYRk4=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "RagnarMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5919106876")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

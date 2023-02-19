import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6232264247:AAHa8-_ym-bJgc7z5QybTvr3d9PgGgYY6D0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKEBu61oklAem5hEy1ItgTviWy0MSctloGtWpsF4b6cZcwuBCINzHaAv5o8MIq_LxyqfL_3QgmfTi0BIuNvL7IytNondzHW5nKiq4DnMX_HuIxBnxgPElgV71dBFStMEauYeWjne6Cpfmo_wcZhf5dX8RZG0fAmM447LJL6V2ttSgmdP198lpuj7b0qxKn1rUfSqeQ91NIcQx6rG9R9JETuZyTlEo2NxnUyBf37p2p0fEwM5FWYQgrs3dOiVLN07owBQW66rgdfRPlE26ps6xRHowfMRvE8B2dUB0ORqdSVq4UNXprH9KStumwAL-UJ5ZzFP-0zu7ImzPOzVOHLnUa-ODcE=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Yash_45music_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1246614686")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

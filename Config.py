import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20879666"))
    API_HASH = os.environ.get("API_HASH", "bad13c21c74240c60e1820fee35923c2)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCHalwL9PkmzsJ6wTnGLpJgEN0gEMVZFhMEPgTBqm5D-5qqFwOCrDh8L93ljIZdVTroriXd_IttuXexbBhe68jXq7YCXQJbZGjwNaMTy6JP1PEYKXhjST4QfpAMW77EN_5q876_L68VYYrFaWKYj7ycePGEzOn2qahnauYEWhjDDQXJBt7mbBlXVmLnpXkxD2vBhzIrvMYjWTm8CJKvMKKiRwPng-LLSMS0zcA88KwA4JIKBiug89XnQ8wLD90HRFsfKuvYMxaDbcPQKGsChKkW_uOBDxDONiAly3amoOfy52XpfblOeoPbrv4wUfmIbgZ9suiFlNHqUaJ7eXsFpgaDAAAAAYYlMwEA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6545552129")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "120000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

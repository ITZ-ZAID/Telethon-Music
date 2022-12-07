import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5917487076:AAEoliWwwPv4oTUvBwt56G28XfCA-IIvuuE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLIBux7gycIK7k8jOnI59ctd3B_D7oMbhcSBaDCPMmoqIB7NlZzNJ-rq2adtnpVdr4TYB65wSznl8kxPGTwwoRQUJEipkxrbxrXSHec0_-Q1pbUPWEeAEedzQQB4JxDQOgaxs22p5_kJL85iwlq48p5PYwxm8IVETKflyrpUa8PcSZezt6-dYYz6vk_F3CHFqL15D2vAtrdkv9qUibVr_SNvdLTtY5qqeAP_cE1G1Ip5_iGdILi5FFoX5CpbBXHN5W9UkcVttp-8H9nTuvF6-3eS-ORkVgm62PMSEVEz4ugs5q0ktYo9zwy3zP3se7RnxA1sm3aPrO05JTD0m6xZF68dHPA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Anak_ajg_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5917487076")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

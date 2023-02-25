import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "22667581"))
    API_HASH = os.environ.get("API_HASH", "be4eb814a7bf7b61d6ec7e6466e74af7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5800281444:AAG3zrbbIj-ejkgN5525nZHlZ86WiS12pHg")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLMBu2Qe5i__cMBI3XylzQlNoTcQ38UgxqZqG978JXZ5nhmcvhwWgXrLLE9-LMES2ln4W1YvMovRzIbDhif0-Cvvka0MwJzRXW-7KT6D9T-WGbENeI_2_4DsI8TEpIriYWVQmsaTpZrOCGYVB-4x4hciatkNWYSSvVR9BsnjLl6ZJ09uVH38YDiokWvgQ2XpKKO7P-O7Zk1LkQvE-tKoYLwoszXZbT16be3WHKiYy1aqslvaRJjgLOggsojOj5NOY7yRB_ZAtrSICYGK3KQzaa9yYORD0qCIwVZXwtKbD3aosrZF4jsPpMjba1Wz1jdF8B1MekWHs5XhLc78HE_jmqm9u3g=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@Youngster_musix_bot")
    SUPPORT = os.environ.get("SUPPORT", "Youngster_fed") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "youngster_music") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5800941593")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "60000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"

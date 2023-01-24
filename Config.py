import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6296490"))
    API_HASH = os.environ.get("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5897701792:AAFIJ8NlfS5NwU3CrnO9RVsm7scvYs1j46k")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1sBu0uhlXBSKci9upQFQS562rsLqU2ONrevbiOHqTNAlFX-ApBhgbLZIUftzHCukOwb27UN2ITfF3MvHtp8MXyjWOfCqAWu69wlxZew-5fJkIG9tKcXga7WtYe0ZF61ZGFElvTTDKubmqohAnapXlR2CahnOoxOoN6BLPW3C70lWotYtnx70mGiG_WSCZ5JX_33lSdezw5erv0thvlCQSLJFapo4QQ6ESKfeLjMo1_tGM7SCRoaS6ZgPzL7nwW07T-DFEQx1bY7PUwGuda2TWkAo-wmIZWuBkls5gutzTxleyErDCaPg6uNoTOydotVyg50b5NsV2Q6Z-AMZ9WEKBpxGWc=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "hckxbot")
    SUPPORT = os.environ.get("SUPPORT", "chhoti_bachi_angel") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "chhoti_bachi_angel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/7e5b79d224638c0d1a38f.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/7e5b79d224638c0d1a38f.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5467311248")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', "True") # Change it to "True"

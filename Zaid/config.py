# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "6435225"  
    API_HASH = "4e984ea35f854762dcde906dce426c2d"
    TOKEN = "5012762229:AAFda4MOon4s8P38EzWr1PZTimPOYwQr3-0"
    OWNER_ID = "1669178360"
    OWNER_USERNAME = "Timesisnotwaiting"
    MONGO_DB_URI = "mongodb+srv://music:music@cluster0.sh6h4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    SUPPORT_CHAT = "Superior_Support"
    JOIN_LOGGER = (
        -1001568185563
    )   
    EVENT_LOGS = (
        -1001568185563
    )  

    # RECOMMENDED
    INFOPIC = "https://telegra.ph/file/be24bbabbe0ec30dff489.jpg"   
    CF_API_KEY = ""
    LASTFM_API_KEY = ""
    BOT_USERNAME = "Zaid2_Robot"
    WALL_API = ""
    OPENWEATHERMAP_ID = ""
    TEMP_DOWNLOAD_DIRECTORY = ""
    REM_BG_API_KEY = ""
    TIME_API_KEY = ""
    CASH_API_KEY = ""
    REM_BG_API_KEY = ""
    SESSION_STRING = "1AZWarzYBu6lLskBZ0pY_9eQp5ge87Z8Bou0X39X5Kp0TI7Q4e1_ZAQ1Bp9J0lHNOC7N7wqx49-3jBqRJrBXoG9o-lkK8RcDHbfWP55iCqr7KrXrjI5PWfbE9FchN-gZv_yxpBtk9SCOz8YlFQRASclPnlqpvQiiolWHL7Nb1Qlw44Q2DhoMPoE9QlgF-gnYubS1mz7NYCAZ7Kb2xoWHrZM8I1IhrONSv3GrYSGeC6-Rh1yZvdlSQVtbIi5bI1ONE7K5Z9g_BXISLMlGg0Qyjfi7P08ofuD4vJXiOjTXnYLF-QomcGrziF141P_X3XX862UBJVVRFXytRIXipfkWo0iTXqtOM-Q8="
    ARQ_API_KEY = "UIUXOY-NTKWDC-QHFFMD-DHHKVV-ARQ"
    ARQ_API = "UIUXOY-NTKWDC-QHFFMD-DHHKVV-ARQ"
    ARQ_API_URL = "aww"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = ""
    BOT_ID = "5012762229"
    STRING_SESSION = "1AZWarzYBu6lLskBZ0pY_9eQp5ge87Z8Bou0X39X5Kp0TI7Q4e1_ZAQ1Bp9J0lHNOC7N7wqx49-3jBqRJrBXoG9o-lkK8RcDHbfWP55iCqr7KrXrjI5PWfbE9FchN-gZv_yxpBtk9SCOz8YlFQRASclPnlqpvQiiolWHL7Nb1Qlw44Q2DhoMPoE9QlgF-gnYubS1mz7NYCAZ7Kb2xoWHrZM8I1IhrONSv3GrYSGeC6-Rh1yZvdlSQVtbIi5bI1ONE7K5Z9g_BXISLMlGg0Qyjfi7P08ofuD4vJXiOjTXnYLF-QomcGrziF141P_X3XX862UBJVVRFXytRIXipfkWo0iTXqtOM-Q8="
    SQLALCHEMY_DATABASE_URI = "postgres://kfxheqenczaskf:9cb540dea5cafdc14b441d70bc51613f4f7e51ce2b199ff265520a022015da86@ec2-35-153-239-126.compute-1.amazonaws.com:5432/d13g4j50j3vjlk"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1669178360"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1669178360"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1669178360"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1669178360"
    WOLVES = "1669178360"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    ALLOW_CHATS = True
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //

from telethon import TelegramClient, events
from decouple import config
import logging
import time
import os
from telethon import TelegramClient as ATGK

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

Lastupdate = time.time()
yoo = logging.getLogger("WARNING")
yooprint = logging.getLogger("WARNING")

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
LOGGER_GROUP = int(os.environ.get("LOGGER_GROUP", None))
BOT_USER = os.environ.get("BOT_USER")
BOT_USERS = str(BOT_USER).split(" ", maxsplit=len(BOT_USER))
ALIVE_NAME = os.environ.get("ALIVE_NAME", "DICTATOR AMAAN")

if 511112479 not in BOT_USER:
    BOT_USER.append(511112479)
OWNER_ID = int(os.environ.get("OWNER_ID", None))
BOT_USER.append(OWNER_ID)

ATGK = TelegramClient('ATGK', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 

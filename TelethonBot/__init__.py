# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //

from telethon import TelegramClient, events
from decouple import config
import logging
import time
from telethon import TelegramClient as ATGK

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SUDO_USERS = config("SUDO_USERS", default=None)


ATGK = TelegramClient('ATGK', APP_ID, API_HASH).start(bot_token=BOT_TOKEN) 

# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //


from . import *
from .. import ATGK, ALIVE_NAME
from telethon import events, Button


ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "SPAMMER BOT"

@ATGK.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    await event.reply("SPAMMER BOT FOR {ALIVE_NAME} MADE BY @CRiMiNaL786",
                    buttons=[
                        [Button.inline("Check Me",data="helpme")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I Am SPAMMER BOT!\nI SPAM FOR MY MASTER.\n\nTry Me!! Request Code in Support Group!"
    await event.edit(text,
                     buttons=[
                         [Button.url("CHANNEL", url="https://t.me/destroyxSupport")],
                         [Button.url("GROUP", url="https://t.me/DesTRoYxOfficial")],
                         [Button.url("GIVE STAR⭐", url="https://github.com/CRiMiNaL786")],
                         [Button.inline("Fuck", data="2")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="2"))
async def ex(event):
    await event.edit(text,
                     buttons=[
                         [Button.inline("BacK", data="helpme")]
                     ])

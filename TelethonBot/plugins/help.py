# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //


from . import *
from .. import ATGK
from telethon import events, Button

@ATGK.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    await event.reply("SPAMMER BOT FOR @HACKERPREM MADE BY @CRiMiNaL786",
                    buttons=[
                        [Button.inline("Click HeRe",data="helpme")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I am SPAMMER BOT!\nI can SPAM for you.\n\nTry Me!! Make sure to join my channel and support me!"
    await event.edit(text,
                     buttons=[
                         [Button.url("Channel", url="https://t.me/Javes2Support")],
                         [Button.url("Repository", url="https://github.com/Javes786")],
                         [Button.inline("Fuck", data="2")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="2"))
async def ex(event):
    await event.edit("SoRRY , Because There is No BacK Button Adding Soon")

# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //

from .. import ATGK
from telethon import events, Button

@ATGK.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Some iNFoRMaTioN AbouT Me!",
                    buttons=[
                        [Button.url("OWNER", url="https://t.me/CRiMiNaL786")],
                        [Button.inline("Commands",data="1")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="1"))
async def ex(event):
    await event.edit("Check /help ")





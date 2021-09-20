# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //

from .. import ATGK
from telethon import events, Button

@ATGK.on(events.NewMessage(incoming=True, pattern="/start"))
@ATGK.on(events.callbackquery.CallbackQuery(data="2"))
async def start(event):
    await event.reply("ѕοмє ιиƒο αϐουτ οωиєя.",
                    buttons=[
                        [Button.url("οωиєя", url="https://t.me/CRiMiNaL786")],
                        [Button.inline("Cнєϲκ мє",data="1")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="1"))
async def ex(event):
    await event.reply("υѕє τнιѕ ρℓєαѕє `/help`,
                    buttons=[
                        [Button.inline("ϐαϲκ",data="2")]
                    ])





# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //

from .. import ATGK
from telethon import events, Button

@ATGK.on(events.NewMessage(incoming=True, pattern="/start"))
@ATGK.on(events.callbackquery.CallbackQuery(data="shu"))
async def start(event):
    await event.send("ѕοмє ιиƒο αϐουτ οωиєя.",
                    buttons=[
                        [Button.url("οωиєя", url="https://t.me/CRiMiNaL786")],
                        [Button.inline("Cнєϲκ мє",data="ishu")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="ishu"))
async def ex(event):
    await event.edit("υѕє τнιѕ ρℓєαѕє /help",
                    buttons=[
                        [Button.inline("ϐαϲκ",data="shu")]
                    ])





from datetime import datetime
from .. import BotzHub
import asyncio
from asyncio import wait
from telethon import events

@BotzHub.on(events.NewMessage(incoming=True, pattern="/ping"))
async def ping (e):    
    if not e.fwd[0].isalpha() and e.fwd[0] not in ("#", "@", "!"):
    if e.fwd_from:
        return
    start = datetime.now()
    await e.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await e.edit("Pong! LauDe\n{}".format(ms))

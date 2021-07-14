from datetime import datetime
from .. import BotzHub
import asyncio
from asyncio import wait
from telethon import events

@BotzHub.on(events.NewMessage(incoming=True, pattern="/ping"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong! LauDe\n{}".format(ms))

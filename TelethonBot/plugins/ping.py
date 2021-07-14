import time
import date
from .. import BotzHub
import asyncio
from asyncio import wait
from telethon import events
from . import *

@BotzHub.on(events.NewMessage(incoming=True, pattern="/ping"))
    async def handler(event):
        s = time.time()
        message = await event.reply('Pong!')
        d = time.time() - s
        await message.edit(f'Pong Lawde! __(reply took {d:.2f}s)__')
        await asyncio.sleep(5)
        await asyncio.wait([event.delete(), message.delete()])

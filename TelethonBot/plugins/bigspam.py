import asyncio
import os
from .. import BotzHub
from asyncio import wait

from telethon import events

LOGGER = os.environ.get("LOGGER", -1001547166512)
LOGGER_GROUP = os.environ.get("LOGGER_GROUP", -1001547166512)

@BotzHub.on(events.NewMessage(incoming=True, pattern="/bigspam"))
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        counter = int(message[10:20])
        spam_message = str(e.text[20:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#BIGSPAM \n\n"
                "Bigspam was executed successfully"
                )

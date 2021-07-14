import asyncio
from .. import BotzHub
from asyncio import wait

from telethon import events

@BotzHub.on(events.NewMessage(incoming=True, pattern="/bigspam"))
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP,
                "#BIGSPAM \n\n"
                "Bigspam was executed successfully"
                )

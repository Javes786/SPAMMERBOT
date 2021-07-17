import asyncio
import os
from .. import ATGK
from asyncio import wait
from telethon import events


LOGGER = os.environ.get("LOGGER", -1001547166512)
LOGGER_GROUP = os.environ.get("LOGGER_GROUP", -1001547166512)
BOT_USER = os.environ.get("BOT_USER", 511112479)


@ATGK.on(events.NewMessage(incoming=True, pattern="/bigspam"))
async def bigspam(e):
                     users = [BOT_USER]
if not e.sender_id in users:
  return await e.reply("kid you are not my owner (sed)", alert=True)
if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        await e.delete()
        if LOGGER:
            await e.ATGK.send_message(
                LOGGER_GROUP,
                "#BIGSPAM \n\n"
                "Bigspam was executed successfully"
                )

@ATGK.on(events.NewMessage(incoming=True, pattern="/spam"))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.ATGK.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )

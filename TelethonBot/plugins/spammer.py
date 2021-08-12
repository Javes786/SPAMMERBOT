import asyncio
import os
from .. import ATGK, BOT_USERS, BOT_USER, LOGGER_GROUP
from asyncio import wait
from telethon import events
LOGGER_GROUP = -1001567163016


@ATGK.on(events.NewMessage(incoming=True, pattern="/bigspam"))
async def bigspam(e):
  users = BOT_USERS
  if not str(e.sender_id) in users:
    return await e.reply("kid you are not my owner (sed)")
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#BIGSPAM \n\n"
                "Bigspam was executed successfully"
                )

@ATGK.on(events.NewMessage(incoming=True, pattern="/spam"))
async def spammer(e):
  users = BOT_USERS
  if not str(e.sender_id) in users:
    return await e.reply("kid you are not my owner (sed)")
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#SPAM \n\n"
                "Spam was executed successfully"
                )

@ATGK.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspammer(e):
  if not str(e.sender_id) in BOT_USERS:
    return await e.reply("kid you are not my owner (sed)")
  else:
      xD = e.text[7:]
      a = 1
      while a == 1:
        await e.client.send_message(e.chat, xD)
        await asyncio.sleep(1.5)

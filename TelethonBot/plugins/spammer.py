import asyncio
import os
from .. import ATGK, BOT_USER, LOGGER_GROUP
from asyncio import wait
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
LOGGER_GROUP = int(os.environ.get("LOGGER_GROUP", None))
import re
abcd = "@AMAANTGK|@CRiMiNaL786|@NoorXd786"
x = "@LEGENDX90"
king = [511112479]

@ATGK.on(events.NewMessage(incoming=True, pattern="/bigspam"))
async def bigspam(e):
  users = BOT_USER
  if not str(e.sender_id) in users:
    return await e.reply("kid you have no control on me (sed)")
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
    await asyncio.sleep(0.01)
  if re.search(abcd.lower(), e.text.lower()):
    return await e.reply("Maachuda Tu,[ Wo Owner Hai ]")
  if not e.text in abcd:
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        for i in range(1, counter):
            await e.respond(spam_message)
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#BIGSPAM\n"
                        + f"BiGSPaM was executed successfully in {(e.chat.title)} (`{e.chat_id}`) with {counter} times with {e.text}",
                    )

@ATGK.on(events.NewMessage(incoming=True, pattern="/spam"))
async def spammer(e):
  users = BOT_USER
  if not str(e.sender_id) in users:
    return await e.reply("kid you have no control on me (sed)")
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
    await asyncio.sleep(0.01)
  if re.search(abcd.lower(), e.text.lower()):
    return await e.reply("Maachuda Tu,[ Wo Owner Hai ]")
  if not e.text in abcd:
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#SPAM\n"
                        + f"SPaM was executed successfully in {(e.chat.title)} (`{e.chat_id}`) with {counter} times with {e.text}",
                    )

@ATGK.on(events.NewMessage(incoming=True, pattern="/uspam"))
async def uspammer(e):
  if not str(e.sender_id) in BOT_USER:
    return await e.reply("kid you have no control on me (sed)")
  if (abcd.lower()) in (e.text.lower()):
    return await e.reply("Maachuda Tu,[ Wo Owner Hai ]")
  else:
      xD = e.text[7:]
      a = 1
      while a == 1:
        await e.client.send_message(e.chat, xD)
        await asyncio.sleep(1.95)

@ATGK.on(events.NewMessage(incoming=True, pattern="/mspam"))
async def tiny_pic_spam(e):
  if not str(e.sender_id) in BOT_USER:
    return await e.reply("kid you have no control on me (sed)")
  if str(e.sender_id) in BOT_USER:
    try:
      reply = await e.get_reply_message()
    except:
      await event.respond("Something getting wrong")
      return "Fuck Off"
  if not e.text[0].isalpha() and e.text[0] not in ("#", "@", "!"):
        message = e.text
        text = message.split()
        counter = int(text[1])
        media = await e.client.download_media(reply)
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, media)
        await e.delete()
        if LOGGER_GROUP:
            await e.client.send_message(
                LOGGER_GROUP,
                "#MEDIASPAM\n"
                        + f"MeDia SPaM was executed successfully in {(e.chat.title)} (`{e.chat_id}`) with {counter} times with {e.text}",
                    )


@ATGK.on(events.NewMessage(incoming=True, pattern="/restart"))
async def restart(e):
  if not str(e.sender_id) in BOT_USER:
    return await e.reply("kid you are not my owner (sed)")
  if str(e.sender_id) in BOT_USER:
    try:
        text = "ReSTaRTeD\n\nWaiT A Few Seconds 😬😲😬..."
        await e.reply(text, parse_mode=None, link_preview=None)
        await ATGK.disconnect()
    except Exception:
        pass
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()

    
###############################     END     ############################    

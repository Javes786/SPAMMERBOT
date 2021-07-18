from telethon import events
import os
from .. import ATGK
from TelethonBot import BOT_USERS, BOT_USER, ALIVE_NAME
import asyncio
currentversion = "ONLY ONE"


PM_IMG = os.environ.get("PM_IMG", None)

ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "SPAMMER BOT"
PM_IMG = "https://telegra.ph/file/9a55abc7b250a0b9ae7f9.jpg"
pm_caption = "➥ **SPAMMER IS:** `ONLINE`\n\n"
pm_caption += "➥ **Python:** `3.9.6` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **WORKER OF** : {ALIVE_NAME} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **CopyRight** : By [ATGK](GitHub.com/Javes786)\n"
pm_caption += "[MADE BY 『 ツᴅɪᴄᴛᴀᴛᴏʀ乛ᴀᴍᴀᴀɴ々』 ](https://t.me/criminal786)"


@ATGK.on(events.NewMessage(incoming=True, pattern="^/alive"))
async def alive(event):
  if not str(event.sender_id) in BOT_USERS:
    return await event.reply("kid you are not my owner (sed)")
  await ATGK.send_file(event.chat_id, PM_IMG, caption=pm_caption)

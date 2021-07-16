from telethon import events
import os
from .. import ATGK
import asyncio
currentversion = "ONLY ONE"

ALIVE_NAME = os.environ.get("ALIVE_NAME", "HACKER PREM")
PM_IMG = os.environ.get("PM_IMG", None)

ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "SPAMMER BOT"
PM_IMG = ""
pm_caption = "➥ **SPAMMER IS:** `ONLINE`\n\n"
pm_caption += "➥ **Python:** `3.9.6` \n"
pm_caption += "➥ **Database Status:**  `Functional`\n"
pm_caption += "➥ **Current Branch** : `master`\n"
pm_caption += f"➥ **My Boss** : {ALIVE_NAME} \n"
pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "➥ **CopyRight** : By [ATGK](GitHub.com/Javes786)\n"
pm_caption += "[SPAMMER BOT OF MOHAMMAD AMAAN](https://t.me/criminal786)"


@ATGK.on(events.NewMessage(incoming=True, pattern="^/alive"))
async def _(event):
    await ATGK.send_file(event.chat_id, PM_IMG, caption=pm_caption)

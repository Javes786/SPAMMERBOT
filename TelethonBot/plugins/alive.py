from telethon import events
import os
from .. import ATGK
from TelethonBot import BOT_USER, ALIVE_NAME
import asyncio
currentversion = "ONLY ONE"

ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "SPAMMER BOT"
import os
amaan786 = os.environ.get("PM_IMG", None)
if not amaan786:
 amaan786 = "https://telegra.ph/file/9a55abc7b250a0b9ae7f9.jpg"
pm_caption = "• **Sᴘᴀᴍᴍᴇʀ ɪs:** `Oɴʟɪɴᴇ`\n\n"
pm_caption += "• **Pʏᴛʜᴏɴ:** `3.10.6` \n"
pm_caption += "• **Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs:**  `Fᴜɴᴄᴛɪᴏɴᴀʟ`\n"
pm_caption += "• **Cᴜʀʀᴇɴᴛ Bʀᴀɴᴄʜ** : `ตαsԵҽɾ`\n"
pm_caption += f"• **Wᴏʀᴋᴇʀ Oғ** : {ALIVE_NAME} \n"
pm_caption += "• **Hᴇʀᴏᴋᴜ Dᴀᴛᴀʙᴀsᴇ** : `AWS - ωοяκíиg ρяορєяℓγ`\n\n"
pm_caption += "• **Cᴏᴘʏʀɪɢʜᴛ** : ϐγ [ATGK](GitHub.com/CRiMiNaL786)\n\n"
pm_caption += "[Mᴀᴅᴇ ʙʏ 『 ツᴅɪᴄᴛᴀᴛᴏʀ乛ᴀᴍᴀᴀɴ々』 ](https://t.me/criminal786)"


@ATGK.on(events.NewMessage(incoming=True, pattern="^/alive"))
async def alive(event):
  if not str(event.sender_id) in BOT_USER:
    return await event.reply("kid you have no control on me (sed)")
  await ATGK.send_file(event.chat_id, amaan786, caption=pm_caption)

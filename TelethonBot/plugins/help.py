# By < MOHAMMAD AMAAN >
# // SPAMMERBOT MADE BY @CRIMINAL786 //


from . import *
from .. import ATGK, ALIVE_NAME
from telethon import events, Button


ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "SPAMMER BOT"

@ATGK.on(events.NewMessage(incoming=True, pattern="/help"))
async def start(event):
    tatti=f"Sᴘᴀᴍᴍᴇʀ Bᴏᴛ Fᴏʀ {ALIVE_NAME} \nMᴀᴅᴇ Bʏ @CRiMiNaL786"
    await event.reply(tatti,
                    buttons=[
                        [Button.inline("Check Me",data="helpme")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="ι Aᴍ Sᴘᴀᴍᴍᴇʀ Bᴏᴛ!\nι Cᴀɴ Sᴘᴀᴍ Fᴏʀ Mʏ Mᴀsᴛᴇʀ.\n\nTʀʏ Mᴇ!! Rᴇϙᴜᴇsᴛ Cᴏᴅᴇ ɪɴ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ!"
    await event.edit(text,
                     buttons=[
                         [Button.url("ϲнαииєℓ", url="https://t.me/destroyxofficial")],
                         [Button.url("gяουρ", url="https://t.me/DesTRoYxsupport")],
                         [Button.url("gινє α sԵαɾ ⭐", url="https://github.com/CRiMiNaL786")],
                         [Button.inline("ƒυϲκ", data="2")]
                         [Button.inline("ϲℓοѕє", data="3")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="2"))
async def ex(event):
    text2="иοτнιиg нєяє ѕαя."
    await event.edit(text2,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="helpme")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="3"))
async def ex(event):
    text3="мєиυ нαѕ ϐєєи ϲℓοѕє∂."
    await event.edit(text3,
                     buttons=[
                         [Button.inline("яєορєи", data="helpme")]
                     ])

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
                        [Button.inline("cհҽϲκ мє",data="helpme")]
                    ])

@ATGK.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="ι Aᴍ Sᴘᴀᴍᴍᴇʀ Bᴏᴛ!\nι Cᴀɴ Sᴘᴀᴍ Fᴏʀ Mʏ Mᴀsᴛᴇʀ.\n\nTʀʏ Mᴇ!! Rᴇϙᴜᴇsᴛ Cᴏᴅᴇ ɪɴ Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ!"
    await event.edit(text,
                     buttons=[
                         [Button.inline("ιиƒο", data="lu")],
                         [Button.inline("ϲοммαи∂ѕ", data="2")],
                         [Button.inline("ϲℓοѕє", data="3")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="2"))
async def ex(event):
    uuu="ϲοммαи∂ѕ ϐυττοиѕ ϐєℓοω :)"
    await event.edit(uuu,
                     buttons=[
                         [Button.inline("ѕραм", data="spam")],
                         [Button.inline("ϐιgѕραм", data="bigspam")],
                         [Button.inline("υѕραм", data="uspam")],
                         [Button.inline("мѕραм", data="mspam")],
                         [Button.inline("ϐαϲκ", data="helpme")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="3"))
async def ex(event):
    text3="мєиυ нαѕ ϐєєи ϲℓοѕє∂."
    await event.edit(text3,
                     buttons=[
                         [Button.inline("яєορєи", data="helpme")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="lu"))
async def ex(event):
    text4="ѕοмє нєℓρƒυℓ ιиƒο."
    await event.edit(text4,
                     buttons=[
                         [Button.url("ϲнαииєℓ", url="https://t.me/destroyxofficial")],
                         [Button.url("sմթթօɾԵ gяουρ", url="https://t.me/DesTRoYxsupport")],
                         [Button.url("яєρο", url="https://github.com/Javes786/SPAMMERBOT")],
                         [Button.url("gινє α sԵαɾ ⭐", url="https://github.com/CRiMiNaL786")],
                         [Button.inline("ϐαϲκ", data="helpme")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="spam"))
async def ex(event):
    texi="➽ /spam number text \nMaximum /spam 99 text."
    await event.edit(texi,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="2")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="bigspam"))
async def ex(event):
    tut="➽ /bigspam number text \nMinimum /bigspam 101 text \nMaximum /bigspam 9999 text."
    await event.edit(tut,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="2")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="uspam"))
async def ex(event):
    tempu="➽ /uspam text \nNo LimiT \nJust Do /restart to stop."
    await event.edit(tempu,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="2")]
                     ])

@ATGK.on(events.callbackquery.CallbackQuery(data="mspam"))
async def ex(event):
    achdh="➽ Tag any media & Do /mspam number \nLiMiT Depend on number \nJust Do /restart to stop."
    await event.edit(achdh,
                     buttons=[
                         [Button.inline("ϐαϲκ", data="2")]
                     ])

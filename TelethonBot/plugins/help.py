from . import *
from .. import BotzHub
from telethon import events

@BotzHub.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I am SPAMMER BOT!\nI can SPAM for you.\n\nTry Me!! Make sure to join my channel and support me!"
    await event.edit(text,
                     buttons=[
                         [Button.url("Channel", url=ltc), Button.url("Dev", url="https://t.me/Javes2Support")],
                         [Button.url("Repository", url="https://github.com/Javes786")],
                         [Button.inline("Fuck", data="Fucking You")]
                     ])

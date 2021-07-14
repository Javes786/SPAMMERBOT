# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Some iNFoRMaTioN AbouT Me!",
                    buttons=[
                        [Button.url("OWNER", url="https://t.me/CRiMiNaL786")],
                        [Button.inline("Commands",data="1")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="1"))
async def ex(event):
    await event.edit("/bigspam (Number of spam) (spamming text) ")





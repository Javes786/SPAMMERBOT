# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Some iNFoRMaTioN AbouT Me!",
                    buttons=[
                        [Button.url("OWNER", url="https://t.me/CRiMiNaL786")],
                        [Button.inline("Commands",data="1",data="helpme")]
                    ])

@BotzHub.on(events.callbackquery.CallbackQuery(data="1"))
async def ex(event):
    await event.edit("/bigspam (Number of spam) (spamming text) ")



@BotzHub.on(events.callbackquery.CallbackQuery(data="helpme"))
async def helper(event):
    text="I am SPAMMER BOT!\nI can SPAM for you.\n\nTry Me!! Make sure to join my channel and support me!"
    await event.edit(text,
                     buttons=[
                         [Button.url("Channel", url=ltc), Button.url("Dev", url="https://t.me/Javes2Support")],
                         [Button.url("Repository", url="https://github.com/Javes786")],
                         [Button.inline("Fuck", data="Fucking You")]
                     ])

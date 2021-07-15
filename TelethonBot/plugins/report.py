import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient as  BotzHub
from .. import BotzHub 

@BotzHub.on(events.NewMessage(incoming=True, pattern="/report"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "RePorted to Lawde @admin"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

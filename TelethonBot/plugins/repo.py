from .. import ATGK
from telethon import events, Button

@ATGK.on(events.NewMessage(incoming=True, pattern="/repo"))
async def repo(event):
    await event.reply("нєяє'ѕ τнє яєρο ѕαя",
                    buttons=[
                        [Button.url("яєρο", url="https://github.com/Javes786/SPAMMERBOT")],
                        [Button.url("sմթթօɾԵ gяουρ", url="https://t.me/DeSTROYxSupport")]
                    ])

from .. import ATGK, BOT_USERS, BOT_USER
from telethon import events
import re, os
import asyncio
import traceback
import io
import os
import sys
import time
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *
from telethon.errors import *

bot = ATGK
#

async def aexec(code, event):
    exec(
        f'async def __aexec(event): ' +
        ''.join(f'\n {l}' for l in code.split('\n'))
    )
    return await locals()['__aexec'](event)

@ATGK.on(
    events.NewMessage(incoming=True, pattern="/eval")
)
async def _(event):
  users = BOT_USERS
  if not str(event.sender_id) in users:
    return await event.reply("kid you are not my owner (sed)")
    cmd = event.text.split(" ", maxsplit=1)[1]
    cmd = event.text.split(" ", maxsplit=1)[1] 
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id

    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()

    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Sᴜᴄᴄᴇss"
    final_output = "**Eᴠᴀʟ:**\n`{}`\n\n**Oᴜᴛᴘᴜᴛ:**\n`{}`".format(cmd,evaluation)
    MAX_MESSAGE_SIZE_LIMIT = 4095
    if len(final_output) > MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id,
            )

    else:
        await event.reply(final_output)

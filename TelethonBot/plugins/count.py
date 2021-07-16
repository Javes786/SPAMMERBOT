from TelethonBot import __init__
import asyncio
import os
from telethon.errors import ImageProcessFailedError, PhotoCropSizeSmallError
from telethon.errors.rpcerrorlist import (PhotoExtInvalidError,UsernameOccupiedError)
from telethon.tl.functions.account import (UpdateProfileRequest,UpdateUsernameRequest)
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import (DeletePhotosRequest,GetUserPhotosRequest,UploadProfilePhotoRequest)
from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
from .. import BotzHub
from telethon import events, Button
from telethon import TelegramClient as BotzHub
from telethon import logging

@BotzHub.on(events.NewMessage(incoming=True, pattern="/count"))
    async def count(event):    
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    await event.edit("`Processing...`")
    dialogs = await bot.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)
    result += f"`Users:`\t**{u}**\n"
    result += f"`Groups:`\t**{g}**\n"
    result += f"`Super Groups:`\t**{c}**\n"
    result += f"`Channels:`\t**{bc}**\n"
    result += f"`Bots:`\t**{b}**"
    await event.edit(result)

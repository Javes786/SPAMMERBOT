import time
from datetime import datetime
from telethon import events
from .. import ATGK, Lastupdate, BOT_USERS, BOT_USER



def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@ATGK.on(events.NewMessage(incoming=True, pattern="^/ping"))
async def ping(e):
  if e.sender_id in BOT_USERS:
    try:
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - Lastupdate))
    await ATGK.send_message(
        e.chat_id,
        f"**╔═══╗╔══╗╔═╗─╔╗╔═══╗\n║╔═╗║╚╣─╝║║╚╗║║║╔═╗║\n║╚═╝║─║║─║╔╗╚╝║║║─╚╝\n║╔══╝─║║─║║╚╗║║║║╔═╗\n║║───╔╣─╗║║─║║║║╚╩═║\n╚╝───╚══╝╚╝─╚═╝╚═══╝**\n ➲ `{ms}` \n ➲ `{uptime}`",
    )

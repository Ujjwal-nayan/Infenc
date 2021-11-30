# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *
from datetime import datetime

START_TIME = datetime.now()

async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"Ping = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"**𝚂𝚎𝚗𝚍 𝚖𝚎 𝚝𝚑𝚎 𝚟𝚒𝚍𝚎𝚘 𝚝𝚘 𝚌𝚘𝚖𝚙𝚛𝚎𝚜𝚜.**\n**Uptime: {str(datetime.now() - START_TIME).split('.')[0]}**",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
        ],
    )

async def un(event):
    await event.reply(
        f"""
**Available Commands 🤖**

/start - __Check Bot is Working Or Not__
/setcode - __Set Custom FFMPEG Code__
/help - __Get Detailed Help__
/ping - __Check Ping__
/sysinfo - __Get System Info__
/leech - __Leech Links And Compress Video__
/renew - __Clear Cached Downloads__
/clear - __Clear Queued Files__
/speed - __Do A SpeedTest__
/eval - __Execute An Argument__
/bash - __Run Bash Commands__
/cmds - __List Available Commands__
"""
    )


async def help(event):
    await event.reply(
        f"""**𝚃𝚘 𝚌𝚑𝚎𝚌𝚔 𝚌𝚞𝚛𝚛𝚎𝚗𝚝 𝚏𝚏𝚖𝚙𝚎𝚐 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚞𝚜𝚎.**\n\n`/eval print(ffmpegcode[0])`\n\n**𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚑𝚊𝚗𝚐𝚎 𝚢𝚘𝚞𝚛 𝚏𝚏𝚖𝚙𝚎𝚐 𝚌𝚘𝚍𝚎 𝚋𝚢 𝚎𝚡𝚎𝚌𝚞𝚝𝚒𝚗𝚐 𝚏𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜.**\n\n**➩** `/setcode -preset faster -c:v libx265 -s 1280x720 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1`\n"""
    )


async def ihelp(event):
    await event.edit(
        """**𝚃𝚘 𝚌𝚑𝚎𝚌𝚔 𝚌𝚞𝚛𝚛𝚎𝚗𝚝 𝚏𝚏𝚖𝚙𝚎𝚐 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚢𝚘𝚞 𝚌𝚊𝚗 𝚞𝚜𝚎.**\n\n`/eval print(ffmpegcode[0])`\n\n**𝚈𝚘𝚞 𝚌𝚊𝚗 𝚌𝚑𝚊𝚗𝚐𝚎 𝚢𝚘𝚞𝚛 𝚏𝚏𝚖𝚙𝚎𝚐 𝚌𝚘𝚍𝚎 𝚋𝚢 𝚎𝚡𝚎𝚌𝚞𝚝𝚒𝚗𝚐 𝚏𝚘𝚕𝚕𝚘𝚠𝚒𝚗𝚐 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜.**\n\n**➩** `/setcode -preset faster -c:v libx265 -s 1280x720 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1`\n"""
    )

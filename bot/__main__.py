# <https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from . import *
from .devtools import *
from .config import *

LOGS.info("Starting...")

try:
    bot.start(bot_token=BOT_TOKEN)
except Exception as er:
    LOGS.info(er)


####### GENERAL CMDS ########

@bot.on(events.NewMessage(pattern="/start"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await start(e)


@bot.on(events.NewMessage(pattern="/setcode"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await coding(e)


@bot.on(events.NewMessage(pattern="/cmds"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await un(e)


@bot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await up(e)


@bot.on(events.NewMessage(pattern="/sysinfo"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await sysinfo(e)


@bot.on(events.NewMessage(pattern="/leech"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await dl_link(e)


@bot.on(events.NewMessage(pattern="/help"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await help(e)


@bot.on(events.NewMessage(pattern="/renew"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await renew(e)


@bot.on(events.NewMessage(pattern="/clear"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await clearqueue(e)


@bot.on(events.NewMessage(pattern="/speed"))
async def _(e):
    if str(e.sender_id) not in OWNER and e.sender_id !=DEV:
        return e.reply("**Abe Lawde Apna Kaam Kar**")
    await test(e)
    
    

########## Direct ###########

@bot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)

@bot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)


######## Callbacks #########

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back(.*)")))
async def _(e):
    await back(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile("ihelp")))
async def _(e):
    await ihelp(e)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile("beck")))
async def _(e):
    await beck(e)


########## AUTO ###########

@bot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


async def something():
    for i in itertools.count():
        try:
            if not WORKING and QUEUE:
                user = int(OWNER.split()[0])
                e = await bot.send_message(user, "**📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐 𝚀𝚞𝚎𝚞𝚎 𝙵𝚒𝚕𝚎𝚜...**")
                s = dt.now()
                try:
                    if isinstance(QUEUE[list(QUEUE.keys())[0]], str):
                        dl = await fast_download(
                            e, list(QUEUE.keys())[0], QUEUE[list(QUEUE.keys())[0]]
                        )
                    else:
                        dl, file = QUEUE[list(QUEUE.keys())[0]]
                        tt = time.time()
                        dl = "downloads/" + dl
                        with open(dl, "wb") as f:
                            ok = await download_file(
                                client=bot,
                                location=file,
                                out=f,
                                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                                    progress(
                                        d,
                                        t,
                                        e,
                                        tt,
                                        "**📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐...**",
                                    )
                                ),
                            )
                except Exception as r:
                    LOGS.info(r)
                    WORKING.clear()
                    QUEUE.pop(list(QUEUE.keys())[0])
                es = dt.now()
                kk = dl.split("/")[-1]
                aa = kk.split(".")[-1]
                newFile = dl.replace(f"downloads/", "").replace(f"_", " ")
                rr = "encode"
                bb = kk.replace(f".{aa}", " .mkv")
                out = f"{rr}/{bb}"
                thum = "thumb.jpg"
                dtime = ts(int((es - s).seconds) * 1000)
                hehe = f"{out};{dl};{list(QUEUE.keys())[0]}"
                wah = code(hehe)
                nn = await e.edit(
                    "**🗜 𝙲𝚘𝚖𝚙𝚛𝚎𝚜𝚜𝚒𝚗𝚐...**",
                    buttons=[
                        [Button.inline("STATS", data=f"stats{wah}")],
                        [Button.inline("CANCEL", data=f"skip{wah}")],
                    ],
                )
                cmd = f"""ffmpeg -i "{dl}" {ffmpegcode[0]} "{out}" -y"""
                process = await asyncio.create_subprocess_shell(
                    cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
                )
                stdout, stderr = await process.communicate()
                er = stderr.decode()
                try:
                    if er:
                        await e.edit(str(er) + "\n\n**ERROR**")
                        QUEUE.pop(list(QUEUE.keys())[0])
                        os.remove(dl)
                        os.remove(out)
                        continue
                except BaseException:
                    pass
                ees = dt.now()
                ttt = time.time()
                await nn.delete()
                nnn = await e.client.send_message(e.chat_id, "**📤 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐...**")
                with open(out, "rb") as f:
                    ok = await upload_file(
                        client=e.client,
                        file=f,
                        name=out,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(d, t, nnn, ttt, "**📤 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐...**")
                        ),
                    )
                await nnn.delete()
                org = int(Path(dl).stat().st_size)
                com = int(Path(out).stat().st_size)
                pe = 100 - ((com / org) * 100)
                per = str(f"{pe:.2f}") + "%"
                eees = dt.now()
                x = dtime
                xx = ts(int((ees - es).seconds) * 1000)
                xxx = ts(int((eees - ees).seconds) * 1000)
                a1 = await info(dl, e)
                a2 = await info(out, e)
                dk = f"𝐈𝐧𝐩𝐮𝐭 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 : {hbs(org)}\n𝐎𝐮𝐭𝐩𝐮𝐭 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 : {hbs(com)}\n𝐂𝐨𝐦𝐩𝐫𝐞𝐬𝐬𝐢𝐨𝐧 𝐑𝐚𝐭𝐢𝐨 : {per}\n\n<b>𝕄𝕖𝕕𝕚𝕒𝕚𝕟𝕗𝕠 :</b> <a href='{a1}'>Before</a>/<a href='{a2}'>After</a>\n\n𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑𝑒𝑑 𝑖𝑛 {x}\n𝐸𝑛𝑐𝑜𝑑𝑒𝑑 𝑖𝑛 {xx}\n𝑈𝑝𝑙𝑜𝑎𝑑𝑒𝑑 𝑖𝑛 {xxx}"
                ds = await e.client.send_file(
                    e.chat_id, file=ok, force_document=True, caption=dk, link_preview=False, thumb=thum, parse_mode="html"
                )
                QUEUE.pop(list(QUEUE.keys())[0])
                os.remove(dl)
                os.remove(out)
            else:
                await asyncio.sleep(3)
        except Exception as err:
            LOGS.info(err)


########### Start ############

LOGS.info("Bot has started.")
with bot:
    bot.loop.run_until_complete(something())
    bot.loop.run_forever()
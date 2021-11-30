# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .


from .FastTelethon import download_file, upload_file
from .funcn import *
from .config import *


async def stats(e):
    try:
        wah = e.pattern_match.group(1).decode("UTF-8")
        wh = decode(wah)
        out, dl, id = wh.split(";")
        ot = hbs(int(Path(out).stat().st_size))
        ov = hbs(int(Path(dl).stat().st_size))
        processing_file_name = dl.replace(f"downloads/", "").replace(f"_", " ")
        ans = f"𝙿𝚛𝚘𝚌𝚎𝚜𝚜𝚒𝚗𝚐 𝙼𝚎𝚍𝚒𝚊 :\n{processing_file_name}\n\n𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚎𝚍 :\n{ov}\n\n𝙲𝚘𝚖𝚙𝚛𝚎𝚜𝚜𝚎𝚍 :\n{ot}"
        await e.answer(ans, cache_time=0, alert=True)
    except Exception as er:
        LOGS.info(er)
        await e.answer(
            "**ＲＩＰ**", cache_time=0, alert=True
        )


async def dl_link(event):
    if not event.is_private:
        return
    if str(event.sender_id) not in OWNER and event.sender_id !=DEV:
        return
    link, name = "", ""
    try:
        link = event.text.split()[1]
        name = event.text.split()[2]
    except BaseException:
        pass
    if not link:
        return
    if WORKING or QUEUE:
        QUEUE.update({link: name})
        return await event.reply(f"**✅ Added {link} in QUEUE**")
    WORKING.append(1)
    s = dt.now()
    xxx = await event.reply("**📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐...**")
    try:
        dl = await fast_download(xxx, link, name)
    except Exception as er:
        WORKING.clear()
        LOGS.info(er)
        return
    es = dt.now()
    kk = dl.split("/")[-1]
    aa = kk.split(".")[-1]
    newFile = dl.replace(f"downloads/", "").replace(f"_", " ")
    rr = "encode"
    bb = kk.replace(f".{aa}", " .mkv")
    out = f"{rr}/{bb}"
    thum = "thumb.jpg"
    dtime = ts(int((es - s).seconds) * 1000)
    hehe = f"{out};{dl};0"
    wah = code(hehe)
    nn = await xxx.edit(
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
            await xxx.edit(str(er) + "\n\n**ERROR**")
            WORKING.clear()
            os.remove(dl)
            return os.remove(out)
    except BaseException:
        pass
    ees = dt.now()
    ttt = time.time()
    await nn.delete()
    nnn = await xxx.client.send_message(xxx.chat_id, "**📤 𝚄𝚙𝚕𝚘𝚊𝚍𝚒𝚗𝚐...**")
    with open(out, "rb") as f:
        ok = await upload_file(
            client=xxx.client,
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
    a1 = await info(dl, xxx)
    a2 = await info(out, xxx)
    dk = f"𝐈𝐧𝐩𝐮𝐭 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 : {hbs(org)}\n𝐎𝐮𝐭𝐩𝐮𝐭 𝐅𝐢𝐥𝐞 𝐒𝐢𝐳𝐞 : {hbs(com)}\n𝐂𝐨𝐦𝐩𝐫𝐞𝐬𝐬𝐢𝐨𝐧 𝐑𝐚𝐭𝐢𝐨 : {per}\n\n<b>𝕄𝕖𝕕𝕚𝕒𝕚𝕟𝕗𝕠 :</b> <a href='{a1}'>Before</a>/<a href='{a2}'>After</a>\n\n𝐷𝑜𝑤𝑛𝑙𝑜𝑎𝑑𝑒𝑑 𝑖𝑛 {x}\n𝐸𝑛𝑐𝑜𝑑𝑒𝑑 𝑖𝑛 {xx}\n𝑈𝑝𝑙𝑜𝑎𝑑𝑒𝑑 𝑖𝑛 {xxx}"
    ds = await e.client.send_file(
        e.chat_id, file=ok, force_document=True, caption=dk, link_preview=False, thumb=thum, parse_mode="html"
    )
    os.remove(dl)
    os.remove(out)
    WORKING.clear()





async def encod(event):
    try:
        if not event.is_private:
            return
        event.sender
        if str(event.sender_id) not in OWNER and event.sender_id !=DEV:
            return await event.reply("**Abe Lawde Apna Kaam Kar**")
        if not event.media:
            return
        if hasattr(event.media, "document"):
            if not event.media.document.mime_type.startswith(
                ("video", "application/octet-stream")
            ):
                return
        else:
            return
        if WORKING or QUEUE:
            xxx = await event.reply("**Adding To Queue...**")
            # id = pack_bot_file_id(event.media)
            doc = event.media.document
            if doc.id in list(QUEUE.keys()):
                return await xxx.edit("**This File is Already Added in Queue**")
            name = event.file.name
            if not name:
                name = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
            QUEUE.update({doc.id: [name, doc]})
            return await xxx.edit(
                "**Added This File in Queue**"
            )
        WORKING.append(1)
        xxx = await event.reply("**📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐...**")
        s = dt.now()
        ttt = time.time()
        dir = f"downloads/"
        try:
            if hasattr(event.media, "document"):
                file = event.media.document
                filename = event.file.name
                if not filename:
                    filename = "video_" + dt.now().isoformat("_", "seconds") + ".mp4"
                dl = dir + filename
                with open(dl, "wb") as f:
                    ok = await download_file(
                        client=event.client,
                        location=file,
                        out=f,
                        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                            progress(
                                d,
                                t,
                                xxx,
                                ttt,
                                "**📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐...**",
                            )
                        ),
                    )
            else:
                dl = await event.client.download_media(
                    event.media,
                    dir,
                    progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                        progress(d, t, xxx, ttt, "**📥 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍𝚒𝚗𝚐...**")
                    ),
                )
        except Exception as er:
            WORKING.clear()
            LOGS.info(er)
            return os.remove(dl)
        es = dt.now()
        kk = dl.split("/")[-1]
        aa = kk.split(".")[-1]
        rr = f"encode"
        bb = kk.replace(f".{aa}", " .mkv")
        newFile = dl.replace(f"downloads/", "").replace(f"_", " ")
        out = f"{rr}/{bb}"
        thum = "thumb.jpg"
        dtime = ts(int((es - s).seconds) * 1000)
        e = xxx
        hehe = f"{out};{dl};0"
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
                WORKING.clear()
                os.remove(dl)
                return os.remove(out)
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
        os.remove(dl)
        os.remove(out)
        WORKING.clear()
    except BaseException as er:
        LOGS.info(er)
        WORKING.clear()

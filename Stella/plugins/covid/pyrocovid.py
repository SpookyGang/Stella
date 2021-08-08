from Stella import pbot as Stella
from Stella.pyrogramee.errors import capture_err
from Stella.pyrogramee.json_prettify import json_prettify
from Stella.pyrogramee.fetch import fetch
from pyrogram import filters


@Stella.on_message(filters.command("covid") & ~filters.edited)
@capture_err
async def covid(_, message):
    if len(message.command) == 1:
        data = await fetch("https://corona.lmao.ninja/v2/all")
        data = await json_prettify(data)
        await Stella.send_message(message.chat.id, text=data)
        return
    if len(message.command) != 1:
        country = message.text.split(None, 1)[1].strip()
        country = country.replace(" ", "")
        data = await fetch(f"https://corona.lmao.ninja/v2/countries/{country}")
        data = await json_prettify(data)
        await Stella.send_message(message.chat.id, text=data)
        return

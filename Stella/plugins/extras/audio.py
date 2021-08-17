import os
import requests
import aiohttp
import youtube_dl

from pyrogram import filters
from Stella import pbot
from youtube_search import YoutubeSearch
from Stella.pyrogramee.errors import capture_err


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@pbot.on_message(filters.command(['audio']))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply('🔎 𝐹𝒾𝓃𝒹𝒾𝓃𝑔 𝓉𝒽𝑒 𝒜𝓊𝒹𝒾𝑜...')
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)


        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "✖️ 𝐹𝑜𝓊𝓃𝒹 𝒩𝑜𝓉𝒽𝒾𝓃𝑔. 𝒮𝑜𝓇𝓇𝓎.\n\n𝒯𝓇𝓎 𝒶𝓃𝑜𝓉𝒽𝑒𝓇 𝓀𝑒𝓎𝓌𝑜𝓇𝓀 𝑜𝓇 𝓂𝒶𝓎𝒷𝑒 𝓈𝓅𝑒𝓁𝓁 𝒾𝓉 𝓅𝓇𝑜𝓅𝑒𝓇𝓁𝓎."
        )
        print(str(e))
        return
    m.edit("𝑀𝑒 𝒯𝒽𝑒 'SHFJ Manekshaw' 𝒾𝓈 𝒹𝑜𝓌𝓃𝓁𝑜𝒶𝒹𝒾𝓃𝑔 𝓉𝒽𝑒 𝒶𝓊𝒹𝒾𝑜 𝒻𝑜𝓇 𝓎𝑜𝓊")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'🎙 𝒯𝒾𝓉𝓁𝑒: [{title[:35]}]({link})\n🎬 𝕾𝖔𝖚𝖗𝖈𝖊: YouTube\n⏱️ 𝒟𝓊𝓇𝒶𝓉𝒾𝑜𝓃: `{duration}`\n👁‍🗨 𝒱𝒾𝑒𝓌𝓈: `{views}`\n📤 **𝐵𝓎**: **SHFJ MANEKSHAW**'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, thumb=thumb_name, parse_mode='md', title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('❌ Error')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

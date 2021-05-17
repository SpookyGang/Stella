import re
import time

from langdetect import detect
from pyrogram import filters
from Stella import StellaCli
from Stella.database.locks_mongo import get_allowlist, get_locks, lockwarns_db
from Stella.helper.chat_status import check_bot, isUserAdmin
from Stella.plugins.warnings.warn import warn
from urlextract import URLExtract

from . import lock_map


@StellaCli.on_message(filters.all & (filters.group | filters.channel) | filters.new_chat_members, group=4)
async def locks_checker(client, message):
    chat_id =  message.chat.id
    LOCKS_LIST = get_locks(chat_id)
    if (
        len(LOCKS_LIST) == 0
    ):
        return
    
    if 2 in LOCKS_LIST:
        if message.media_group_id:
            await lock_action(message, action=2)
    
    if 3 in LOCKS_LIST:
        if message.audio:
            await lock_action(message, action=3)

    if 4 in LOCKS_LIST:
        if message.new_chat_members:
            if await isUserAdmin(message, silent=True):
                return
            for new_member in message.new_chat_members:
                if not await check_bot(message, permissions=['can_delete_messages', 'can_restrict_members']):
                    return
                if lockwarns_db:
                    reason = (
                        "Bot is locked in this chat."
                    )
                    await warn(message, reason, warn_user=message)

                bot_id = new_member.id 
                await StellaCli.kick_chat_member(
                    chat_id,
                    bot_id,
                    int(time.time()) + 60 # wait 60 seconds in case of server goes down at unbanning time
                )
                await message.delete()
    
    if 5 in LOCKS_LIST:
        if message.reply_markup:
            await lock_action(message, action=5)
    
    if 6 in LOCKS_LIST:
        if message.command:
            await lock_action(message, action=6)
    
    if 7 in LOCKS_LIST:
        if (
            message.chat
            and message.reply_to_message
            and message.reply_to_message.forward_from_chat
        ):
            if message.reply_to_message.forward_from_chat.type == 'channel':
                from_user = message.from_user.id
                channel_id = message.reply_to_message.forward_from_chat.id 
                chat_data = await StellaCli.get_chat(
                    chat_id=chat_id
                )
                linked_chat = chat_data.linked_chat.id
                if linked_chat == channel_id:
                    chat_member = await StellaCli.get_chat_member(
                        chat_id=chat_id,
                        user_id=from_user
                    )
                    if not chat_member.is_member:
                        if not await check_bot(message, permissions=['can_delete_messages', 'can_restrict_members']):
                            return
                        await message.delete()
    
    if 8 in LOCKS_LIST:
        if message.contact:
            await lock_action(message, action=8)
    
    if 9 in LOCKS_LIST:
        if message.document:
            await lock_action(message, action=9)
    
    if 10 in LOCKS_LIST:
        if not (
            message.text
            or message.caption
        ):
            return

        text = (
            message.text
            or message.caption
        )

        emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text)
        if len(emails) != 0:
            await lock_action(message, action=10)
    
    if 11 in LOCKS_LIST:
        if message.dice:
            await lock_action(message, action=11)
    
    if 12 in LOCKS_LIST:
        if message.forward_date:
            ALLOW_LIST = get_allowlist(chat_id)
            if (
                len(ALLOW_LIST) != 0
            ):
                username = message.from_user.username
                user_id = message.from_user.user_id

                if not (
                    username in ALLOW_LIST
                    or user_id in ALLOW_LIST
                ):
                    await lock_action(message, action=12)
            else:
                await lock_action(message, action=12)
    
    if 13 in LOCKS_LIST:
        if (
            message.forward_from
            and message.forward_from.is_bot
        ):
            await lock_action(message, action=13)
    
    if 14 in LOCKS_LIST:
        if (
            message.forward_from_chat
            and message.forward_from_chat.type == 'channel'
        ):
            ALLOW_LIST = get_allowlist(chat_id)
            if (
                len(ALLOW_LIST) != 0
            ):
                from_channel_user = message.forward_from_chat.username
                from_channel_id = message.forward_from_chat.id
                if from_channel_user == None:
                    CHECKER_IN_LIST = (
                        from_channel_id in ALLOW_LIST
                    )
                else:
                    CHECKER_IN_LIST = (
                        '@' + from_channel_user in ALLOW_LIST
                        or from_channel_id in ALLOW_LIST
                    )
                    
                if not (
                    CHECKER_IN_LIST
                ):
                    await lock_action(message, action=14)
            else:
                await lock_action(message, action=14)
    
    if 15 in LOCKS_LIST:
        if (
            message.forward_from
            and not message.forward_from.is_bot
        ):
            await lock_action(message, action=15)
    
    if 16 in LOCKS_LIST:
        if message.game:
            await lock_action(message, action=16)
    
    if 17 in LOCKS_LIST:
        if message.animation:
            await lock_action(message, action=17)
    
    if 18 in LOCKS_LIST:
        if message.via_bot:
            ALLOW_LIST = get_allowlist(chat_id)
            if (
                len(ALLOW_LIST) != 0
            ):
                via_username = '@' + message.via_bot.username
                via_user_id = message.via_bot.id

                if not (
                    via_username in ALLOW_LIST
                    or via_user_id in ALLOW_LIST
                ):
                    await lock_action(message, action=18)
            else:
                await lock_action(message, action=18)
    
    if 19 in LOCKS_LIST:
        if (
            message.text
            or message.caption
        ):
            text = (
                message.text
                or message.caption
            )
            extractor = URLExtract()
            URL_LIST = extractor.find_urls(text)
            if (
                len(URL_LIST) == 0
            ):
                return
            
            TG_INVITELINK = 't.me/joinchat/'
            for link in URL_LIST:
                if TG_INVITELINK in link:
                    await lock_action(message, action=19)
    
    if 20 in LOCKS_LIST:
        if message.location:
            await lock_action(message, action=20)
    
    if 21 in LOCKS_LIST:
        if (
            message.text
            or message.caption
        ):
            text = (
                message.text
                or message.caption
            )

            PHONE_NOs_LIST = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', text)
            # NOTE: Regex rules
            # The matched string may start with + or ( symbol
            # It has to be followed by a number between 1-9
            # It has to end with a number between 0-9
            # It may contain 0-9 (space) .-() in the middle.

            if (
                len(PHONE_NOs_LIST) != 0
            ):
                await lock_action(message, action=21)
    
    if 22 in LOCKS_LIST:
        if message.photo:
            await lock_action(message, action=27)

    if 23 in LOCKS_LIST:
        if message.poll:
            await lock_action(message, action=23)
    
    if 24 in LOCKS_LIST:
        text = (
            message.text
            or message.caption
        )

        if text:
            RTL_LIST = [
                'ar', # Arabic,
                'dv', # Divehi
                'fa', # Persian (Farsi)
                'ha', # Hausa
                'he', # Hebrew
                'iw', # Hebrew (old code)
                'ji', # Yiddish (old code)
                'ps', # Pashto, Pushto
                'ur', # Urdu
                'yi'  # Yiddish
                ]
            if not text.isdigit():
                return
            detected_lang = detect(text)
            if detected_lang in RTL_LIST:
                await lock_action(message, action=24)
    
    if 25 in LOCKS_LIST:
        if message.sticker:
            await lock_action(message, action=25)
    
    if 26 in LOCKS_LIST:
        if (
            message.text
            or message.caption
        ):
            await lock_action(message, action=26)

    if 27 in LOCKS_LIST: 
        text = (
            message.text
            or message.caption
        )

        if text:
            extractor = URLExtract()
            URL_LIST = extractor.find_urls(text)
            ALLOW_LIST = get_allowlist(chat_id)
            if (
                len(URL_LIST) != 0
            ):
                ALLOW_LIST = get_allowlist(chat_id)
                if (
                    len(ALLOW_LIST) != 0
                ):  
                    for url in URL_LIST:
                        if url not in ALLOW_LIST:
                            await lock_action(message, action=27)
                            break
                else:
                    await lock_action(message, action=27) 

    if 28 in LOCKS_LIST:
        if message.video:
            await lock_action(message, action=28)
    
    if 29 in LOCKS_LIST:
        if message.video_note:
            await lock_action(message, action=29)

    if 30 in LOCKS_LIST:
        if message.voice:
            await lock_action(message, action=30)



async def lock_action(message, action: int = None, delete: bool = True):
    lock_name = lock_map.LocksMap(action).name
    if await isUserAdmin(message, silent=True):
        return
    if not await check_bot(message, permissions=['can_delete_messages', 'can_restrict_members']):
        return
    if lockwarns_db:
        reason = (
            f"{lock_name} is locked in this chat."
        )
        await warn(message, reason, warn_user=message)
    if delete:
        await message.delete()

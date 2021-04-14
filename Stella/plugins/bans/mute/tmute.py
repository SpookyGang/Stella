import html 
import time

from pyrogram.types import ChatPermissions

from Stella import StellaCli, BOT_ID

from Stella.helper import custom_filter
from Stella.helper.chat_status import (
    isBotAdmin,
    isUserAdmin,
    can_restrict_member
)
from Stella.helper.get_user import get_user_id, get_text
from Stella.helper.time_checker import get_time
from Stella.helper.convert import convert_time
from Stella.helper.anon_admin import anonadmin_checker


@StellaCli.on_message(custom_filter.command(commands=('tmute')))
@anonadmin_checker
async def tmute(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isBotAdmin(message):
        return

    if not await isUserAdmin(message):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    if user_id == BOT_ID:
        await message.reply(
            "You know what I'm not going to do? mute myself."
        )
        return

    if not await can_restrict_member(message, user_id):
        await message.reply(
            "Why would I mute an admin? That sounds like a pretty dumb idea."
        )
        return
    
    time_args = await get_time(message)
    time_limit, time_format = time_string_helper(time_args)

    if time_args:
        cal_time = convert_time(int(time_args[:-1]), time_args[-1])
        until_time = int(time.time() + int(cal_time))
        await StellaCli.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
            can_send_messages=False
            ),
            until_date=int(time.time()) + int(until_time)
        )
        

        text = f"{user_info.mention} was mute for {time_limit} {time_format}.\n"
        raw_reason = get_text(message)
        reason = ' '.join(raw_reason.split()[1:])
        if reason:
            text += f"Reason: {reason}"
        await message.reply(
            text
        )
    
    
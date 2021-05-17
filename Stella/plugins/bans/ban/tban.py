import html
import time

from Stella import BOT_ID, StellaCli
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import CheckAllAdminsStuffs, can_restrict_member
from Stella.helper.convert import convert_time
from Stella.helper.get_user import get_text, get_user_id
from Stella.helper.time_checker import get_time, time_string_helper


@StellaCli.on_message(custom_filter.command(commands=('tban')))
@anonadmin_checker
async def tban(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title
    
    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    if user_id == BOT_ID:
        await message.reply(
            "You know what I'm not going to do? Ban myself."
        )
        return

    if not await can_restrict_member(message, user_id):
        await message.reply(
            "Why would I ban an admin? That sounds like a pretty dumb idea."
        )
        return
    
    time_args = await get_time(message)
    if time_args:
        cal_time = convert_time(int(time_args[:-1]), time_args[-1])
        until_time = int(time.time() + int(cal_time))
        await StellaCli.kick_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            until_date=until_time
            )
        
        time_limit, time_format = time_string_helper(time_args)

        text = f"{user_info.mention} was banned for {time_limit} {time_format}.\n"
        raw_reason = get_text(message)
        reason = ' '.join(raw_reason.split()[1:])
        if reason:
            text += f"Reason: {reason}"
        await message.reply(
            text
        )
    
    
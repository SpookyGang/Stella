import html
from enum import Enum, auto

from Stella import StellaCli
from Stella.database.antiflood_mongo import set_antiflood_mode
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs
from Stella.helper.time_checker import get_time, time_string_helper


class FloodModeMap(Enum):
    ban = auto()  
    mute = auto()  
    kick = auto()   
    tban = auto()   
    tmute = auto()

@StellaCli.on_message(custom_filter.command(commands=('setfloodmode')))
async def setfloodmode(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title

    if not await CheckAllAdminsStuffs(message, permissions=['can_delete_messages', 'can_restrict_members']):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You need to specify an action to take upon flooding. Current modes are: ban/kick/mute/tban/tmute"
        )
        return 
    
    arg = message.command[1]
    if (
        arg == 'ban'
    ):
        mode_id = FloodModeMap.ban.value
        set_antiflood_mode(chat_id, mode_id)
        await message.reply(
            f"Updated antiflood reaction in {html.escape(chat_title)} to: banned"
        )
    
    elif (
        arg == 'mute'
    ):
        mode_id = FloodModeMap.mute.value
        set_antiflood_mode(chat_id, mode_id)
        await message.reply(
            f"Updated antiflood reaction in {html.escape(chat_title)} to: muted"
        )
    
    elif (
        arg == 'kick'
    ):
        mode_id = FloodModeMap.kick.value
        set_antiflood_mode(chat_id, mode_id)
        await message.reply(
            f"Updated antiflood reaction in {html.escape(chat_title)} to: kicked"
        )
    
    elif (
        arg == 'tban'
    ):
        mode_id = FloodModeMap.tban.value
        time_args = await get_time(message)
        time_limit, time_format = time_string_helper(time_args)
        set_antiflood_mode(chat_id, mode_id, time_args)
        await message.reply(
            f"Updated antiflood reaction in {html.escape(chat_title)} to: temporarily banned for {time_limit} {time_format}"
        )
    
    elif (
        arg == 'tmute'
    ):
        mode_id = FloodModeMap.tmute.value
        time_args = await get_time(message)
        time_limit, time_format = time_string_helper(time_args)
        set_antiflood_mode(chat_id, mode_id, time_args)
        await message.reply(
            f"Updated antiflood reaction in {html.escape(chat_title)} to: temporarily muted for {time_limit} {time_format}"
        )
    
    else:
        await message.reply(
            f"Unknown type '{arg}'. Please use one of: ban/kick/mute/tban/tmute"
        )

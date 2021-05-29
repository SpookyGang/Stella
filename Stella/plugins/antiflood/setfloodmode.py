#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
            "You're gonns need to specify an action to take upon flooding. Supported modes are: `ban/kick/mute/tban/tmute`"
        )
        return 
    
    arg = message.command[1]
    if (
        arg == 'ban'
    ):
        mode_id = FloodModeMap.ban.value
        set_antiflood_mode(chat_id, mode_id)
        await message.reply(
            f"I've updated antiflood action in {html.escape(chat_title)} to: `banned`"
        )
    
    elif (
        arg == 'mute'
    ):
        mode_id = FloodModeMap.mute.value
        set_antiflood_mode(chat_id, mode_id)
        await message.reply(
            f"I've updated antiflood action in {html.escape(chat_title)} to: `muted`"
        )
    
    elif (
        arg == 'kick'
    ):
        mode_id = FloodModeMap.kick.value
        set_antiflood_mode(chat_id, mode_id)
        await message.reply(
            f" I've updated antiflood action in {html.escape(chat_title)} to: `kicked`"
        )
    
    elif (
        arg == 'tban'
    ):
        mode_id = FloodModeMap.tban.value
        time_args = await get_time(message)
        time_limit, time_format = time_string_helper(time_args)
        set_antiflood_mode(chat_id, mode_id, time_args)
        await message.reply(
            f"I've updated antiflood action in {html.escape(chat_title)} to: `temporarily banned for {time_limit} {time_format}`"
        )
    
    elif (
        arg == 'tmute'
    ):
        mode_id = FloodModeMap.tmute.value
        time_args = await get_time(message)
        time_limit, time_format = time_string_helper(time_args)
        set_antiflood_mode(chat_id, mode_id, time_args)
        await message.reply(
            f"I've updated antiflood action in {html.escape(chat_title)} to: `temporarily muted for {time_limit} {time_format}`"
        )
    
    else:
        await message.reply(
            f"I don't recognize this argument '{arg}'. Please use one of: `ban/kick/mute/tban/tmute`"
        )

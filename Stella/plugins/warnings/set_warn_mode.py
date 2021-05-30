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
from Stella.database.warnings_mongo import set_warn_mode_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import isBotAdmin, isUserCan
from Stella.helper.convert import convert_time
from Stella.helper.time_checker import get_time, time_string_helper


class WarnModeMap(Enum):
    Ban = auto()
    Kick = auto()
    Mute = auto()
    Tban = auto()
    Tmute = auto()

@StellaCli.on_message(custom_filter.command(commands='setwarnmode'))
async def set_warn_mode(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title 

    if not await isUserCan(message, permissions='can_restrict_members' ,silent=True):
        await message.reply(
            "You need to be an admin to do this."
        )
        return
    
    if not await isBotAdmin(message, silent=True):
        await message.reply(
            f"I am not admin in {html.escape(chat_title)}!\n"
            "you want me to set different warn modes, I need to be admin."
        )
        return
    
    if (
        len(message.command) >= 2
    ):
        args = message.command[1]
        
        if (
            args == 'ban'
        ):
            warn_mode_map = WarnModeMap.Ban.value
            set_warn_mode_db(chat_id, warn_mode_map, time=None)
            await message.reply(
                "Updated warning mode to: `banned`"
            )

        elif (
            args == 'kick'
        ):
            warn_mode_map = WarnModeMap.Kick.value
            set_warn_mode_db(chat_id, warn_mode_map, time=None)
            await message.reply(
                "Updated warning mode to: `kicked`"
            )
        
        elif (
            args == 'mute'
        ):
            warn_mode_map = WarnModeMap.Mute.value
            set_warn_mode_db(chat_id, warn_mode_map, time=None)
            await message.reply(
                "Updated warning mode to: `muted`"
            )
        
        elif (
            args == 'tban'
        ):
            warn_mode_map = WarnModeMap.Tban.value
            time_args = await get_time(message)
            cal_time = convert_time(int(time_args[:-1]), time_args[-1])
            time_limit, time_format = time_string_helper(time_args)
            set_warn_mode_db(chat_id, warn_mode_map, time=cal_time)
            await message.reply(
                f"Updated warning mode to: `temporarily banned for {time_limit} {time_format}`"
            )
        
        elif (
            args == 'tmute'
        ):
            warn_mode_map = WarnModeMap.Tmute.value
            time_args = await get_time(message)
            cal_time = convert_time(int(time_args[:-1]), time_args[-1])
            time_limit, time_format = time_string_helper(time_args)
            set_warn_mode_db(chat_id, warn_mode_map, time=cal_time)
            await message.reply(
                f"Updated warning mode to: `temporarily muted for {time_limit} {time_format}`"
            )
        else:
            await message.reply(
                f"i don't recognize this argument: '{args}'. Please use one of: ban/kick/mute/tban/tmute"
            )
    else:
        await message.reply(
            "You need to specify an action to take upon too many warns. Current modes are: ban/kick/mute/tban/tmute"
        )

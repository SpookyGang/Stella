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


import time

from pyrogram.types import ChatPermissions, Message
from Stella import StellaCli
from Stella.database.antiflood_mongo import get_antiflood_mode
from Stella.helper.chat_status import can_restrict_member
from Stella.helper.convert import convert_time
from Stella.helper.time_checker import time_string_helper


async def AntiFLoodModeAction(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_mention = message.from_user.mention 

    FloodMode, Flood_until_time = get_antiflood_mode(chat_id)
    if FloodMode == 1:
        await StellaCli.kick_chat_member(
            chat_id,
            user_id
        )
        await message.reply(
            f"Yeah, I ain't gonna leave your flooding be! \n{user_mention} has been banned!"
        )
    
    elif FloodMode == 2:
        await StellaCli.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
                can_send_messages=False
            )
        )
        await message.reply(
            f"Yeah, I ain't gonna leave your flooding be! \nQuiet now {user_mention}!"
        )
    
    elif FloodMode == 3:
        await StellaCli.kick_chat_member(
            chat_id,
            user_id,
            int(time.time()) + 60 # wait 60 seconds in case of server goes down at unbanning time
        )
        await message.reply(
            f"Yeah, I ain't gonna leave your flooding be! \n{user_mention} has been kicked!"
        )

        # Unbanning proceess and wait 5 sec to give server to kick user first
        await asyncio.sleep(5) 
        await StellaCli.unban_chat_member(chat_id, user_id)

    elif FloodMode == 4:
        until_time = convert_time(int(Flood_until_time[:-1]), Flood_until_time[-1])
        time_limit, time_format = time_string_helper(Flood_until_time)
        await StellaCli.kick_chat_member(
            chat_id,
            user_id,
            int(time.time()) + int(until_time)
        )
        
        await message.reply(
                f"Yeah, I ain't gonna leave your flooding be! \n{user_mention} has been banned for {time_limit} {time_format}!"
        )
    
    elif FloodMode == 5:
        until_time = convert_time(int(Flood_until_time[:-1]), Flood_until_time[-1])
        time_limit, time_format = time_string_helper(Flood_until_time)
        await StellaCli.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
            can_send_messages=False
            ),
            until_date=int(time.time()) + int(until_time)
        )
        await message.reply(
                f"Yeah, I ain't gonna leave your flooding be! \n{user_mention} has been muted for {time_limit} {time_format}!"
        )

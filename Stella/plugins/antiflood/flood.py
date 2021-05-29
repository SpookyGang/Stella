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


from Stella import StellaCli
from Stella.database.antiflood_mongo import (get_antiflood_mode, get_flood,
                                             get_floodlimit)
from Stella.helper import custom_filter
from Stella.helper.time_checker import time_string_helper


@StellaCli.on_message(custom_filter.command(commands=('flood')))
async def flood(client, message):

    chat_id = message.chat.id
    if not get_flood(chat_id):
        await message.reply(
            "This chat isn't currently enforcing flood control."
        )
        return 
    
    FLOOD_LIMIT = get_floodlimit(chat_id)
    FLOOD_MODE, FLOOD_TIME = get_antiflood_mode(chat_id)
    text = (
        f"This chat is currently enforcing flood control after {FLOOD_LIMIT} messages. "
    )
    if FLOOD_MODE == 1:
        text += "Any user that sends more than that amount of messages will be banned."
    elif FLOOD_MODE == 2:
        text += "Any user that sends more than that amount of messages will be muted."
    elif FLOOD_MODE == 3:
        text += "Any user that sends more than that amount of messages will be kicked."
    elif FLOOD_MODE == 4:
        time_limit, time_format = time_string_helper(FLOOD_TIME)
        text += f"Any user that sends more than that amount of messages will be temporarily banned for {time_limit} {time_format}."
    elif FLOOD_MODE == 5:
        time_limit, time_format = time_string_helper(FLOOD_TIME)
        text += f"Any user that sends more than that amount of messages will be temporarily muted for {time_limit} {time_format}."

    await message.reply(
        text
    )

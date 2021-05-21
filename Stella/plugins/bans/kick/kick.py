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


import asyncio
import html
import time

from Stella import BOT_ID, StellaCli
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import (can_restrict_member, isBotCan,
                                       isUserAdmin)
from Stella.helper.get_user import get_text, get_user_id


@StellaCli.on_message(custom_filter.command(commands=['kick', 'dkick', 'skick']))
@anonadmin_checker
async def kick(client, message):
        
    chat_id = message.chat.id 
    chat_title = message.chat.title
    message_id = None
    if not await isUserAdmin(message):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    if user_id == BOT_ID:
        await message.reply(
            "You know what I'm not going to do? kick myself."
        )
        return

    if not await isBotCan(message, permissions='can_restrict_members'):
        return

    if not await can_restrict_member(message, user_id):
        await message.reply(
            "Why would I kick an admin? That sounds like a pretty dumb idea."
        )
        return
    
    await StellaCli.kick_chat_member(
        chat_id,
        user_id,
        int(time.time()) + 60 # wait 60 seconds in case of server goes down at unbanning time
        )
    
    if message.command[0].find('dkick') >= 0:
        if message.reply_to_message:
            message_id = message.reply_to_message.message_id

    elif message.command[0].find('skick') >= 0:
        message_id = message.message_id   
    
    
    if not message.command[0].find('skick') >= 0:
        text = f"{user_info.mention} is kicked in {html.escape(chat_title)}.\n"
        
        reason = get_text(message)
        if reason:
            text += f"Reason: {reason}"

        await message.reply(
            text
        )
    
    # Deletaion of message according to user admin command
    if message_id is not None:
        await StellaCli.delete_messages(
                chat_id=chat_id,
                message_ids=message_id
            )
    
    # Unbanning proceess and wait 5 sec to give server to kick user first
    await asyncio.sleep(5) 
    await StellaCli.unban_chat_member(chat_id, user_id)

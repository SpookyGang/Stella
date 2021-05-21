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


from pyrogram import filters
from Stella import StellaCli
from Stella.database.federation_mongo import (get_fed_from_chat,
                                              get_fed_reason, is_user_fban)
from Stella.helper.chat_status import isBotCan


@StellaCli.on_message(filters.all & filters.group, group=2)
async def fed_checker(client, message):
    
    chat_id = message.chat.id
    
    if not message.from_user:
        return

    user_id = message.from_user.id 
    fed_id = get_fed_from_chat(chat_id)
    
    if not fed_id == None:
        if is_user_fban(fed_id, user_id):
            fed_reason = get_fed_reason(fed_id, user_id)
            text = (
                    "**This user is banned in the current federation:**\n\n"
                    f"User: {message.from_user.mention} (`{message.from_user.id}`)\n"
                    f"Reason: `{fed_reason}`"
                )
            if await isBotCan(message, permissions='can_restrict_members'):
                if await StellaCli.kick_chat_member(chat_id, user_id): 
                    text += '\nAction: `Banned`'
            
            await message.reply(
                text
            )
            return 

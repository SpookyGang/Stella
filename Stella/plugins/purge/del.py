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
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs


@StellaCli.on_message(custom_filter.command(commands=('del')))
async def delete(client, message):
    chat_id = message.chat.id
    message_id = message.message_id

    if not await CheckAllAdminsStuffs(message, permissions='can_delete_messages'):
        return

    if not message.reply_to_message:
        await message.reply(
            'Reply to any message to delete message.'
        )
        return
        
    try:
        reply_to_message = message.reply_to_message.message_id
        await StellaCli.delete_messages(
            chat_id=chat_id,
            message_ids=(
                [message_id, reply_to_message]
            )
        )
    except:
        await message.reply(
            "I can't delete messages here! Make sure I'm admin and can delete other user's messages."
        )

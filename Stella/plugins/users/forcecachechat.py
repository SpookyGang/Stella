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
from Stella.database.users_mongo import add_chat
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin


@StellaCli.on_message(custom_filter.command(commands=('forcecachechat')))
async def forcecachechat(client, message):
    chat_id = message.chat.id 
    chat_title = message.chat.title

    if (
        message.chat.type == 'private'
    ):
        await message.reply(
            "This command is made to be used in group chats, not in pm!"
        )
        return 
    
    if not await isUserAdmin(message):
        return
    
    add_chat(chat_id, chat_title)
    await message.reply(
        "I've exported your chat's data to my database. I hope to not forget it again~ tee-hee"
    )
    

    

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
from Stella.database.users_mongo import add_chat, add_user


@StellaCli.on_message(filters.all & filters.group, group=1)
async def logger(client, message):
    if message.chat:
        chat_id = message.chat.id
        chat_title = message.chat.title
        add_chat(chat_id, chat_title)

    if message.from_user:
        user_id = message.from_user.id
        username = message.from_user.username
        chat_id = message.chat.id
        chat_title = message.chat.title
        add_user(user_id, username, chat_id, chat_title)
        add_chat(chat_id, chat_title)
    
    if (
        message.reply_to_message
        and message.reply_to_message.from_user
    ):

        user_id = message.reply_to_message.from_user.id
        username = message.reply_to_message.from_user.username
        chat_id = message.chat.id 
        chat_title = message.chat.title
        
        add_user(user_id, username, chat_id, chat_title)
        add_chat(chat_id, chat_title)

    if message.forward_from:

        user_id = message.forward_from.id
        username = message.forward_from.username
    
        add_user(user_id, username, Forwared=True)

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

from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.disable import disable


@StellaCli.on_message(custom_filter.command(commands=('adminlist'), disable=True))
@disable
async def admin_list(client, message):
    chat_title = message.chat.title 
    chat_id = message.chat.id 

    data_list = await StellaCli.get_chat_members(
        chat_id=chat_id,
        filter='administrators'
        )
    ADMINS_LIST = []
    for user in data_list:
        if user.user.username is not None:
            ADMINS_LIST.append(f'- <a href=tg://user?id={user.user.username}>{user.user.first_name}</a> id `{user.user.id}`\n')
        else:
            ADMINS_LIST.append(f'- <a href=tg://user?id={user.user.id}>{user.user.first_name}</a> id `{user.user.id}`\n')


    admin_header = f"Admins in {html.escape(chat_title)}:\n"
    
    for admin in ADMINS_LIST:
        admin_header += admin
    await message.reply(
        (
            f"{admin_header}\n\n"
            "__These are the updated values.__"
        ),
        quote=True
    )
        

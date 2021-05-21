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
from Stella.database.federation_mongo import (get_fed_name, is_fed_exist,
                                              join_fed_db)
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCreator


@StellaCli.on_message(custom_filter.command(commands=('joinfed')))
async def JoinFeb(client, message):
    
    if not (
        message.chat.type == 'supergroup'
    ):
        await message.reply(
            "Only supergroups can join feds."
        )
        return 
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You need to specify which federation you're asking about by giving me a FedID!"
        )
        return

    if not (
        await isUserCreator(message)
    ):
        await message.reply(
            "Only Group Creator can join new fed!"
        )
        return 

    if not (
        is_fed_exist(message.command[1])
    ):
        await message.reply(
            "This FedID does not refer to an existing federation."
        )
        return

    fed_id = message.command[1]
    chat_id = message.chat.id
    chat_title = html.escape(message.chat.title)
    fed_name = get_fed_name(fed_id)

    join_fed_db(chat_id, chat_title,  fed_id)
    await message.reply(
        f'Successfully joined the "{fed_name}" federation! All new federation bans will now also remove the members from this chat.'
    )

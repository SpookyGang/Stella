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
from Stella.database.connection_mongo import (GetConnectedChat,
                                              get_allow_connection,
                                              isChatConnected)
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin, isUserBanned
from Stella.plugins.connection.connect import connect_button


@StellaCli.on_message(custom_filter.command(commands=('connection')))
async def ConnectionChat(client, message):
    if not (
        message.chat.type == 'private'
    ):
        await message.reply(
            "You need to be in PM to use this."
        )
        return
    if await connection(message) is not None:
        chat_id = await connection(message)
        await connect_button(message, chat_id)
    else:
        await message.reply(
            "You aren't connected to any chat :)",
            quote=True
        )


async def connection(message):
    if not (
        message.chat.type == 'private'
    ):
        return None
        
    user_id = message.from_user.id
    connected_chat = GetConnectedChat(user_id)
    if isChatConnected:
        if connected_chat is not None:
            if get_allow_connection(connected_chat):
                if not await isUserBanned(connected_chat, user_id):
                    return connected_chat
                else:
                    await message.reply(
                        f"You are banned user of {chat_title}",
                        quote=True
                    )
                    return None
            else:
                return None
        else:
            return None
    else:
        return None
    
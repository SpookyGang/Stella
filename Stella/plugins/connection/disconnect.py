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
from Stella.database.connection_mongo import disconnectChat
from Stella.helper import custom_filter
from Stella.plugins.connection.connection import connection


@StellaCli.on_message(custom_filter.command(commands=('disconnect')))
async def diconnectChat(client, message):
    user_id = message.from_user.id 
    if not (
        message.chat.type == 'private'
    ):
        await message.reply(
            "You need to be in pm to use this."
        )
        return
    if await connection(message) is not None:
        disconnectChat(user_id)
        await message.reply(
            "Disconnected from chat.",
            quote=True
        )
    else:
        await message.reply(
            "You aren't connected to any chats! Anything you save here is for your eyes only :)",
            quote=True
        )

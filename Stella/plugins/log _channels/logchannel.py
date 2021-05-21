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
from Stella.database.log_channels_mongo import get_set_channel
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import isUserAdmin
from Stella.plugins.connection.connection import connection


@StellaCli.on_message(custom_filter.command(commands=('logchannel')))
@anonadmin_checker
async def logcategories(client, message):
    
    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id 

    if not await isUserAdmin(message):
        return 
    
    if get_set_channel(chat_id) is not None:
        channel_title = get_set_channel(chat_id)
        await message.reply(
            f"I am currently logging admin actions in '{html.escape(channel_title)}'.",
            quote=True
        )
    else:
        await message.reply(
            "There are no log channels assigned to this chat.",
            quote=True
        )


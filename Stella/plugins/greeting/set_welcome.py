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
from Stella.database.welcome_mongo import SetWelcome
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import isUserCan
from Stella.helper.welcome_helper.get_welcome_message import GetWelcomeMessage
from Stella.plugins.connection.connection import connection


@StellaCli.on_message(custom_filter.command(commands=('setwelcome')))
@anonadmin_checker
async def set_welcome(client, message):

    if await connection(message) is not None:
        ChatID = await connection(message)
    else:
        ChatID = message.chat.id

        if message.chat.type == 'private':
            await message.reply(
                "This command is only made for grup, not for PM."
            )
            return

    if not await isUserCan(message, permissions='can_change_info'):
        return

    if (
        not message.reply_to_message
        and not len(message.command) > 1
    ):
        await message.reply(
            "You need to give the welcome message some content!"
        )  
        return

    CONTENT, TEXT, DATATYPE = GetWelcomeMessage(message)
    print(CONTENT, TEXT, DATATYPE)
    SetWelcome(
        ChatID,
        CONTENT,
        TEXT,
        DATATYPE
    )

    await message.reply(
        "The new welcome message has been saved!",
        quote=True
    )

    
    
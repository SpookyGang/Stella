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
from Stella.database.chats_settings_mongo import anonadmin_db, get_anon_setting
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCreator

ANONADMIN_TRUE = ['yes', 'on']
ANONADMIN_FALSE = ['no', 'off']

@StellaCli.on_message(custom_filter.command(commands=('anonadmin')))
async def anon_admin(client, message):
    
    chat_id = message.chat.id 
    chat_title = message.chat.title 

    if not await isUserCreator(message):
        await message.reply(
            "Only the group creator can execute this command"
        )
        return
    
    if len(message.command) >= 2:
        args = message.command[1]

        if (
            args in ANONADMIN_TRUE
        ):  
            anonadmin_db(chat_id, True)
            await message.reply(
                f"The anon admin setting for {html.escape(chat_title)} has been updated to true."
            )
        elif (
            args in ANONADMIN_FALSE
        ):
            anonadmin_db(chat_id, False)
            await message.reply(
                f"The anon admin setting for {html.escape(chat_title)} has been updated to false."
            )
        else:
            await message.reply(
                f"failed to get boolean from input: expected one of y/yes/on or n/no/off; got: {args}"
            )
    
    else:
        if get_anon_setting(chat_id):
            await message.reply(
                f"{html.escape(chat_title)} currently allows all anonymous admins to use any admin command without restriction."
            )
        else:
            await message.reply(
                f"{html.escape(chat_title)} currently requires anonymous admins to press a button to confirm their permissions."
            )

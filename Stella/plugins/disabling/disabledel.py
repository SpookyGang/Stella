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
from Stella.database.disable_mongo import disabledel_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import check_bot, check_user

DISABLEDEL_TRUE = ['on', 'yes']
DISABLEDEL_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('disabledel')))
async def disabledel(client, message):

    chat_id = message.chat.id

    if not await check_bot(message, permissions='can_delete_messages'):
        return

    if not await check_user(message, permissions='can_change_info'):
        return
    
    if (
        len(message.command) >= 2
    ):
        arg = message.command[1]
        if (
            arg in DISABLEDEL_TRUE
        ):
            disabledel_db(chat_id, True)
            await message.reply(
                "Disabled messages will now be deleted."
            )
        
        elif (
            arg in DISABLEDEL_FALSE
        ):
            disabledel_db(chat_id, False)
            await message.reply(
                "Disabled messages will no longer be deleted."
            )
        
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )
    else:
        await message.reply(
            "You need to give me a setting; yes/no/on/off"
        )

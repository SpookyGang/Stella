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
from Stella.database.locks_mongo import lockwarns_db, set_lockwarn_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import check_user

LOCKWARN_TRUE = ['on', 'yes']
LOCKWARN_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('lockwarns')))
async def lockwarns(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title
    if (
        len(message.command) >= 2
    ):
        args = message.command[1]
        if (
            args in LOCKWARN_TRUE
        ):
            set_lockwarn_db(chat_id, True)
            await message.reply(
                "Lock warns have been enabled. Any user using locked messages will be warned, as well has have their message deleted."
            )
        
        elif (
            args in LOCKWARN_FALSE
        ):
            set_lockwarn_db(chat_id, False)
            await message.reply(
                "Lock warns have been disabled. Any user using locked messages will no longer be warned, and will only have their message deleted."
            )
        
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )
    else:
        if lockwarns_db(chat_id):
            await message.reply(
                f"I am currently warning all users who try to use locked message types in {html.escape(chat_title)}."
            )
        else:
            await message.reply(
                f"I am NOT warning all users who try to use locked message types in {html.escape(chat_title)}. I will simply delete the messages."
            )

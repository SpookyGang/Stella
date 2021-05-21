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
from Stella.database.rules_mongo import get_private_note, set_private_rule
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import isUserCan

PRIVATE_RULES_TRUE = ['yes', 'on']
PRIVATE_RULES_FALSE = ['no', 'off']

@StellaCli.on_message(custom_filter.command(commands=('privaterules')))
@anonadmin_checker
async def private_rules(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if (
        len(message.command) >= 2
    ):
        args = message.command[1]

        if (
            args in PRIVATE_RULES_TRUE
        ):
            set_private_rule(chat_id, True)
            await message.reply(
                "Use of /rules will send the rules to the user's PM.",
                quote=True
            )

        elif (
            args in PRIVATE_RULES_FALSE
        ):
            set_private_rule(chat_id, False)
            await message.reply(
                f"All /rules commands will send the rules to {html.escape(chat_title)}.",
                quote=True
            )

        else:
            await message.reply(
                "I only understand the following: yes/no/on/off",
                quote=True
            )
    else:
        if get_private_note(chat_id):
            await message.reply(
                "Use of /rules will send the rules to the user's PM."
            )
        else:
            await message.reply(
                f"All /rules commands will send the rules to UPDATED! {html.escape(chat_title)}."
            )

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
from Stella.database.pin_mongo import (antichannelpin_db, cleanlinked_db,
                                       get_antichannelpin, get_cleanlinked)
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs

CLEAN_LINKED_TRUE = ['on', 'yes']
CLEAN_LINKED_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('cleanlinked')))
async def cleanlinked(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title
    if not await CheckAllAdminsStuffs(message, permissions='can_delete_messages'):
        return
    
    if (
        len(message.command) >= 2
    ):
        args = message.command[1]
        if (
            args in CLEAN_LINKED_TRUE
        ):
            ANTICHANNEL_PIN = get_antichannelpin(chat_id)
            if ANTICHANNEL_PIN:
                await message.reply(
                    "I've disabled `/antichannelpin`. Do /pininfo to know why or you can also read the `/help`."
                )
                antichannelpin_db(chat_id, False)
                
            cleanlinked_db(chat_id, True)
            await message.reply(
                f"**Enabled** linked channel post deletion in {html.escape(chat_title)}. Messages sent from the linked channel will be deleted."
            )
        
        elif (
            args in CLEAN_LINKED_FALSE
        ):
            cleanlinked_db(chat_id, False)
            await message.reply(
                f"**Disabled** linked channel post deletion in {html.escape(chat_title)}."
            )
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )

    else:
        IS_CLEAN_LINK = get_cleanlinked(chat_id)
        if IS_CLEAN_LINK:
            await message.reply(
                f"Linked channel post deletion is currently **enabled** in {html.escape(chat_title)}. Messages sent from the linked channel will be deleted."
            )
        
        else:
            await message.reply(
                f"Linked channel post deletion is currently **disabled** in {html.escape(chat_title)}."
            )

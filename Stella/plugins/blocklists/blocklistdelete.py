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
from Stella.database.blocklists_mongo import (blocklistMessageDelete,
                                              getblocklistMessageDelete)
from Stella.helper import custom_filter
from Stella.helper.chat_status import isBotCan, isUserCan

BLOCKLIST_DELETE_TRUE = ['on', 'yes']
BLOCKLIST_DELETE_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands='blocklistdelete'))
async def blocklistdelete(client, message):

    chat_id = message.chat.id 

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if not await isBotCan(message, permissions='can_delete_messages'):
        return

    if (
        len(message.command) >= 2 
    ):
        args = message.command[1]

        if (
            args in BLOCKLIST_DELETE_TRUE
        ):
            blocklistMessageDelete(chat_id, True)
            await message.reply(
                "Blocklist deletes have now been **enabled**. I will be deleting all blocklisted messages from now on."
            )
        
        elif (
            args in BLOCKLIST_DELETE_FALSE
        ):
            blocklistMessageDelete(chat_id, False)
            await message.reply(
                "Blocklist deletes have now been **disabled**. I will no longer be deleting any blocklisted messages. However, I will still take actions; such as warnings, or bans."
            )
        
        else:
            await message.reply(
                "Your input was not recognised as one of: `yes/no/on/off`"
            )
    else:
        if getblocklistMessageDelete:
            await message.reply(
                "I am currently deleting all blocklisted messages."
            )
        else:
            await message.reply(
                "I am currently **not** deleting blocklisted messages."
            )

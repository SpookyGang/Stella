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
from Stella.database.locks_mongo import get_locks
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin

from . import lock_map


@StellaCli.on_message(custom_filter.command(commands=('locks')))
async def locks(client, message):

    chat_id = message.chat.id

    if not await isUserAdmin(message):
        return
    
    LOCKS_LIST = get_locks(chat_id)

    if (
        len(LOCKS_LIST) == 0
    ):
        await message.reply(
            "No items locked in this chat."
        )
        return
        
    if 1 in LOCKS_LIST:
        await message.reply(
            "Jokes on you, everything's locked."
        )
        return
        
    text = "These are the currently locked items:\n"
    for item in LOCKS_LIST:
        lock_name = lock_map.LocksMap(item).name
        text += f'- `{lock_name}`\n'
    
    await message.reply(
        text
    )

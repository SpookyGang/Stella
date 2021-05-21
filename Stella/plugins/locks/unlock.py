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

from pyrogram.errors import BadRequest
from pyrogram.types import ChatPermissions
from Stella import StellaCli
from Stella.database.locks_mongo import unlock_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import check_bot, check_user

from . import lock_map


@StellaCli.on_message(custom_filter.command(commands=('unlock')))
async def lock(client, message):
    
    chat_id = message.chat.id

    if not await check_bot(message, permissions='can_restrict_members'):
        return

    if not await check_user(message, permissions='can_change_info'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You haven't specified a type to unlock."
        )
        return

    LOCKS_LIST = lock_map.LocksMap.list()

    lock_args = message.command[1:]
    
    LOCK_ITMES = []
    INCORRECT_ITEMS = []

    for lock in lock_args:
        if lock not in LOCKS_LIST:
            INCORRECT_ITEMS.append(lock)
        else:
            LOCK_ITMES.append(lock)
    
    if (
        len(INCORRECT_ITEMS) != 0
    ):
        text = (
            "Unknown unlock types:\n"
        )
        for item in INCORRECT_ITEMS:
            text += f'- {item}\n'
        text += "Check /locktypes!"
        await message.reply(
                text
            )
        return
    
    for item in LOCK_ITMES:
        lock_value = lock_map.LocksMap[item].value
        unlock_db(chat_id, lock_value)

    text = 'Unlocked:\n'
    for unlock_arg in LOCK_ITMES:
        if len(LOCK_ITMES) != 1:
            text += f'- `{unlock_arg}`\n'
        else:
            text = (
                f"Unlocked `{unlock_arg}`."
            )

    if 'all' in LOCK_ITMES:
        try:
            await StellaCli.set_chat_permissions(
                chat_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,   
                    can_send_stickers=True,
                    can_send_animations=True
                    )
            )
        except:
            await message.reply(    
                "All items are **already** unlocked."
            )
            return
        
        

    await message.reply(
        text
    )

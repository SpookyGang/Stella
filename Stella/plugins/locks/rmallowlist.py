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
from Stella.database.locks_mongo import get_allowlist, rmallow_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import check_user


@StellaCli.on_message(custom_filter.command(commands=('rmallowlist')))
async def rmallow(client, message):

    chat_id = message.chat.id
    if not await check_user(message, permissions='can_change_info'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You haven't given me any items to remove from the allowlist!"
        )
        return
    
    RMALLOW_LIST = message.command[1:]
    ALLOW_LIST = get_allowlist(chat_id)

    CORRECT_LIST = []
    INCORRECT_LIST = []

    for rmallow in RMALLOW_LIST:
        if rmallow in ALLOW_LIST:
            CORRECT_LIST.append(rmallow)
        else:
            INCORRECT_LIST.append(rmallow)
    if (
        len(INCORRECT_LIST) != 0
    ):
        text = (
            "The following items are not currently allowlisted, and so can't be removed from the allowlist:\n"
        )
        for item in INCORRECT_LIST:
            text += f'- `{item}`\n'
        
        await message.reply(
            text
        )
        return
    
    text = (
        "These items are has been successfully removed from the allowlist:\n"
    )
    for item in CORRECT_LIST:
        rmallow_db(chat_id, item)
        if len(CORRECT_LIST) == 1:
            text = f"'{item}' removed from the allowlist."
        else:
            text += f'- `{item}`\n'
    
    await message.reply(
        text
    )

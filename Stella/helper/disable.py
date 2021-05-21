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


from Stella.database.disable_mongo import get_disabled, get_disabledel
from Stella.helper.chat_status import isBotCan, isUserAdmin
from Stella.helper.custom_filter import DISABLE_COMMANDS


def disable(func):

    async def wrapper(client, message):
        if not message.command:
            return
        if not await isUserAdmin(message, silent=True):
            chat_id = message.chat.id
            command = message.command[0]
            DISABLED_LIST = get_disabled(chat_id)
            if command in DISABLED_LIST:
                if get_disabledel(chat_id):
                    if not await isBotCan(message, permissions='can_delete_messages'):
                        return
                    await message.delete()
                    return
                else:
                    return
            else:
                await func(client, message)
        else:
            await func(client, message)
    
    return wrapper

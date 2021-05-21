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
from Stella.database.warnings_mongo import (count_user_warn,
                                            get_all_warn_reason, warn_limit)
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.helper.disable import disable
from Stella.helper.get_user import get_user_id


@StellaCli.on_message(custom_filter.command(commands=('warns'), disable=True))
@disable
async def warns(client, message):

    chat_id = message.chat.id 
    if not await isUserAdmin(message):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id 

    user_warn_num = count_user_warn(chat_id, user_id)
    if user_warn_num is None:
        await message.reply(
            f"User {user_info.mention} has no warnings!"
        )
        return
    
    chat_warn_limit = warn_limit(chat_id)
    REASONS = get_all_warn_reason(chat_id, user_id)

    await message.reply(
        f"User {user_info.mention} has {user_warn_num}/{chat_warn_limit} warnings. Reasons are:\n{''.join(REASONS)}"
    )

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

from pyrogram import filters
from pyrogram.types import CallbackQuery
from Stella import StellaCli
from Stella.database.warnings_mongo import remove_warn
from Stella.helper.chat_status import isUserAdmin


@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'warn_' in query.data))
async def warn_remove_callback(client: StellaCli, callback_query: CallbackQuery):
    user_id = int(callback_query.data.split('_')[1])
    warn_id = int(callback_query.data.split('_')[2])
    chat_id = callback_query.message.chat.id
    from_user = callback_query.from_user.id 
    admin_mention = callback_query.from_user.mention 

    if not await isUserAdmin(message=callback_query.message, user_id=from_user, chat_id=chat_id, silent=True):
        await callback_query.answer(
            text='You are not admin to do this.'
        )
        return
    
    remove_warn(chat_id, user_id, warn_id)
    user_data= await StellaCli.get_users(
        user_ids=user_id
    )
    await callback_query.edit_message_text(
        f"Admin {admin_mention} has removed {user_data.mention}'s warning."
    )
    
    


   
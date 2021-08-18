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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from Stella import BOT_ID
from Stella.database.warnings_mongo import count_user_warn, warn_db, warn_limit
from Stella.helper.chat_status import can_restrict_member
from Stella.helper.get_user import get_user_id
from Stella.plugins.warnings.warn_checker import warn_checker


async def warn(message, reason, silent=False, warn_user=None):

    chat_id = message.chat.id 
    admin_id = message.from_user.id 
    
    if warn_user is None:
        user_info = await get_user_id(message)
        user_id = user_info.id
        if user_id == BOT_ID:
            await message.reply(
                "Bold of you to think I'm gonna warn myself!"
            )
            return

        if not await can_restrict_member(message, user_id):
            await message.reply(
                "Wish I could warn an admin but sadly enough that isn't technically possible!"
            )
            return

    else:
        user_info = warn_user.from_user
        user_id = warn_user.from_user.id 

    warn_db(chat_id, admin_id, user_id, reason)
    warnchecker = await warn_checker(message, user_id, silent)
    
    if (
        warnchecker is True
        or warnchecker is None
    ):
        return False

    countuser_warn = count_user_warn(chat_id, user_id)
    warnlimit = warn_limit(chat_id)

    warn_text = f"User {user_info.mention} has {countuser_warn}/{warnlimit} warnings; gotta be be careful from now on!\n"
    if reason:
        warn_text += f"**Reason:**\n{reason}"

    button = [[InlineKeyboardButton(text='Remove warn (admin only)', callback_data=f'warn_{user_id}_{countuser_warn}')]]

    if not silent:    
        await message.reply(
            text=warn_text,
            reply_markup=InlineKeyboardMarkup(button)
        )
        return True

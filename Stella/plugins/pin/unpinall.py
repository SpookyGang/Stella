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
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs, isUserCan


@StellaCli.on_message(custom_filter.command(commands=('unpinall')))
async def unpinall(client, message):

    chat_id = message.chat.id
    if not await CheckAllAdminsStuffs(message, permissions='can_pin_messages'):
        return 
    
    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='Yes', callback_data='unpin_yes'), 
        InlineKeyboardButton(text='No', callback_data='unpin_no')]]
    )

    await message.reply(
        text='Are you sure you want to unpin all messages?',
        reply_markup=button
    )

@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'unpin_' in query.data))
async def unpinall_callback(client: StellaCli, callback_query: CallbackQuery):

    query_data = callback_query.data.split('_')[1]  
    chat_id = callback_query.message.chat.id
    user_id = callback_query.from_user.id 
    if not await isUserCan(callback_query, user_id=user_id, chat_id=chat_id, permissions='can_pin_messages', silent=True):
        await callback_query.answer(
            text='you don\'t have permission to use this button.'
        )
        return 
    if query_data == 'yes':
        await StellaCli.unpin_all_chat_messages(
            chat_id=chat_id
        )
        await callback_query.edit_message_text(
            "All pinned messages have been unpinned."
        )
    elif query_data == 'no':
        await callback_query.edit_message_text(
            "Unpin of all pinned messages has been cancelled."
        )

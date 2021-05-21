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

from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import CallbackQuery
from Stella import StellaCli
from Stella.plugins.urban_dictionary.get_data import getData


@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'pagination_keyboard#' in query.data))
async def ud_callback(client: StellaCli, callback_query: CallbackQuery):
    
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id 
    CurrentPage = int(callback_query.data.split('#')[1]) 
    GetWord = callback_query.data.split('#')[2]

    try:
        UDReasult, PageLen = await getData(chat_id, message_id, GetWord, CurrentPage)
    except TypeError:
        return

    keyboard = InlineKeyboard()
    keyboard.paginate(PageLen, CurrentPage, 'pagination_keyboard#{number}' + f'#{GetWord}')
    await StellaCli.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=UDReasult,
        reply_markup=keyboard
    )

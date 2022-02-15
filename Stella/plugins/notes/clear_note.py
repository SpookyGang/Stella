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

import html

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)
from Stella import StellaCli
from Stella.database.notes_mongo import (ClearAllNotes, ClearNote, NoteList,
                                         isNoteExist)
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import CheckAdmins, isUserCreator
from Stella.helper.get_data import GetChat
from Stella.plugins.connection.connection import connection


@StellaCli.on_message(custom_filter.command(commands=('clear')))
@anonadmin_checker
async def Clear_Note(client, message):
    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id 

    if not await CheckAdmins(message):
        return

    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You need to give the note a name!",
            quote=True
        )
        return
    
    note_name = message.command[1].lower()

    if isNoteExist(chat_id, note_name):
        ClearNote(chat_id, note_name)

        await message.reply(
            f"I've removed the note `{note_name}`!.",
            quote=True
        )
    else:
        await message.reply(
            "You haven't saved a note with this name yet!",
            quote=True
        )


@StellaCli.on_message(custom_filter.command(commands=('clearall')))
async def ClearAll_Note(client, message):
    owner_id = message.from_user.id
    if await connection(message) is not None:
        chat_id = await connection(message)
        chat_title = await GetChat(chat_id)
        chat_title = html.escape(chat_title)
    else:
        chat_id = message.chat.id 
        chat_title = html.escape(message.chat.title)
        if message.chat.type == 'private':
            chat_title = 'local'

    if not await isUserCreator(message):
        await message.reply(
            f"You need to be the chat owner of {chat_title} to do this.",
            quote=True
        )
        return 

    note_list = NoteList(chat_id)
    if note_list == 0:
        await message.reply(
            f"No notes in {chat_title}",
            quote=True
        )
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton(text='Delete all notes', callback_data=f'clearallnotes_clear_{owner_id}_{chat_id}')
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data=f'clearallnotes_cancel_{owner_id}')
        ]]
    )
    await message.reply(
        f"Are you sure you want to clear **ALL** notes in {chat_title}? This action is irreversible.",
        reply_markup=keyboard,
        quote=True
    )

@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'clearallnotes_' in query.data))
async def ClearAllCallback(client: StellaCli, callback_query: CallbackQuery):
    query_data = callback_query.data.split('_')[1]
    owner_id = int(callback_query.data.split('_')[2])
    user_id = callback_query.from_user.id 

    if owner_id == user_id:
        if query_data == 'clear':
            chat_id = int(callback_query.data.split('_')[3])
            ClearAllNotes(chat_id)
            await callback_query.edit_message_text(
                "Deleted all chat notes."
            ) 
            return
    
        if query_data == 'cancel':
            await callback_query.edit_message_text(
                "Cancelled."
            )
    else:
        await callback_query.answer(
            "Only admins can execute this command!"
        )

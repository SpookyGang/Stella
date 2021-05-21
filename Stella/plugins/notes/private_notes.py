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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Stella import BOT_USERNAME
from Stella.helper.note_helper.note_send_message import exceNoteMessageSender


async def note_redirect(message):
    chat_id = int(message.command[1].split('_')[1])
    note_name = message.command[1].split('_')[2]
    await exceNoteMessageSender(message, note_name, from_chat_id=chat_id)

async def PrivateNoteButton(message, chat_id, NoteName):
    PrivateNoteButton = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text='Click me!', url=f'http://t.me/{BOT_USERNAME}?start=note_{chat_id}_{NoteName}')
            ]
        ]
    )
    await message.reply(
        text=f"Tap here to view '{NoteName}' in your private chat.",
        reply_markup=PrivateNoteButton
    )

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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Stella import BOT_USERNAME, StellaCli
from Stella.database.connection_mongo import connectDB, get_allow_connection
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.helper.get_data import GetChat


@StellaCli.on_message(custom_filter.command(commands=('connect')))
async def Connect(client, message):
    if message.chat.type == 'private':
        if not (
            len(message.command) >= 2
        ): 
            await message.reply(
                "I need a chat id to connect to!",
                quote=True
            )
            return 
        chat_id = message.command[1]
        if not (
            chat_id.startswith('-100')
        ):
            await message.reply(
                "I was expecting a chat id, but this isn't a valid integer",
                quote=True 
            )
            return 

        chat_title = await GetChat(int(chat_id))
        if chat_title is None:
            await message.reply(
                "failed to connect to chat!\nError: `chat not found`",
                quote=True 
            )
        else:
            await connect_button(message, int(chat_id))
    else:
        chat_id = message.chat.id 
        await message.reply(
            "Tap the following button to connect to this chat in PM",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="Connect to chat", url=f"http://t.me/{BOT_USERNAME}?start=connect_{chat_id}")]
                ]
            )
        )

async def connectRedirect(message):
    chat_id = int(message.text.split('_')[1])
    await connect_button(message, chat_id)

async def connect_button(message, chat_id):
    
    user_id = message.from_user.id
    if await isUserAdmin(message, chat_id, silent=True):
        keyboard = [[InlineKeyboardButton(text='Admin commands', callback_data='connect_admin')]]
        keyboard += [[InlineKeyboardButton(text='user commands', callback_data='connect_user')]]

    else:
        if get_allow_connection(chat_id):
            keyboard = [[InlineKeyboardButton(text='user commands', callback_data='connect_user')]]
        else:
            keyboard = []

    chat_title = await GetChat(chat_id)

    reply_markup = None
    text = f"Users are **not** allowed to connect in {html.escape(chat_title)}."
    if len(keyboard) > 0:
        connectDB(user_id, chat_id)
        reply_markup = InlineKeyboardMarkup(keyboard)
        text = f"You have been connected to {html.escape(chat_title)}!"

    await StellaCli.send_message(
        text=text,
        chat_id=message.from_user.id,
        reply_markup=reply_markup,
        reply_to_message_id=message.message_id
        ) 

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
from typing import Union

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from Stella import StellaCli
from Stella.database.rules_mongo import get_rules
from Stella.database.welcome_mongo import isRuleCaptcha
from Stella.helper.get_data import GetChat

from ..utils.actions import passedAction


async def ruleCaptchaButton(message: Union[Message, CallbackQuery], chat_id: int, message_id: int) -> bool:
    
    user_id = message.from_user.id 
    KEYBOARD = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='I have read and accept the rules', callback_data=f'captcharule_{chat_id}_{message_id}')]]
    )

    RULES = get_rules(chat_id=chat_id)
    if RULES is None:
        chat_title = GetChat(chat_id)
        RULES = (
            f"{html.escape(chat_title)} haven't any rules yet."
        )

    await StellaCli.send_message(
        chat_id=user_id,
        text=RULES,
        reply_markup=KEYBOARD
    )

@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'captcharule_' in query.data))
async def captchaRules(client: StellaCli, callback_query: CallbackQuery):
    
    user_id = callback_query.from_user.id 
    chat_id = int(callback_query.data.split('_')[1])
    message_id = int(callback_query.data.split('_')[2])

    await callback_query.answer(
        text=(
            'You have passed the CAPTCHA.'
        )
    )

    str_chat_id = str(chat_id).replace('-100', '')
    passedButton = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text='Go Back to the chat', url=f'http://t.me/c/{str_chat_id}/{message_id}')
                ]
            ]
        )
    
    await callback_query.edit_message_text(
        text='You have pass the CAPTCHA.',
        reply_markup=passedButton  
    )

    await passedAction(chat_id=chat_id, user_id=user_id, message_id=message_id)

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


from pyrogram.types import ChatPermissions
from Stella import StellaCli
from Stella.database.welcome_mongo import (AppendVerifiedUsers,
                                           DeleteUsercaptchaData, GetWelcome,
                                           isWelcome)
from Stella.helper.button_gen import button_markdown_parser


async def passedAction(chat_id: int, user_id: int, message_id: int):
    await StellaCli.restrict_chat_member(
        chat_id,
        user_id,
        ChatPermissions(
            can_send_messages=True,
            can_add_web_page_previews=True
        )
    )
        
    if isWelcome(chat_id):
        Content, Text, DataType = GetWelcome(chat_id)
        Text, buttons = button_markdown_parser(Text)
        reply_markup = None
        if len(buttons) > 0:
            reply_markup = InlineKeyboardMarkup(buttons)
    else:
        reply_markup = None

    # Edit the main chat
    await StellaCli.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=message_id,
        reply_markup=reply_markup
    )

    # Delete user's captcha data and append them into varified list
    DeleteUsercaptchaData(chat_id, user_id)
    AppendVerifiedUsers(chat_id, user_id)

async def failedAction(message, user_id: int, chat_id: int, message_id: int):
    await StellaCli.kick_chat_member(
                            chat_id=chat_id,
                            user_id=user_id
                        )
        
    await StellaCli.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=(
            f"User {message.from_user.mention} has failed the CAPTCHAs!"
        )
    )

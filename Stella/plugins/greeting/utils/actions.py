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

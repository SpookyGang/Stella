from Stella import StellaCli
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery
)
from pyrogram.types import ChatPermissions
from Stella.database.welcome_mongo import (
    GetCaptchaSettings, GetWelcome, isWelcome,
    isUserVerified
)

from Stella.helper.button_gen import button_markdown_parser


async def CaptchaButton(chat_id, user_id):
    
    captcha_mode, captcha_text, captcha_kick_time = GetCaptchaSettings(chat_id)
    
    CaptchaButton = (
        [
            [
                InlineKeyboardButton(text=captcha_text, callback_data=f'captcha_{user_id}')
            ]
        ]
    )
        
    return CaptchaButton
    
    
@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'captcha_' in query.data))
async def CaptchaCallback(client: StellaCli, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    chat_id = callback_query.message.chat.id 
    NewJoinUserID = int(callback_query.data.split('_')[1])

    if NewJoinUserID == user_id:

        if isWelcome(chat_id):
            Content, Text, DataType = GetWelcome(chat_id)
            Text, buttons = button_markdown_parser(Text)

            reply_markup = None
            if len(buttons) > 0:
                reply_markup = InlineKeyboardMarkup(buttons)
        else:
            reply_markup = None
        await callback_query.edit_message_reply_markup(
            reply_markup=reply_markup
        )
        await callback_query.answer("Thank for your time!", show_alert=False)
        await StellaCli.restrict_chat_member(
                chat_id,
                NewJoinUserID,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_stickers=True,
                    can_send_animations=True,
                    can_send_games=True,
                    can_use_inline_bots=True,
                    can_add_web_page_previews=True,
                    can_send_polls=True
                )
            )
    else:
        await callback_query.answer("This button isn't made for you!", show_alert=False)
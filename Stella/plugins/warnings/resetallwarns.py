import html

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)
from Stella import StellaCli
from Stella.database.warnings_mongo import reset_all_warns_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCreator


@StellaCli.on_message(custom_filter.command(commands=('resetallwarns')))
async def reset_all_warns(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title 

    if not await isUserCreator(message):
        await message.reply(
            f"You need to be the chat owner of {html.escape(chat_title)} to do this."
        )
        return
    
    buttons = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='Reset all warnings', callback_data='resetwarns_confirm')],
        [InlineKeyboardButton(text='Cancel', callback_data='resetwarns_cancel')]]
    )
    await message.reply(
        text=(
            f"Are you sure you would like to reset ALL warnings in {html.escape(chat_title)}? This action cannot be undone."
        ),
        reply_markup=buttons,
        quote=True
    )

@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'resetwarns_' in query.data))
async def resetwarns_callback(client: StellaCli, callback_query: CallbackQuery):

    query_data = callback_query.data.split('_')[1]  
    if not await isUserCreator(callback_query, chat_id=callback_query.message.chat.id, user_id=callback_query.from_user.id):
        await callback_query.answer(
            text='You\'re not owner of this chat.'
        )
        return

    if query_data == 'confirm':
        reset_all_warns_db(callback_query.message.chat.id)
        await callback_query.edit_message_text(
            text="Reset all chat warnings."
        )
    else:
        await callback_query.edit_message_text(
            text='Resetting of all warnings has been cancelled.'
        )

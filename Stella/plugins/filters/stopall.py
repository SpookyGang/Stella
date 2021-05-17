import html

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup)
from Stella import StellaCli
from Stella.database.filters_mongo import stop_all_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCreator


@StellaCli.on_message(custom_filter.command('stopall'))
async def stopall(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title 
    
    if message.chat.type == 'private':
        chat_title = 'local'
    if not await isUserCreator(message):
        await message.reply(
            'You\'re not creator of this chat.' 
        )
        return

    KEYBOARD = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='Delete all filters', callback_data='filters_stopall')],
        [InlineKeyboardButton(text='Cancel', callback_data='filters_cancel')]]
    )

    await message.reply(
        text=(
            f'Are you sure you would like to stop **ALL** filters in {html.escape(chat_title)}? This action cannot be undone.'
        ),
        reply_markup=KEYBOARD
    )


@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'filters_' in query.data))
async def stopall_callback(client: StellaCli, callback_query: CallbackQuery):
     
    chat_id = callback_query.message.chat.id 
    query_data = callback_query.data.split('_')[1]  
    
    if not await isUserCreator(callback_query, chat_id=callback_query.message.chat.id, user_id=callback_query.from_user.id):
        await callback_query.answer(
            text='You\'re not owner of this chat.'
        )
        return
    
    if query_data == 'stopall':
        stop_all_db(chat_id)
        await callback_query.edit_message_text(
            text='Deleted all chat filters.'
        )
    
    elif query_data == 'cancel':
        await callback_query.edit_message_text(
            text='Stopping of all filters has been cancelled.'
        )

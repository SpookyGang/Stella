from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message
)

from Stella import (
    StellaCli,
    GROUP_ANONYMOUS_BOT
)

from Stella.helper.chat_status import anon_admin_checker

from Stella.database.chats_settings_mongo import get_anon_setting

def anonadmin_checker(func):
    """Generates a verification button for the anon admin in the if /anonadmin is off

    Args:
        func ([type]): pass client: StellaCli, message: Message
    """
    async def wrap(client, message: Message):
        if not get_anon_setting(message.chat.id):
            message_id = message.message_id
            if message.sender_chat:
                sender_chat = message.sender_chat.id
                chat_id = message.chat.id
            else:
                sender_chat = message.from_user.id 
                chat_id = GROUP_ANONYMOUS_BOT

            if chat_id == sender_chat:
                button = [[InlineKeyboardButton(text='Click to prove admin', callback_data=f'anonAdminConfirm_')]]
                await message.reply(
                    text='It looks like you\'re anonymous. Tap this button to confirm your identity.',
                    reply_markup=InlineKeyboardMarkup(button)
                )
            else:
                await func(client, message)
        else:
            await func(client, message)
        
        @StellaCli.on_callback_query(filters.create(lambda _, __, query: 'anonAdminConfirm_' in query.data))
        async def anon_callback(client: StellaCli, callback_query: CallbackQuery):
            if await anon_admin_checker(callback_query.message.chat.id, callback_query.from_user.id):
                await func(client, message)
                await callback_query.message.delete()
            else:
                await callback_query.answer(
                    text="You are not admin to do that."
                )

    return wrap
from Stella import StellaCli, StellaAPI
from Stella.helper import custom_filter

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

@StellaCli.on_message(custom_filter.command(commands=('getapi')))
async def generate_api(client, message):
    if not (
        message.chat.type == 'private'
    ):
        await message.reply(
            "You can only get your API key in PM.",
            quote=True
        )
        return 
    
    button = InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='Generate Key', callback_data='api_generate')]]
    )

    await message.reply(
        "Tap the button to generate your API key.",
        reply_markup=button,
        quote=True
    )


@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'api_generate' in query.data))
async def generate_api_callback(client: StellaCli, callback_query: CallbackQuery):
    user_id = callback_query.from_user.id 
    first_name = callback_query.from_user.first_name 
    username = callback_query.from_user.username

    operation, api_key = StellaAPI.generate_api(user_id, first_name, username)
    if operation:
        text=(
            "Here is your **StellaGban** API key:\n\n"
            f"`{api_key}`"
        )
    else:
        text = 'Server is currently down, please try again later.'

    await callback_query.edit_message_text(
        text=text
    )

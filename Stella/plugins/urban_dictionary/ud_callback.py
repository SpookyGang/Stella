from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import CallbackQuery
from Stella import StellaCli
from Stella.plugins.urban_dictionary.get_data import getData


@StellaCli.on_callback_query(filters.create(lambda _, __, query: 'pagination_keyboard#' in query.data))
async def ud_callback(client: StellaCli, callback_query: CallbackQuery):
    
    message_id = callback_query.message.message_id
    chat_id = callback_query.message.chat.id 
    CurrentPage = int(callback_query.data.split('#')[1]) 
    GetWord = callback_query.data.split('#')[2]

    try:
        UDReasult, PageLen = await getData(chat_id, message_id, GetWord, CurrentPage)
    except TypeError:
        return

    keyboard = InlineKeyboard()
    keyboard.paginate(PageLen, CurrentPage, 'pagination_keyboard#{number}' + f'#{GetWord}')
    await StellaCli.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=UDReasult,
        reply_markup=keyboard
    )

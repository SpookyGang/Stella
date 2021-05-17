from pykeyboard import InlineKeyboard
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.plugins.urban_dictionary.get_data import getData


@StellaCli.on_message(custom_filter.command(commands=('ud')))
async def urbanDictionary(client, message):
    message_id = message.message_id 
    chat_id = message.chat.id 
    GetWord = ' '.join(message.command[1:])
    if not GetWord:
        message = await StellaCli.ask(
            message.chat.id,
            'Now give any word for query!'
        )
        GetWord = message.text
    
    CurrentPage = 1
    UDReasult, PageLen = await getData(chat_id, message_id, GetWord, CurrentPage)
    
    keyboard = InlineKeyboard()
    keyboard.paginate(PageLen, CurrentPage, 'pagination_keyboard#{number}' + f'#{GetWord}')
    await message.reply(
        text=f"{UDReasult}",
        reply_markup=keyboard
    )   

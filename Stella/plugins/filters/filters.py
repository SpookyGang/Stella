import html

from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.database.filters_mongo import get_filters_list

@StellaCli.on_message(custom_filter.command('filters'))
async def filters(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title 
    if message.chat.type == 'private':
        chat_title = 'local'
    FILTERS = get_filters_list(chat_id)
    
    if len(FILTERS) == 0:
        await message.reply(
            f'No filters in {html.escape(chat_title)}.'
        )
        return

    filters_list = f'List of filters in {html.escape(chat_title)}:\n'
    
    for filter_ in FILTERS:
        filters_list += f'- `{filter_}`\n'
    
    await message.reply(
        filters_list
    )
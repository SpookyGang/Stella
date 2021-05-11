from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.database.filters_mongo import (
    stop_db,
    get_filters_list
)

@StellaCli.on_message(custom_filter.command('stop'))
async def stop(client, message):

    chat_id = message.chat.id

    if not await isUserAdmin(message):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            'Not enough arguments provided.'
        )
        return
    
    filter_name = message.command[1]
    if (
        filter_name not in get_filters_list(chat_id)
    ):
        await message.reply(
            'You haven\'t saved any filters on this word yet!'
        )
        return
    
    stop_db(chat_id, filter_name)
    await message.reply(
        f'Stopped `{filter_name}`.'
    )

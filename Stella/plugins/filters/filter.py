from Stella import StellaCli
from Stella.database.filters_mongo import add_filter_db
from Stella.helper import custom_filter
from Stella.helper.filters_helper.get_filters_message import GetFIlterMessage
from Stella.helper.get_data import get_text_reason


@StellaCli.on_message(custom_filter.command(commands=('filter')))
async def filter(client, message):
    
    chat_id = message.chat.id 
    if (
        message.reply_to_message
        and not len(message.command) == 2
    ):
        await message.reply(
            "You need to give the filter a name!"
        )  
        return 
    
    filter_name, filter_reason = get_text_reason(message)
    if (
        message.reply_to_message
        and not len(message.command) >=2
    ):
        await message.reply(
            "You need to give the filter some content!"
        )
        return

    content, text, data_type = await GetFIlterMessage(message)
    add_filter_db(chat_id, filter_name=filter_name, content=content, text=text, data_type=data_type)
    await message.reply(
        f"Saved filter '`{filter_name}`'."
    )

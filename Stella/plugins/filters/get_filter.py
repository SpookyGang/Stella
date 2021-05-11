import re

from pyrogram import filters

from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.filters_helper.send_filter_message import SendFilterMessage
from Stella.database.filters_mongo import (
    get_filters_list,
    get_filter
)

@StellaCli.on_message(filters.all & filters.group, group=8)
async def FilterCheckker(client, message):
    
    if not message.text:
        return
    text = message.text
    chat_id = message.chat.id

    # If 'chat_id' has no filters then simply return  
    if (
        len(get_filters_list(chat_id)) == 0
    ):
        return

    ALL_FILTERS = get_filters_list(chat_id)
    for filter_ in ALL_FILTERS:
        
        if (
            message.command
            and message.command[0] == 'filter'
            and len(message.command) >= 2
            and message.command[1] ==  filter_
        ):
            return
            
        pattern = r"( |^|[^\w])" + re.escape(filter_) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            filter_name, content, text, data_type = get_filter(chat_id, filter_)
            await SendFilterMessage(
                message=message,
                filter_name=filter_,
                content=content,
                text=text,
                data_type=data_type
            )

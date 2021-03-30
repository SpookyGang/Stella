import html 
from Stella import StellaCli
from Stella.helper import custom_filter

@StellaCli.on_message(custom_filter.command(commands=('filter')))
async def filter(client, message):
    message_id = message.message_id
    chat_id = message.chat.id 
    chat_title = html.escape(message.chat.title) 
    print(message)
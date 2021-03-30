import html
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.get_data import GetChat
from Stella.plugins.connection.connection import connection
from Stella.database.connection_mongo import reconnectChat, GetConnectedChat

@StellaCli.on_message(custom_filter.command(commands=('reconnect')))
async def reconnectC(client, message):
    user_id = message.from_user.id 
    if not (
        message.chat.type == 'private'
    ):
        await message.reply(
            "You need to be in pm to use this."
        )
        return
    if GetConnectedChat(user_id) is not None:
        chat_id = GetConnectedChat(user_id)
        chat_title = await GetChat(chat_id)
        chat_title = html.escape(chat_title)
        if await connection(message) is not None:
            reconnectChat(user_id)
            await message.reply(
                f"You are now reconnected to {chat_title}.",
                quote=True
            )
        
            
    else:
        await message.reply(
            "You haven't made a connection to any chats yet.",
            quote=True
        )

    
    
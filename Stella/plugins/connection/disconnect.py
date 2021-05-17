from Stella import StellaCli
from Stella.database.connection_mongo import disconnectChat
from Stella.helper import custom_filter
from Stella.plugins.connection.connection import connection


@StellaCli.on_message(custom_filter.command(commands=('disconnect')))
async def diconnectChat(client, message):
    user_id = message.from_user.id 
    if not (
        message.chat.type == 'private'
    ):
        await message.reply(
            "You need to be in pm to use this."
        )
        return
    if await connection(message) is not None:
        disconnectChat(user_id)
        await message.reply(
            "Disconnected from chat.",
            quote=True
        )
    else:
        await message.reply(
            "You aren't connected to any chats! Anything you save here is for your eyes only :)",
            quote=True
        )

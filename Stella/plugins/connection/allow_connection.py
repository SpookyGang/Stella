from Stella import StellaCli
from Stella.database.connection_mongo import (allow_collection,
                                              get_allow_connection)
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import isUserAdmin
from Stella.plugins.connection.connection import connection

ALLOW_CONNECTION_TRUE = ['on', 'yes' ,'true']
ALLOW_CONNECTION_FALSE = ['off', 'no' ,'false']

@StellaCli.on_message(custom_filter.command(commands=('allowconnection')))
@anonadmin_checker
async def allow_connection(client, message):
    
    if await connection(message) is not None:
        chat_id = connection(message)
        chat_title = None
    else:
        chat_id = message.chat.id 
        chat_title = message.chat.title 

    if not await isUserAdmin(message):
        return 

    if (
        len(message.command) >= 2
    ):
        get_arg = message.command[1]

        if (
            get_arg in ALLOW_CONNECTION_TRUE
        ):
            allow_collection(chat_id, chat_title, allow_collection=True)
            await message.reply(
                "Allow all user in connection.",
                quote=True
            )
        elif (
            get_arg in ALLOW_CONNECTION_FALSE
        ):
            allow_collection(chat_id, chat_title, allow_collection=False)
            await message.reply(
                "Disallow all user in connection.",
                quote=True
            )
        else:
            await message.reply(
                f"I got {get_arg} arg!"
            )
    else:
        if get_allow_connection(chat_id):
            t_message = (
                "users are allowed to connect chat in PM"
            )
        else:
            t_message = (
                "users are not allowed to connect chat in PM"
            )
        
        await message.reply(
            t_message,
            quote=True
        )
    
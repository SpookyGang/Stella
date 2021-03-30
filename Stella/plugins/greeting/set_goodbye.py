from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import (
    isUserCan
    )
from Stella.helper.anon_admin import anonadmin_checker

from Stella.database.welcome_mongo import SetGoodBye
from Stella.helper.welcome_helper.get_welcome_message import GetWelcomeMessage

from Stella.plugins.connection.connection import connection

@StellaCli.on_message(custom_filter.command(commands=('setgoodbye')))
@anonadmin_checker
async def set_goodbye(client, message):

    if await connection(message) is not None:
        ChatID = await connection(message)
    else:
        ChatID = message.chat.id

    if not await isUserCan(message, permissions='can_change_info'):
        return

    if (
        not message.reply_to_message
        and not len(message.command) > 1
    ):
        await message.reply(
            "You need to give the goodbye message some content!"
        )  
        return

    CONTENT, TEXT, DATATYPE = GetWelcomeMessage(message)

    SetGoodBye(
        ChatID,
        CONTENT,
        TEXT,
        DATATYPE
    )

    await message.reply(
        "The new goodbye message has been saved!",
        quote=True
    )

    
    
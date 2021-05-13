from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import (
    isUserCan
    )
from Stella.helper.anon_admin import anonadmin_checker

from Stella.database.welcome_mongo import SetWelcome
from Stella.helper.welcome_helper.get_welcome_message import GetWelcomeMessage

from Stella.plugins.connection.connection import connection

@StellaCli.on_message(custom_filter.command(commands=('setwelcome')))
@anonadmin_checker
async def set_welcome(client, message):

    if await connection(message) is not None:
        ChatID = await connection(message)
    else:
        ChatID = message.chat.id

        if message.chat.type == 'private':
            await message.reply(
                "This command is only made for grup, not for PM."
            )
            return

    if not await isUserCan(message, permissions='can_change_info'):
        return

    if (
        not message.reply_to_message
        and not len(message.command) > 1
    ):
        await message.reply(
            "You need to give the welcome message some content!"
        )  
        return

    CONTENT, TEXT, DATATYPE = GetWelcomeMessage(message)
    print(CONTENT, TEXT, DATATYPE)
    SetWelcome(
        ChatID,
        CONTENT,
        TEXT,
        DATATYPE
    )

    await message.reply(
        "The new welcome message has been saved!",
        quote=True
    )

    
    
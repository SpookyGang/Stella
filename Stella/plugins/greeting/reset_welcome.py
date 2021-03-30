from pyrogram.methods import password
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import (
    isUserCan
    )
from Stella.helper.anon_admin import anonadmin_checker

from Stella.database.welcome_mongo import UnSetWelcome

from Stella.plugins.connection.connection import connection

@StellaCli.on_message(custom_filter.command(commands=('resetwelcome')))
@anonadmin_checker
async def ResetWelcome(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not await isUserCan(message, permissions='can_change_info'):
        return

    UnSetWelcome(chat_id)

    await message.reply(
        "The welcome message has been reset to default!",
        quote=True
    )


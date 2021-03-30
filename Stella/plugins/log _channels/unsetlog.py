from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCan
from Stella.plugins.connection.connection import connection
from Stella.database.log_channels_mongo import unset_log_db
from Stella.helper.anon_admin import anonadmin_checker

@StellaCli.on_message(custom_filter.command(commands=('unsetlog')))
@anonadmin_checker
async def unset_log(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id
    
    if not await isUserCan(message, permissions='can_change_info'):
        return

    unset_log_db(chat_id)

    await message.reply(
        "Successfully unset log channel. Admin actions will no longer be logged.",
        quote=True
    )
    

import html
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.helper.anon_admin import anonadmin_checker

from Stella.plugins.connection.connection import connection
from Stella.database.log_channels_mongo import get_set_channel

@StellaCli.on_message(custom_filter.command(commands=('logchannel')))
@anonadmin_checker
async def logcategories(client, message):
    
    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id 

    if not await isUserAdmin(message):
        return 
    
    if get_set_channel(chat_id) is not None:
        channel_title = get_set_channel(chat_id)
        await message.reply(
            f"I am currently logging admin actions in '{html.escape(channel_title)}'.",
            quote=True
        )
    else:
        await message.reply(
            "There are no log channels assigned to this chat.",
            quote=True
        )


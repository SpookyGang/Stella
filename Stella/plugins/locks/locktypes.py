from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.helper.disable import disable

from . import lock_map

@StellaCli.on_message(custom_filter.command(commands='locktypes', disable=True))
@disable
async def locktypes(client, message):
    
    LOCKS_LIST = lock_map.LocksMap.list()

    text = "The available locktypes are:\n"
    for lock in LOCKS_LIST:
        text += f"- {lock}\n"
    
    await message.reply(
        text,
        quote=True
    )
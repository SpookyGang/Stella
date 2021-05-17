from Stella import StellaCli
from Stella.database.locks_mongo import get_locks
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin

from . import lock_map


@StellaCli.on_message(custom_filter.command(commands=('locks')))
async def locks(client, message):

    chat_id = message.chat.id

    if not await isUserAdmin(message):
        return
    
    LOCKS_LIST = get_locks(chat_id)

    if (
        len(LOCKS_LIST) == 0
    ):
        await message.reply(
            "No items locked in this chat."
        )
        return
        
    if 1 in LOCKS_LIST:
        await message.reply(
            "Jokes on you, everything's locked."
        )
        return
        
    text = "These are the currently locked items:\n"
    for item in LOCKS_LIST:
        lock_name = lock_map.LocksMap(item).name
        text += f'- `{lock_name}`\n'
    
    await message.reply(
        text
    )

from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.get_user import get_user_id
from Stella.helper.chat_status import isUserAdmin

from Stella.database.warnings_mongo import (
    reset_user_warns,
    count_user_warn
)

@StellaCli.on_message(custom_filter.command(commands=('resetwarn')))
async def reset_warn(client, message):
    chat_id = message.chat.id 

    if not await isUserAdmin(message):
        return

    user_info = await get_user_id(message)
    user_id = user_info.id 
    warn_num = count_user_warn(chat_id, user_id)

    print(warn_num)
    
    if warn_num is None:
        await message.reply(
            f"User {user_info.mention} has no warnings to delete!"
        )
        return

    reset_user_warns(chat_id, user_id)
    await message.reply(
        f"User {user_info.mention} has had all their previous warns removed."
    )
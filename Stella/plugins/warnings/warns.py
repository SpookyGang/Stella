from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.get_user import get_user_id
from Stella.helper.chat_status import isUserAdmin

from Stella.database.warnings_mongo import (
    get_all_warn_reason,
    warn_limit,
    count_user_warn
)

@StellaCli.on_message(custom_filter.command(commands=('warns')))
async def warns(client, message):

    chat_id = message.chat.id 
    if not await isUserAdmin(message):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id 

    user_warn_num = count_user_warn(chat_id, user_id)
    if user_warn_num is None:
        await message.reply(
            f"User {user_info.mention} has no warnings!"
        )
        return
    
    chat_warn_limit = warn_limit(chat_id)
    REASONS = get_all_warn_reason(chat_id, user_id)

    await message.reply(
        f"User {user_info.mention} has {user_warn_num}/{chat_warn_limit} warnings. Reasons are:\n{''.join(REASONS)}"
    )
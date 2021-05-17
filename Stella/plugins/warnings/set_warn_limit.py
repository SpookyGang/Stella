import html

from Stella import StellaCli
from Stella.database.warnings_mongo import set_warn_limit_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCan


@StellaCli.on_message(custom_filter.command(commands=('setwarnlimit')))
async def setWarnLimit(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "Please specify how many warns a user should be allowed to receive before being acted upon.",
            quote=True
        )
        return
    
    warn_limit_arg = message.command[1]
    if not warn_limit_arg.isdigit():
        await message.reply(
            f"{warn_limit_arg} is not a valid integer.",
            quote=True
        )
        return
    
    if int(warn_limit_arg) > 50:
        await message.reply(
            "The maximum warning limit is 50.",
            quote=True
        )
        return
    
    if int(warn_limit_arg) == 0:
        await message.reply(
            "The warning limit has to be set to a number bigger than 0.",
            quote=True
        )
        return
    
    set_warn_limit_db(chat_id, int(warn_limit_arg))
    await message.reply(
        f"Warn limit settings for {html.escape(chat_title)} has been updated to {warn_limit_arg}.",
        quote=True
    )

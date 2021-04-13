import html

from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs

from Stella.database.antiflood_mongo import setflood_db

@StellaCli.on_message(custom_filter.command(commands=('setflood')))
async def setflood(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title

    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            'I expected some arguments! Either off, or an integer. eg: `/setflood 5`, or `/setflood off`'
        )
        return
    
    arg = message.command[1]

    if (
        arg == 'off'
        or (
            arg.isdigit()
            and int(arg) == 0
        )
    ):
        setflood_db(chat_id, False)
        await message.reply(
            "Antiflood has been disabled."
        )
        return
    
    elif (
        arg.isdigit()
    ):
        if int(arg) > 100:
            await message.reply(
                "The flood limit is 100. You can set a value between 0 and 100."
            )
        else:
            setflood_db(chat_id, int(arg))
            await message.reply(
                f"Antiflood settings for {html.escape(chat_title)} have been updated to {arg}."
            )
    else:
        await message.reply(
            f"{arg} is not a valid integer."
        )
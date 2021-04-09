from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import (
    check_user,
    check_bot
)

from Stella.database.disable_mongo import disabledel_db

DISABLEDEL_TRUE = ['on', 'yes']
DISABLEDEL_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('disabledel')))
async def disabledel(client, message):

    chat_id = message.chat.id

    if not await check_bot(message, permissions='can_delete_messages'):
        return

    if not await check_user(message, permissions='can_change_info'):
        return
    
    if (
        len(message.command) >= 2
    ):
        arg = message.command[1]
        if (
            arg in DISABLEDEL_TRUE
        ):
            disabledel_db(chat_id, True)
            await message.reply(
                "Disabled messages will now be deleted."
            )
        
        elif (
            arg in DISABLEDEL_FALSE
        ):
            disabledel_db(chat_id, False)
            await message.reply(
                "Disabled messages will no longer be deleted."
            )
        
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )
    else:
        await message.reply(
            "You need to give me a setting; yes/no/on/off"
        )
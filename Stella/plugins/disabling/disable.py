from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.custom_filter import DISABLE_COMMANDS
from Stella.helper.chat_status import check_user

from Stella.database.disable_mongo import disable_db

@StellaCli.on_message(custom_filter.command(commands=('disable')))
async def disable(client, message):
    chat_id = message.chat.id 

    if not await check_user(message, permissions='can_change_info'):
        return

    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You haven't specified a command to disable."
            )
        return
    
    disable_args = message.command[1:]

    DISABLE_ITMES = []
    INCORRECT_ITEMS = []
    
    for disable_arg in disable_args:
        if (
            disable_arg not in DISABLE_COMMANDS
        ):
            INCORRECT_ITEMS.append(disable_arg)
        else:
            DISABLE_ITMES.append(disable_arg)

    if (
        len(INCORRECT_ITEMS) != 0
    ):
        text = (
            "Unknown command to disable:\n"
        )
        for item in INCORRECT_ITEMS:
            text += f'- `{item}`\n'
        text += "Check /disableable!"
        await message.reply(
                text
            )
        return
            
    for items in DISABLE_ITMES:
        disable_db(chat_id, items)

    text = 'Disabled:\n'
    for disable_arg in DISABLE_ITMES:
        if len(DISABLE_ITMES) != 1:
            text += f'- `{disable_arg}`\n'
        else:
            text = (
                f"Disable `{disable_arg}`."
            )
    
    await message.reply(
        text
    )
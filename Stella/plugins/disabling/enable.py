from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.custom_filter import DISABLE_COMMANDS
from Stella.helper.chat_status import check_user

from Stella.database.disable_mongo import enable_db

@StellaCli.on_message(custom_filter.command(commands=('enable')))
async def enable(client, message):
    chat_id = message.chat.id 

    if not await check_user(message, permissions='can_change_info'):
        return

    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You haven't specified a command to enable."
        )
        return
    
    enable_args = message.command[1:]

    ENABLE_ITMES = []
    for enable_arg in enable_args:
        if (
            enable_arg not in DISABLE_COMMANDS
        ):
            await message.reply(
                (
                    f"Unknown command to reenable:\n- {enable_arg}\n"
                    "Check /disableable!"
                )
            )
            return
        else:
            ENABLE_ITMES.append(enable_arg)

    for items in ENABLE_ITMES:
        enable_db(chat_id, items)

    text = 'Enabled:\n'
    for enable_arg in ENABLE_ITMES:
        if len(ENABLE_ITMES) != 1:
            text += f'- `{enable_arg}`\n'
        else:
            text = (
                f"Enabled `{enable_arg}`."
            )

    await message.reply(
        text
    )
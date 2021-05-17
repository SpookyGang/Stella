from Stella import StellaCli
from Stella.database.disable_mongo import get_disabled
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin


@StellaCli.on_message(custom_filter.command(commands=('disabled')))
async def disable(client, message):

    chat_id = message.chat.id 

    if not await isUserAdmin(message):
        return
    
    DISABLE_LIST = get_disabled(chat_id)

    if (
        len(DISABLE_LIST) == 0
    ):
        await message.reply(
            "There are no disabled commands in this chat."
        )
        return
    
    text = "The following commands are disabled in this chat:\n"
    for item in DISABLE_LIST:
        text += f'- `{item}`\n'
    
    await message.reply(
        text
    )

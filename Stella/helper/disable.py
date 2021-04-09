from Stella.helper.custom_filter import DISABLE_COMMANDS
from Stella.helper.chat_status import isBotCan

from Stella.database.disable_mongo import (
    get_disabled,
    get_disabledel
)


def disable(func):

    async def wrapper(client, message):
        if not message.command:
            return
        chat_id = message.chat.id
        command = message.command[0]
        DISABLED_LIST = get_disabled(chat_id)
        if command in DISABLED_LIST:
            if get_disabledel(chat_id):
                if not await isBotCan(message, permissions='can_delete_messages'):
                    return
                await message.delete()
                return
            else:
                return
        else:
            await func(client, message)
    
    return wrapper
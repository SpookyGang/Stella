from Stella.database.disable_mongo import get_disabled, get_disabledel
from Stella.helper.chat_status import isBotCan, isUserAdmin
from Stella.helper.custom_filter import DISABLE_COMMANDS


def disable(func):

    async def wrapper(client, message):
        if not message.command:
            return
        if not await isUserAdmin(message, silent=True):
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
        else:
            await func(client, message)
    
    return wrapper

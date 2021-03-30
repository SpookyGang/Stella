from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCan, isBotCan

from Stella.database.blocklists_mongo import blocklistMessageDelete, getblocklistMessageDelete

BLOCKLIST_DELETE_TRUE = ['on', 'yes']
BLOCKLIST_DELETE_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands='blocklistdelete'))
async def blocklistdelete(client, message):

    chat_id = message.chat.id 

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if not await isBotCan(message, permissions='can_delete_messages'):
        return

    if (
        len(message.command) >= 2 
    ):
        args = message.command[1]

        if (
            args in BLOCKLIST_DELETE_TRUE
        ):
            blocklistMessageDelete(chat_id, True)
            await message.reply(
                "Blocklist deletes have been **enabled**. I will now delete all blocklisted messages."
            )
        
        elif (
            args in BLOCKLIST_DELETE_FALSE
        ):
            blocklistMessageDelete(chat_id, False)
            await message.reply(
                "Blocklist deletes have been **disabled**. I will no longer delete any blocklisted messages. However, I will still apply actions; such as warnings, or bans."
            )
        
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )
    else:
        if getblocklistMessageDelete:
            await message.reply(
                "I am currently deleting all blocklisted messages."
            )
        else:
            await message.reply(
                "I am currently **not** deleting blocklisted messages."
            )

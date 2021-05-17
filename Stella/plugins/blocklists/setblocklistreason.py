from Stella import StellaCli
from Stella.database.blocklists_mongo import (getblocklistmode,
                                              setblocklistreason_db)
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCan


@StellaCli.on_message(custom_filter.command(commands=('setblocklistreason')))
async def setblocklistreason(client, message):
    
    chat_id = message.chat.id 

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    blocklist_mode, blocklist_time, blocklist_default_reason = getblocklistmode(chat_id)
    
    if (
        len(message.command) >= 2
    ):
        set_reason = message.text.markdown[len(message.command[0]) + 2 :]
        setblocklistreason_db(chat_id, set_reason)
        await message.reply(
            f"The default blocklist reason has been set to:\n{set_reason}"
        )
    else:
        if blocklist_default_reason is None:
            await message.reply(
                (
                    "No default blocklist message has been set. I will reply with:\n"
                    "Automated blocklist action, due to a match on: TriggeredFilter"
                )
            )
        else:
            await message.reply(
                f"The current blocklist reason is: \n{blocklist_default_reason}"
            )

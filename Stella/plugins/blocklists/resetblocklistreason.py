from Stella import StellaCli
from Stella.database.blocklists_mongo import setblocklistreason_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCan


@StellaCli.on_message(custom_filter.command(commands=('resetblocklistreason')))
async def resetblocklistreason(client, message):
    
    chat_id = message.chat.id 

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    setblocklistreason_db(chat_id, None)
    await message.reply(
        "The default blocklist reason has been reset."
    )

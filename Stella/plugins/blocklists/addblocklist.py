from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs
from Stella.helper.get_data import get_text_reason

from Stella.database.blocklists_mongo import add_blocklist_db

@StellaCli.on_message(custom_filter.command(commands=['addblocklist', 'addblacklist']))
async def add_blocklist(client, message):

    chat_id = message.chat.id 
    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            (
                "You need to provide a blocklist trigger and reason!\n"
                "eg: `/addblocklist \"the admins suck\" Respect your admins!`"
            )
        )
        return
    
    text, reason = get_text_reason(message)
    add_blocklist_db(chat_id, text, reason)
    await message.reply(
        f"Added blocklist filter '`{text}`'!",
        quote=True
    )


    

    
        
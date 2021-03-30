import html

from Stella import StellaCli

from Stella.helper import custom_filter 
from Stella.helper.chat_status import isUserCan
from Stella.helper.anon_admin import anonadmin_checker

from Stella.database.rules_mongo import set_rules_db

@StellaCli.on_message(custom_filter.command(commands=('resetrules')))
@anonadmin_checker
async def reset_rules(client, message):
    
    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    set_rules_db(chat_id, None)
    
    await message.reply(
        f"Rules for {html.escape(chat_title)} were successfully cleared!"
    )
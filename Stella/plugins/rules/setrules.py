import html

from Stella import StellaCli
from Stella.database.rules_mongo import get_rules, set_rules_db
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import isUserCan


@StellaCli.on_message(custom_filter.command(commands=('setrules')))
@anonadmin_checker
async def set_rules(client, message):
    
    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You need to give me rules to set!",
            quote=True
        )
        return
    
    get_rules = message.text.markdown[len(message.command[0]) + 2 :]
    set_rules_db(chat_id, get_rules)
    await message.reply(
        f"New rules for {html.escape(chat_title)} set successfully!",
        quote=True
    )

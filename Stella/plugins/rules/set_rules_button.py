import html

from Stella import StellaCli

from Stella.helper import custom_filter 
from Stella.helper.chat_status import isUserCan

from Stella.database.rules_mongo import set_rule_button, get_rules_button
from Stella.helper.anon_admin import anonadmin_checker

@StellaCli.on_message(custom_filter.command(commands=('setrulesbutton')))
@anonadmin_checker
async def set_rules(client, message):
    
    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        current_rules_button = get_rules_button(chat_id)
        await message.reply(
            (
                f"The rules button will be called:\n `{current_rules_button}`\n\n"
                "To change the button name, try this command again followed by the new name"
            ),
            quote=True
        )
        return
    
    rules_button = ' '.join(message.text.markdown[1:])

    set_rule_button(chat_id, rules_button)
    await message.reply(
        "Updated the rules button name!",
        quote=True
    )
import html

from Stella import StellaCli

from Stella.helper import custom_filter 
from Stella.helper.chat_status import isUserCan
from Stella.helper.anon_admin import anonadmin_checker

from Stella.database.rules_mongo import set_private_rule, get_private_note

PRIVATE_RULES_TRUE = ['yes', 'on']
PRIVATE_RULES_FALSE = ['no', 'off']

@StellaCli.on_message(custom_filter.command(commands=('privaterules')))
@anonadmin_checker
async def private_rules(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if (
        len(message.command) >= 2
    ):
        args = message.command[1]

        if (
            args in PRIVATE_RULES_TRUE
        ):
            set_private_rule(chat_id, True)
            await message.reply(
                "Use of /rules will send the rules to the user's PM.",
                quote=True
            )

        elif (
            args in PRIVATE_RULES_FALSE
        ):
            set_private_rule(chat_id, False)
            await message.reply(
                f"All /rules commands will send the rules to {html.escape(chat_title)}.",
                quote=True
            )

        else:
            await message.reply(
                "I only understand the following: yes/no/on/off",
                quote=True
            )
    else:
        if get_private_note(chat_id):
            await message.reply(
                "Use of /rules will send the rules to the user's PM."
            )
        else:
            await message.reply(
                f"All /rules commands will send the rules to UPDATED! {html.escape(chat_title)}."
            )
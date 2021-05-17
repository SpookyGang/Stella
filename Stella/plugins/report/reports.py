from Stella import StellaCli
from Stella.database.report_mongo import get_report, reports_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin, isUserCan

REPORTS_TRUE = ['yes', 'on']
REPORTS_FALSE = ['no', 'off']

@StellaCli.on_message(custom_filter.command(commands=('reports')))
async def reports(client, message):

    chat_id = message.chat.id

    if not await isUserAdmin(message):
        return
        
    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if (
        len(message.command) >= 2
    ):
        report_args = message.command[1]

        if (
            report_args in REPORTS_TRUE
        ):
            reports_db(chat_id, True)
            await message.reply(
                "Users will now be able to report messages."
            )
        
        elif (
            report_args in REPORTS_FALSE
        ):
            reports_db(chat_id, False)
            await message.reply(
                "Users will no longer be able to report via @admin or /report."
            )
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )
    else:
        if get_report(chat_id):
            text = (
                "Reports are currently enabled in this chat.\n"
                "Users can use the /report command, or mention @admin, to tag all admins.\n\n"
            )
        else:
            text = "Reports are currently disabled in this chat.\n\n"
        
        await message.reply(
            f"{text} To change this setting, try this command again, with one of the following args: yes/no/on/off"
        )

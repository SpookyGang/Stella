from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin

@StellaCli.on_message(custom_filter.command(commands=('logcategories')))
async def logcategories(client, message):
    
    if not await isUserAdmin(message):
        return 
    
    await message.reply(
        (
            "The following log categories are supported:\n"
            "- `settings`: Bot settings which can be toggled or edited - such as blacklists, welcomes, rules, etc.\n"
            "- `admin`: Admin actions - such as bans, mutes, kicks, and warns.\n"
            "- `user`: User actions - such as kickme, or joining/leaving.\n"
            "- `automated`: Automated admin actions taken after locks, blacklists, or antiflood have been triggered\n"
            "- `reports`: Reports from users - through @admin, or /report.\n"
            "- `other`: Logs regarding extra features, such as notes and filters.\n\n"
            "Enable or disable them to change what data is logged in your logchannel."
        )
    )
    


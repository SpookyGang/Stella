from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs
from Stella.database.welcome_mongo import (
    SetCleanService,
    GetCleanService
)
from Stella.plugins.connection.connection import connection
from Stella.helper.anon_admin import anonadmin_checker

CLEAN_SERVICE_TRUE = ['on', 'yes']
CLEAN_SERVICE_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('cleanservice')))
@anonadmin_checker
async def CleanService(client, message):
    
    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not (
        await  CheckAllAdminsStuffs(message, permissions='can_delete_messages')
    ):
        return 

    if (
        len(message.command) >= 2
    ):
        get_clean_service = message.command[1]

        if (
            get_clean_service in CLEAN_SERVICE_TRUE
        ):
            clean_service = True
            SetCleanService(chat_id, clean_service)
            await message.reply(
                "I'll be deleting all service messages from now on!",
                quote=True
            )

        elif (
            get_clean_service in CLEAN_SERVICE_FALSE
        ):
            clean_service = False 
            SetCleanService(chat_id, clean_service)
            await message.reply(
                "I'll leave service messages.",
                quote=True
            )
        
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off",
                quote=True
            )
    elif (
        len(message.command) == 1
    ):
        if GetCleanService(chat_id):
            CleanServiceis = "I am currently deleting service messages when new members join or leave."

        else:
            CleanServiceis = "I am not currently deleting service messages when members join or leave."
        
        await message.reply(
            (
                f'{CleanServiceis}\n\n'
                "To change this setting, try this command again followed by one of yes/no/on/off"
            ),
            quote=True
        )
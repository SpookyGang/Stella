from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import (
    CheckAdmins
    )
from Stella.database.welcome_mongo import (
    SetCleanWelcome,
    GetCleanWelcome
)
from Stella.plugins.connection.connection import connection
from Stella.helper.anon_admin import anonadmin_checker

CLEAN_WELCOME_TRUE = ['on', 'yes']
CLEAN_WELCOME_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('cleanwelcome')))
@anonadmin_checker
async def CleanWelcome(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not await  CheckAdmins(message):
        return 
    
    if (
        len(message.command) >= 2
    ):
        get_args = message.command[1]
        if (
            get_args in CLEAN_WELCOME_TRUE
        ):
            clean_welcome = True 
            SetCleanWelcome(chat_id, clean_welcome)
            await message.reply(
                "I'll be deleting all old welcome/goodbye messages from now on!",
                quote=True
            )
        
        elif (
            get_args in CLEAN_WELCOME_FALSE
        ):
            clean_welcome = False
            SetCleanWelcome(chat_id, clean_welcome)
            await message.reply(
                "I'll leave old welcome/goodbye messages.",
                quote=True
            )
    elif (
        len(message.command) == 1
    ):
        if (
            GetCleanWelcome(chat_id)
        ):
            CleanMessage = "I am currently deleting old welcome messages when new members join."
        else:
            CleanMessage = "I am not currently deleting old welcome messages when new members join."
        
        await message.reply(
            (
                f'{CleanMessage}\n\n'
                "To change this setting, try this command again followed by one of yes/no/on/off"
            ),
            quote=True
        )
import html

from Stella import StellaCli
from Stella.database.chats_settings_mongo import anonadmin_db, get_anon_setting
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserCreator

ANONADMIN_TRUE = ['yes', 'on']
ANONADMIN_FALSE = ['no', 'off']

@StellaCli.on_message(custom_filter.command(commands=('anonadmin')))
async def anon_admin(client, message):
    
    chat_id = message.chat.id 
    chat_title = message.chat.title 

    if not await isUserCreator(message):
        await message.reply(
            "Only the group creator can use this command"
        )
        return
    
    if len(message.command) >= 2:
        args = message.command[1]

        if (
            args in ANONADMIN_TRUE
        ):  
            anonadmin_db(chat_id, True)
            await message.reply(
                f"The anon admin setting for {html.escape(chat_title)} has been updated to true."
            )
        elif (
            args in ANONADMIN_FALSE
        ):
            anonadmin_db(chat_id, False)
            await message.reply(
                f"The anon admin setting for {html.escape(chat_title)} has been updated to false."
            )
        else:
            await message.reply(
                f"failed to get boolean from input: expected one of y/yes/on or n/no/off; got: {args}"
            )
    
    else:
        if get_anon_setting(chat_id):
            await message.reply(
                f"{html.escape(chat_title)} currently allows all anonymous admins to use any admin command without restriction."
            )
        else:
            await message.reply(
                f"{html.escape(chat_title)} currently requires anonymous admins to press a button to confirm their permissions."
            )

from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import (
    CheckAdmins
    )
from Stella.database.welcome_mongo import (
    SetCaptcha,
    isGetCaptcha
)
from Stella.plugins.connection.connection import connection

CAPTCHA_WELCOME_TRUE = ['on', 'yes']
CAPTCHA_WELCOME_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('captcha')))
async def Captcha(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not await  CheckAdmins(message):
        await message.reply(
            "I need to be admin with the right to restrict to enable CAPTCHAs.",
            quote=True
        )
        return 

    if (
        len(message.command) >= 2
    ):
        get_args = message.command[1]

        if (
            get_args in CAPTCHA_WELCOME_TRUE
        ):
            captcha = True 
            SetCaptcha(chat_id, captcha)
            await message.reply(
                "CAPTCHAs have been enabled. I will now mute people when they join.",
                quote=True
            )
        
        elif (
            get_args in CAPTCHA_WELCOME_FALSE
        ):
            captcha = False 
            SetCaptcha(chat_id, captcha)
            await message.reply(
                "CAPTCHAs have been disabled. Users can join normally.",
                quote=True
            )

    elif (
        len(message.command) == 1
    ):
        if (
            isGetCaptcha(chat_id)
        ):
            CaptchaSetting = "Users will be asked to complete a CAPTCHA before being allowed to speak in the chat."
        else:
            CaptchaSetting = "Users will NOT be muted when joining the chat."
        
        await message.reply(
            (
                f"{CaptchaSetting}\n\n"
                "To change this setting, try this command again followed by one of yes/no/on/off"
            ),
            quote=True
        )  
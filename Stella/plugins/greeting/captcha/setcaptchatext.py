from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import (
    isUserCan, isBotAdmin
    )
from Stella.helper.anon_admin import anonadmin_checker

from Stella.database.welcome_mongo import (
    SetCaptchaText,
    GetCaptchaSettings
)

from Stella.plugins.connection.connection import connection


@StellaCli.on_message(custom_filter.command(commands=('setcaptchatext')))
@anonadmin_checker
async def SetCaptchatext(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id 

    if not await isUserCan(message, permissions='can_change_info'):
        return

    if not await  isBotAdmin(message):
        await message.reply(
            "I need to be admin with the right to restrict to enable CAPTCHAs.",
            quote=True
        )
        return 
    
    CaptchaText = ' '.join(message.text.split()[1:])
    if CaptchaText:
        SetCaptchaText(chat_id, CaptchaText)
        await message.reply(
            "Updated the CAPTCHA button text!",
            quote=True
        )
    else:
        captcha_mode, captcha_text, captcha_kick_time = GetCaptchaSettings(chat_id)
        
        await message.reply(
            (
                "Users will be welcomed with a button containing the following:\n"
                f"`{captcha_text}`\n\n"
                "To change the text, try this command again followed by your new text"
            ),
            quote=True
        )
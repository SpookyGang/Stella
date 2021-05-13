from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.database.welcome_mongo import (
    setReCaptcha,
    isReCaptcha
)

RECAPTCHA_TRUE = ['on', 'yes']
RECAPTCHA_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command('recaptcha'))
async def reCaptcha(client, message):

    chat_id = message.chat.id 
    if (
        len(message.command) >= 2
    ):
        command_arg = message.command[1]
        
        if (
            command_arg in RECAPTCHA_TRUE
        ):
            setReCaptcha(chat_id=chat_id, reCaptcha=True)
            await message.reply(
                'From now I\'ll ask captcha to every user even verifed users.'
            )
        
        elif (
            command_arg in RECAPTCHA_FALSE
        ):
            setReCaptcha(chat_id=chat_id, reCaptcha=False)
            await message.reply(
                'I\'ll not ask captcha again to who have already completed CAPTCHA.'
            )
        
        else:
            await message.reply(
                f'This isn\'t a boolean - excpected one of yes/on or no/off: got: {command_arg}'
            )

    else:
        if isReCaptcha(chat_id=chat_id):
            await message.reply(
                'reCaptcha: **enable**; I\'ll ask captcha to every users even veried users.\n\n'
                'To chnage this setting, try this command again followed by one of yes/no/on/off'
            )
        else:
            await message.reply(
                'reCaptcha: **disable**; I\'ll not ask captcha again to who have already completed CAPTCHA.\n\n'
                'To chnage this setting, try this command again followed by one of yes/no/on/off'
            )    
#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from Stella import StellaCli
from Stella.database.welcome_mongo import isReCaptcha, setReCaptcha
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin

RECAPTCHA_TRUE = ['on', 'yes']
RECAPTCHA_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command('recaptcha'))
async def reCaptcha(client, message):

    chat_id = message.chat.id 

    if not await isUserAdmin(message):
        return
        
    if (
        len(message.command) >= 2
    ):
        command_arg = message.command[1]
        
        if (
            command_arg in RECAPTCHA_TRUE
        ):
            setReCaptcha(chat_id=chat_id, reCaptcha=True)
            await message.reply(
                "From now on, I'll ask the CAPTCHA to every new user; regardless of whether they'd joined the chat before and verified themselves."    
            )
            
        elif (
            command_arg in RECAPTCHA_FALSE
        ):
            setReCaptcha(chat_id=chat_id, reCaptcha=False)
            await message.reply(
                "I won't ask the CAPTCHA to users that have joined the chat before and already verified themselves."
            )
        
        else:
            await message.reply(
                f'This isn\'t a boolean - excpected one of yes/on or no/off: got: {command_arg}'
            )

    else:
        if isReCaptcha(chat_id=chat_id):
            await message.reply(
                "reCAPTCHA: **enabled**; I'm asking the CAPTCHA to every new user, be it someone who has joined before and verified already - they'll have to pass the CAPTCHA again.\n\n"
                "To chnage this setting, try this command again followed by one of yes/no/on/off"
            )
        else:
            await message.reply(
                "reCAPTCHA: **disabled**; I'm not asking the CAPTCHA to people who have joined before and verified themselves.\n\n"
                "To chnage this setting, try this command again followed by one of yes/no/on/off"
            )    

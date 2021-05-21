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
from Stella.database.welcome_mongo import SetCaptcha, isGetCaptcha
from Stella.helper import custom_filter
from Stella.helper.chat_status import isBotCan, isUserCan
from Stella.plugins.connection.connection import connection

CAPTCHA_WELCOME_TRUE = ['on', 'yes']
CAPTCHA_WELCOME_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('captcha')))
async def Captcha(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not await  isBotCan(message, permissions='can_restrict_members', silent=True):
        await message.reply(
            "I need to be admin with the right to restrict to enable CAPTCHAs.",
            quote=True
        )
        return 
    
    if not isUserCan(message, permissions='can_restrict_members', silent=True):
        await message.reply(
            "You need to be admin with the right to restrict to enable CAPTCHAs.",
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

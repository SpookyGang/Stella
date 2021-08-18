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
from Stella.database.welcome_mongo import GetCaptchaSettings, SetCaptchaMode
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import isBotAdmin, isUserCan
from Stella.plugins.connection.connection import connection

CAPTCHA_MODE_MAP = {
    "text": "Text CAPTCHAs require the user to answer a CAPTCHA containing letters and numbers.",
    "math": "Math CAPTCHAs require the user to solve a basic maths question. Please note that this may discriminate against users with little maths knowledge.",
    "button": "Button CAPTCHAs simply require a user to press a button in their welcome message to confirm they're human."
    }

@StellaCli.on_message(custom_filter.command(commands=('captchamode')))
@anonadmin_checker
async def CaptchaMode(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id 

    if not await isUserCan(message, permissions='can_change_info'):
        return
        
    if not await  isBotAdmin(message, silent=True):
        await message.reply(
            "I need to be admin with the right to restrict to enable CAPTCHAs."
        )
        return 

    if (
        len(message.command) >= 2
    ):
        GetArgs = message.command[1]
        if GetArgs == 'text':
            SetCaptchaMode(chat_id, 'text')
            await message.reply(
                "CAPTCHA set to **text**.\n\n"
                f"{CAPTCHA_MODE_MAP['text']}"
            )
        
        elif GetArgs == 'math':
            SetCaptchaMode(chat_id, 'math')
            await message.reply(
                "CAPTCHA set to **math**.\n\n"
                f"{CAPTCHA_MODE_MAP['math']}"
            )
        
        elif GetArgs == 'button':
            SetCaptchaMode(chat_id, 'button')
            await message.reply(
                "CAPTCHA set to **button**.\n\n"
                f"{CAPTCHA_MODE_MAP['button']}"
            )
        
        else:
            await message.reply(
                f"'{GetArgs}' is not a recognised CAPTCHA mode! Try one of: button/math/text"
            )
    else:
        captcha_mode, captcha_text, captcha_kick_time = GetCaptchaSettings(chat_id)

        if captcha_mode is None:
            captcha_mode = 'button'
        
        await message.reply(
            (
                f"The current CAPTCHA mode is: {captcha_mode}\n"
                f"{CAPTCHA_MODE_MAP[captcha_mode]}\n\n"
                "Available CAPTCHA modes are: button/math/text"
            )
        )

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
from Stella.database.welcome_mongo import isRuleCaptcha, setRuleCaptcha
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin

CAPTCHARULE_TRUE = ['on', 'yes']
CAPTCHARULE_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command('captcharules'))
async def rulecaptcha(client, message):
    
    chat_id = message.chat.id

    if (
        len(message.command) >= 2
    ):
        command_arg = message.command[1]
        if (
            command_arg in CAPTCHARULE_TRUE
        ):
            setRuleCaptcha(chat_id=chat_id, rule_captcha=True)
            await message.reply(
                "CAPTCHA rules have been enable. Users now need to accept rules as part of the CAPTCHA."
            )
    
        elif (
            command_arg in CAPTCHARULE_FALSE
        ):
            setRuleCaptcha(chat_id=chat_id, rule_captcha=False)
            await message.reply(
                "CAPTCHA rules have been disabled. Users will not need to accept rules as part of the CAPTCHA."
            )
        
        else:
            await message.reply(
                f"That isn't a boolean - excpected one of /yes/on or no/off; got: {command_arg}"
            )
    
    else:
        print(isRuleCaptcha(chat_id=chat_id), chat_id)
        if isRuleCaptcha(chat_id=chat_id):
            text = (
                'CAPTCHA rules are currently enabled. Users will be asked to accept the rules while completing the CAPTCHA.'
            )
        else:
            text = (
                'CAPTCHA rules are currently disabled.'
            )
        
        await message.reply(
            (
                f'{text}\n\n'
                'To change this setting, try this command agin follwed by on of yes/no/no/off'
            )
        )

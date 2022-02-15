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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.plugins.connection.connect import connectRedirect
from Stella.plugins.greeting.captcha.button_captcha import \
    buttonCaptchaRedirect
from Stella.plugins.greeting.captcha.text_captcha import textCaptchaRedirect
from Stella.plugins.notes.private_notes import note_redirect
from Stella.plugins.rules.rules import rulesRedirect
# from Stella.plugins.help.help import redirectHelp

START_TEXT = (
    "Konnichiwa {mention}! I am Stella - the first telegram group management bot to be built in `Pyrogram` with the support of `MongoDB`, this also means I am faster than others in terms of processing and giving outputs. I have a large set of modular features to offer that'll help you manage your chats in an efficient way. \n\n"
    "— Add me to your group to get a taste of that lightning fast speed ⚡️\n\n"
    "**Do** /help **to get more information on how to use me or click the \"Help\" button below.**\n\n"
    "> Join our updates channel to stay updated about latest changes made to me and my support chat if you need any further help or wish to report an issue.\n\n"
    "Updates Channel: **@StellaUpdates**\n"
    "Support Chat: **@StellaSupportChat**"
)

@StellaCli.on_message(custom_filter.command(commands=('start')))
async def start(client, message):
    if (
        len(message.command) == 1
    ):
        if message.chat.type == 'private':
            buttons = [[
                InlineKeyboardButton('Help', callback_data='help_back')
                ]]
                    
            await message.reply_text(
                START_TEXT.format(mention=message.from_user.mention),
                reply_markup=InlineKeyboardMarkup(buttons),
                disable_web_page_preview=True,
                quote=True
                )

        elif message.chat.type == 'supergroup':
            await message.reply(
                "hey there, ping me in my PM to get help!"
            )
    
    if (
        len(message.command) > 1
    ):
        # # help
        # if startCheckQuery(message, StartQuery='help_'):
        #     await redirectHelp(message)
            
        # Captcha Redirect Implementation 
        if startCheckQuery(message, StartQuery='captcha'):
            await buttonCaptchaRedirect(message)
            await textCaptchaRedirect(message)

        # Private Notes Redirect Implementation 
        elif startCheckQuery(message, StartQuery='note'):
            await note_redirect(message)
        
        # Connection Redirect Implementation
        elif startCheckQuery(message, StartQuery='connect'):
            await connectRedirect(message)
        
        # Rules Redirect Implementation
        elif startCheckQuery(message, StartQuery='rules'):
            await rulesRedirect(message)

    

def startCheckQuery(message, StartQuery=None) -> bool:
    if (
        StartQuery in message.command[1].split('_')[0]
        and message.command[1].split('_')[0] == StartQuery
    ):
        return True
    return False 

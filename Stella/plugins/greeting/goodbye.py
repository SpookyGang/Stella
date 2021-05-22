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


from pyrogram.types import InlineKeyboardMarkup
from Stella import StellaCli
from Stella.database.welcome_mongo import (DEFAUT_GOODBYE, GetCleanService,
                                           GetGoobye, GetGoodbyemessageOnOff,
                                           SetGoodbyeMessageOnOff, isGoodbye)
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.chat_status import isUserCan
from Stella.helper.welcome_helper.welcome_send_message import \
    SendWelcomeMessage
from Stella.plugins.connection.connection import connection

GOODBYE_TRUE = ['on', 'yes']
GOODBYE_FALSE = ['off', 'no']

@StellaCli.on_message(custom_filter.command(commands=('goodbye')))
@anonadmin_checker
async def Welcome(client, message):

    if await connection(message) is not None:
        chat_id = await connection(message)
    else:
        chat_id = message.chat.id

    if not await isUserCan(message, permissions='can_change_info'):
        return

    if len(message.command) >= 2:
        GetWelcomeArg = message.command[1]
        if (
            GetWelcomeArg in GOODBYE_TRUE
        ):
            SetGoodbyeMessageOnOff(chat_id, goodbye_message=True)  
            await message.reply(
                "I'll be saying goodbye to any leavers from now on!",
                quote=True
            )
        
        elif (
            GetWelcomeArg in GOODBYE_FALSE
        ):
            SetGoodbyeMessageOnOff(chat_id, goodbye_message=False)
            await message.reply(
                "I'll stay quiet when people leave.",
                quote=True
            )

        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off",
                quote=True
            )

    elif len(message.command) == 1:
        if GetGoodbyemessageOnOff(chat_id):
            GoodByeMessage = 'true'
        else:
            GoodByeMessage = 'false' 
        
        if GetCleanService(chat_id):
            CleanService = 'true'
        else:
            CleanService = 'false'

        GOODBYE_MESSAGE = (
            f"I am currently saying goodbye to users: `{GoodByeMessage}`\n"
            f"I am currently deleting service messages: `{CleanService}`\n"
            "NOTE: If your group has more than 50 members, it is possible that Stella will stop wishing users goodbye - this is a Telegram restriction.\n\n"
            "Members are currently bidden farewell with:"
        )

        GoodByeSentMessage = await message.reply(
            GOODBYE_MESSAGE,
            quote=True
        )

        if isGoodbye(chat_id):
            Content, Text, DataType = GetGoobye(chat_id)
            Text, buttons = button_markdown_parser(Text)

            reply_markup = None
            if len(buttons) > 0:
                reply_markup = InlineKeyboardMarkup(buttons)
            GoodByeSentMessage = await SendWelcomeMessage(GoodByeSentMessage, None, Content, Text, DataType, reply_markup=reply_markup)
        else:
            await GoodByeSentMessage.reply(
                DEFAUT_GOODBYE
            )

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


import html

from Stella import StellaCli
from Stella.database.antiflood_mongo import setflood_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs, isBotAdmin


@StellaCli.on_message(custom_filter.command(commands=('setflood')))
async def setflood(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title

    if not await isBotAdmin(message):
        await message.reply(
            f"I don't have admin rights in {html.escape(chat_title)}! if you want me to enforce antiflood, you need to give me message deleting and banning permissions."
        )
        return

    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            'I was expecting some arguments but turned out you\'re an exception to people that have a functioning brain! \nEither off, or an integer. eg: `/setflood 5`, or `/setflood off` will work'
        )
        return
    
    arg = message.command[1]

    if (
        arg == 'off'
        or (
            arg.isdigit()
            and int(arg) == 0
        )
    ):
        setflood_db(chat_id, False)
        await message.reply(
            "I've disable antiflood."
        )
        return
    
    elif (
        arg.isdigit()
    ):
        if int(arg) > 75:
            await message.reply(
                "The flood limit is 75. You can set a value between 0 and 75."
            )
        else:
            setflood_db(chat_id, int(arg))
            await message.reply(
                f"Antiflood settings for {html.escape(chat_title)} have been updated and the flood limit is changed to `{arg}`."
            )
    else:
        await message.reply(
            f"{arg} is not a valid integer."
        )

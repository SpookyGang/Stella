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
from Stella.database.blocklists_mongo import add_blocklist_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs
from Stella.helper.get_data import get_text_reason


@StellaCli.on_message(custom_filter.command(commands=['addblocklist', 'addblacklist']))
async def add_blocklist(client, message):

    chat_id = message.chat.id 
    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            (
                "You're gonna need to provide a blocklist trigger and reason!\n"
                "eg: `/addblocklist \"the admins suck\" Respect your admins!`"
            )
        )
        return
    
    text, reason = get_text_reason(message)
    add_blocklist_db(chat_id, text, reason)
    await message.reply(
        f"I have added blocklist filter '`{text}`'!",
        quote=True
    )


    

    
        
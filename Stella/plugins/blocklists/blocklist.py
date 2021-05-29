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
from Stella.database.blocklists_mongo import get_blocklist
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin


@StellaCli.on_message(custom_filter.command(commands=['blocklist', 'blacklist']))
async def blocklist(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title
    if not await isUserAdmin(message):
        return
    
    BLOCKLIST_DATA = get_blocklist(chat_id)
    if (
        BLOCKLIST_DATA is None
        or len(BLOCKLIST_DATA) == 0
    ):
        await message.reply(
            f"No blocklist filters are active in {html.escape(chat_title)}!"
        )
        return

    BLOCKLIST_ITMES = []
    for blocklist_array in BLOCKLIST_DATA:
        BLOCKLIST_ITMES.append(blocklist_array['blocklist_text'])
    
    blocklist_header = f"The following blocklist filters are currently active in {html.escape(chat_title)}:\n"
    for block_itmes in BLOCKLIST_ITMES:
        blocklist_name = f"- `{block_itmes}`\n"
        blocklist_header += blocklist_name

    await message.reply(
        blocklist_header,
        quote=True
    )

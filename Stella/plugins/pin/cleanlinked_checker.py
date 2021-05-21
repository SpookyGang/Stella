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

from pyrogram import filters
from pyrogram.types import Message
from Stella import StellaCli
from Stella.database.pin_mongo import get_cleanlinked
from Stella.helper.chat_status import isBotCan


@StellaCli.on_message(filters.all & filters.group, group=6)
async def cleanlinkedChecker(client, message):
    chat_id = message.chat.id
    if not get_cleanlinked(chat_id):
        return

    channel_id = await GetLinkedChannel(chat_id)
    if channel_id is not None:
        if (
            message.forward_from_chat
            and message.forward_from_chat.type == 'channel'
            and message.forward_from_chat.id == channel_id
        ):
            if await isBotCan(message , permissions='can_delete_messages', silent=True):
                await message.delete()
            else:
                await message.reply(
                    "I don't the right to delete messages in the linked channel.\nError: `not_enough_permissions`"
                )

async def GetLinkedChannel(chat_id: int) -> str:
    chat_data = await StellaCli.get_chat(
        chat_id=chat_id
    )
    if chat_data.linked_chat:
        return chat_data.linked_chat.id
    else:
        return None

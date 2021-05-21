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
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs


@StellaCli.on_message(custom_filter.command(commands=('pin')))
async def pin(client, message):

    chat_id = message.chat.id
    if not await CheckAllAdminsStuffs(message, permissions='can_pin_messages'):
        return 
    
    if not message.reply_to_message:
        await message.reply(
            "You need to reply to a message to pin it!"
        )
        return

    pin_message_id = message.reply_to_message.message_id
    message_link = f"http://t.me/c/{str(chat_id).replace(str(-100), '')}/{pin_message_id}"

    if (
        len(message.command) == 1
        or (
            len(message.command) >= 2
            and message.command[1] in (
                'silent',
                'quiet'
            )
        )
    ):
        await StellaCli.pin_chat_message(
            chat_id=chat_id,
            message_id=pin_message_id,
            disable_notification=True
        )
        await message.reply(
            f"I have pinned [this message]({message_link})."
        )
    
    elif (
        len(message.command) >= 2
        and message.command[1] in (
            'loud',
            'notify',
            'violent'
        )
    ):
        await StellaCli.pin_chat_message(
            chat_id=chat_id,
            message_id=pin_message_id,
            disable_notification=False
        )
        await message.reply(
            f"I have pinned [this message]({message_link}) and notified all members."
        )
    
    elif (
        len(message.command) >= 2
    ):
        await message.reply(
            f"'{message.command[1]}' was not recognised as a valid pin option. Please use one of: loud/violent/notify/silent/quiet"
        )

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

from Stella import BOT_ID, StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import isBotCan, isUserCan
from Stella.helper.get_user import get_text
from Stella.plugins.warnings.warn import warn


@StellaCli.on_message(custom_filter.command(commands=['warn', 'swarn', 'dwarn']))
async def addwarn(client, message):

    chat_id = message.chat.id
    message_id = None
    silent=False

    if not await isUserCan(message, permissions='can_restrict_members'):
        return 
    
    if not await isBotCan(message, permissions='can_restrict_members'):
        return 

    reason = get_text(message)
    if not reason:
        reason = None
    
    if message.command[0].find('dwarn') >= 0:
        if message.reply_to_message:
            message_id = message.reply_to_message.message_id

    elif message.command[0].find('swarn') >= 0:
        message_id = message.message_id  

    if message.command[0].find('swarn') >= 0:
        silent=True

    warn_r = await warn(message, reason, silent, warn_user=None)

    if warn_r:
        # Deletaion of message according to user admin command
        if message_id is not None:
            await StellaCli.delete_messages(
                    chat_id=chat_id,
                    message_ids=message_id
                )

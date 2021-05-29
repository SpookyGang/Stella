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


import time
import uuid

from Stella import LOG_CHANNEL, StellaCli, TELEGRAM_SERVICES_IDs
from Stella.database.federation_mongo import new_fed_db
from Stella.helper import custom_filter


@StellaCli.on_message(custom_filter.command(commands=('newfed')))
async def NewFed(client, message):

    if (
        message.chat.type == 'supergroup'
    ):
        await message.reply(
            'Create your federation in my PM - not in a group.'
        )
        return 

    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "Give your federation a name!"
        )  
        return

    if (
        message.from_user.id in TELEGRAM_SERVICES_IDs
    ):
        await message.reply(
            "This is telegram services IDs, I should not create any new fed for it."
        )
        return

    if (
        len(' '.join(message.command[1:])) > 60
    ):
        await message.reply(
            "Your fed must be smaller than 60 words."
        )
        return

    fed_name = ' '.join(message.command[1:])
    fed_id = str(uuid.uuid4())
    owner_id = message.from_user.id 
    created_time = time.ctime() 

    new_fed_db(fed_name, fed_id, created_time, owner_id)

    await message.reply(
        (
            "Created new federation with FedID: "
            f"`{fed_id}`\n\n"
            "Use this ID to join federation! eg:\n"
            f"`/joinfed {fed_id}`"
        )
    )

    await StellaCli.send_message(
        chat_id=LOG_CHANNEL,
        text=(
            "New Federation created with FedID: "
            f"`{fed_id}`\n"
            f"OwnerID: `{owner_id}`\n"
            f"Created at `{created_time}`"
        )
    )

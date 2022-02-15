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

import json

from Stella import OWNER_ID, SUDO_USERS, StellaCli, StellaDB
from Stella.helper import custom_filter

COLLECTIONS_DATAS = StellaDB.list_collection_names()

@StellaCli.on_message(custom_filter.command(commands=('dbimport')))
async def StellaImport(client, message):
    user_id = message.from_user.id

    if not user_id in OWNER_ID:
        return

    if (
        user_id in SUDO_USERS
    ):
        await message.reply(
            "This command is mode for only my kami-samas!"
        )
        return
    
    if not message.reply_to_message:
        await message.reply(
            "Reply to exported data!"
        )
        return
    
    if not (
        len(COLLECTIONS_DATAS) == 0
    ):
        await message.reply(
            (
                "Make sure you import the backup in fresh mongoDB! - "
                f"Your mongoDB has `{len(COLLECTIONS_DATAS)}` collections right now."
            )
        )
        return

    download_path = await StellaCli.download_media(
        message=message.reply_to_message.document
    )

    starting_msg = await message.reply(
        "Started importing job!"
    )

    with open(download_path) as f:
        data = json.load(f)
    COLLECTIONS_NAMES = data['collections']

    collection_lists = []

    for collection in COLLECTIONS_NAMES:
        for exportData in data['exports_data']:
            get_col = exportData.get(collection)
            if not get_col is None:
                for doc in get_col:
                    collection_lists.append(doc)
                StellaDB[collection].insert_many(collection_lists)
                collection_lists.clear()
                import_msg = await starting_msg.edit_text(
                    f"{collection} imported!"
                )
    await import_msg.edit_text(
        "Imported all collectons!"
    )
 
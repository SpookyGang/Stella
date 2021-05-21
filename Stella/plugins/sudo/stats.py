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

from Stella import OWNER_ID, SUDO_USERS, StellaCli, StellaDB
from Stella.__main__ import STATS
from Stella.helper import custom_filter
from Stella.helper.convert import convert_size


@StellaCli.on_message(custom_filter.command(commands=('stats')))
async def stats(client, message):
    user_id = message.from_user.id 
    if not (
        user_id in SUDO_USERS
        or user_id in OWNER_ID
    ):
        return
    
    if user_id in OWNER_ID:
        text = 'Konnichiwa, Ojii-san! —\n\n'
    elif user_id in SUDO_USERS:
        text = 'Konnichiwa, Onii-chan! —\n\n'

    for m in STATS:
        if m.__stats__:
            text += f'- {m.__stats__()}'
            
    text += dbstats()
    await message.reply(
        text
    )

def dbstats():
    StellaMongoDB = StellaDB.command("dbstats")
    if 'fsTotalSize' in StellaMongoDB:
        text = '\n\nAnddd, that does take `{}`, of my brain *coughs*~ I mean, database size! I have `{}` **free** so needn\'t worry!\n'.format(
            convert_size(StellaMongoDB['dataSize']),
            convert_size(StellaMongoDB['fsTotalSize'] - StellaMongoDB['fsUsedSize'])
        )
    else:
        text = '\n\nAnddd, that does take `{}`, of my brain *coughs*~ I mean, database size! I have `{}` **free** so needn\'t worry!\n'.format(
            convert_size(StellaMongoDB['storageSize']),
            convert_size(536870912 - StellaMongoDB['storageSize'])
        )
    return text

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
from Stella.database.users_mongo import add_user
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.helper.get_user import get_user_id


@StellaCli.on_message(custom_filter.command(commands=('forcecacheuser')))
async def forcecacheuser(client, message):
    
    if not (
        message.chat.type == 'private'
    ):
        if not await isUserAdmin(message):
            return
    
    user_info = await get_user_id(message)
    user_id = user_info.id 

    user_data = await StellaCli.get_users(
        user_ids=user_id
    )
    
    user_name = user_data.username

    add_user(user_id, username=user_name, Forwared=True)
    await message.reply(
        "I've exported this user's data to my database. I hope to not forget it again~ tee-hee"
    )
    

    

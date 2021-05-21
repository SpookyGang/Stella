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
from Stella.helper.chat_status import isUserAdmin


@StellaCli.on_message(custom_filter.command(commands=('pininfo')))
async def pininfo(client, message):

    if not await isUserAdmin(message):
        return 
    
    await message.reply(
        (
            "`/antichannelpin` and `/cleanlinked` can't be enabled at the same time because there's no point in doing so.\n\n"
            "As `/cleanlinked` automatically deletes messages sent by the linked channel and it's removed from the pin."
        )
    )

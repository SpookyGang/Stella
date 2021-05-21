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


@StellaCli.on_message(custom_filter.command(commands=('logcategories')))
async def logcategories(client, message):
    
    if not await isUserAdmin(message):
        return 
    
    await message.reply(
        (
            "The following log categories are supported:\n"
            "- `settings`: Bot settings which can be toggled or edited - such as blacklists, welcomes, rules, etc.\n"
            "- `admin`: Admin actions - such as bans, mutes, kicks, and warns.\n"
            "- `user`: User actions - such as kickme, or joining/leaving.\n"
            "- `automated`: Automated admin actions taken after locks, blacklists, or antiflood have been triggered\n"
            "- `reports`: Reports from users - through @admin, or /report.\n"
            "- `other`: Logs regarding extra features, such as notes and filters.\n\n"
            "Enable or disable them to change what data is logged in your logchannel."
        )
    )
    


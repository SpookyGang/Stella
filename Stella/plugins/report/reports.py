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
from Stella.database.report_mongo import get_report, reports_db
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin, isUserCan

REPORTS_TRUE = ['yes', 'on']
REPORTS_FALSE = ['no', 'off']

@StellaCli.on_message(custom_filter.command(commands=('reports')))
async def reports(client, message):

    chat_id = message.chat.id

    if not await isUserAdmin(message):
        return
        
    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if (
        len(message.command) >= 2
    ):
        report_args = message.command[1]

        if (
            report_args in REPORTS_TRUE
        ):
            reports_db(chat_id, True)
            await message.reply(
                "Users will now be able to report messages."
            )
        
        elif (
            report_args in REPORTS_FALSE
        ):
            reports_db(chat_id, False)
            await message.reply(
                "Users will no longer be able to report via @admin or /report."
            )
        else:
            await message.reply(
                "Your input was not recognised as one of: yes/no/on/off"
            )
    else:
        if get_report(chat_id):
            text = (
                "Reports are currently enabled in this chat.\n"
                "Users can use the /report command, or mention @admin, to tag all admins.\n\n"
            )
        else:
            text = "Reports are currently disabled in this chat.\n\n"
        
        await message.reply(
            f"{text} To change this setting, try this command again, with one of the following args: yes/no/on/off"
        )

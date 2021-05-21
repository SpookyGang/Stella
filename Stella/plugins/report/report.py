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
from Stella import StellaCli
from Stella.database.report_mongo import get_report
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin


async def report_(client, message):
    chat_id = message.chat.id

    if not get_report(chat_id):
        return
    
    if await isUserAdmin(message, silent=True):
        await message.reply(
            "You're an admin here, why'd you need to report someone?"
        )
        return
    
    if not message.reply_to_message:
        await message.reply(
            "Which user you want to report?"
        )
        return
    
    if await isUserAdmin(message.reply_to_message, silent=True):
        await message.reply(
            "You can't report admin."
        )
        return
    
    reported_user = message.reply_to_message.from_user

    admin_data = await StellaCli.get_chat_members(
        chat_id=chat_id,
        filter='administrators'
        )
        
    ADMINS_TAG = str()
    TAG = u'\u200b'
    for admin in admin_data:
        if not admin.user.is_bot:
            ADMINS_TAG = ADMINS_TAG + f'[{TAG}](tg://user?id={admin.user.id})'

    await message.reply(
        f"Reported {reported_user.mention} to admins.{ADMINS_TAG}"
    )

@StellaCli.on_message(custom_filter.command(commands=('report')))
async def report(client, message):
    await report_(client, message)

@StellaCli.on_message(filters.regex(pattern=(r"(?i)@admin(s)?")))
async def regex_report(client, message):
    await report_(client, message)

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

from pyrogram.types import ChatPermissions
from Stella import StellaCli
from Stella.database.warnings_mongo import (count_user_warn,
                                            get_all_warn_reason, get_warn_mode,
                                            reset_user_warns, warn_limit)
from Stella.helper.chat_status import isBotCan, isUserCan


async def warn_checker(message, user_id, silent=False):
    chat_id = message.chat.id

    countuser_warn = count_user_warn(chat_id, user_id)
    warnlimit = warn_limit(chat_id)
    
    if  countuser_warn >= warnlimit:
        warn_mode, warn_mode_time = get_warn_mode(chat_id)
        
        if warn_mode == 1:
            await StellaCli.kick_chat_member(
                chat_id,
                user_id
            )
            
            if not silent:
                user_info = await StellaCli.get_users(
                    user_ids=user_id
                )
                REASONS = get_all_warn_reason(chat_id, user_id)

                text = f"That's {countuser_warn}/{warnlimit} warnings; {user_info.mention} is banned!\n"
                for reason in REASONS:
                    text += reason
                await message.reply(
                    text
                )
                reset_user_warns(chat_id, user_id)
            return True
        
        elif warn_mode == 2:
            await StellaCli.kick_chat_member(
                chat_id,
                user_id,
                int(time.time()) + 60 # wait 60 seconds in case of server goes down at unbanning time
            )
            
            if not silent:
                user_info = await StellaCli.get_users(
                    user_ids=user_id
                )
                REASONS = get_all_warn_reason(chat_id, user_id)

                text = f"That's {countuser_warn}/{warnlimit} warnings; {user_info.mention} is kicked!\n"
                for reason in REASONS:
                    text += reason
                await message.reply(
                    text
                )
                reset_user_warns(chat_id, user_id)

            # Unbanning proceess and wait 5 sec to give server to kick user first
            await asyncio.sleep(5) 
            await StellaCli.unban_chat_member(chat_id, user_id)

            return True
        
        elif warn_mode == 3:
            await StellaCli.restrict_chat_member(
                chat_id,
                user_id,
                ChatPermissions(
                    can_send_messages=False
                )
            )

            if not silent:
                user_info = await StellaCli.get_users(
                    user_ids=user_id
                )
                REASONS = get_all_warn_reason(chat_id, user_id)

                text = f"That's {countuser_warn}/{warnlimit} warnings; {user_info.mention} is muted!\n"
                for reason in REASONS:
                    text += reason
                await message.reply(
                    text
                )
                reset_user_warns(chat_id, user_id)
            return True

        elif warn_mode == 4:
            until_time = int(time.time() + int(warn_mode_time))
            await StellaCli.restrict_chat_member(
                chat_id,
                user_id,
                until_date=until_time
            )
            
            if not silent:
                user_info = await StellaCli.get_users(
                    user_ids=user_id
                )
                REASONS = get_all_warn_reason(chat_id, user_id)

                text = f"That's {countuser_warn}/{warnlimit} warnings; {user_info.mention} is temporarily banned!\n"
                for reason in REASONS:
                    text += reason
                await message.reply(
                    text
                )
                reset_user_warns(chat_id, user_id)
            return True

        elif warn_mode == 5:
            until_time = int(time.time() + int(warn_mode_time))
            await StellaCli.restrict_chat_member(
                chat_id,
                user_id,
                ChatPermissions(
                can_send_messages=False 
                ),
                until_date=until_time
            )

            if not silent:
                user_info = await StellaCli.get_users(
                    user_ids=user_id
                )
                REASONS = get_all_warn_reason(chat_id, user_id)

                text = f"That's {countuser_warn}/{warnlimit} warnings; {user_info.mention} is temporarily mutted!\n"
                for reason in REASONS:
                    text += reason
                await message.reply(
                    text
                )
                reset_user_warns(chat_id, user_id)
            return True
    else:
        return False

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


import asyncio
import time

from pyrogram import filters
from pyrogram.types import Message
from Stella import StellaCli
from Stella.database.antiflood_mongo import get_flood, get_floodlimit
from Stella.helper.chat_status import isUserAdmin

from . import floodmode_action


class FloodControl:
    FLOOD_COUNT = dict() 
    PREV_MSG_USER_ID = dict()


@StellaCli.on_message(filters.group & ~filters.edited, group=5)
async def FloodWatcher(client, message):
    if not message.from_user:
        return
        
    chat_id = message.chat.id
    user_id = message.from_user.id

    if not get_flood(chat_id):
        return
    
    FLOOD_LIMIT = get_floodlimit(chat_id)
    
    
    if await isUserAdmin(message, silent=True):
        FloodControl.FLOOD_COUNT[chat_id] = 0
        FloodControl.PREV_MSG_USER_ID[chat_id] = user_id
        return

    if (
        chat_id in FloodControl.PREV_MSG_USER_ID
        and user_id == FloodControl.PREV_MSG_USER_ID[chat_id]   
        ):
            FloodControl.FLOOD_COUNT[chat_id] += 1
    else:
        FloodControl.FLOOD_COUNT[chat_id] = 1
        FloodControl.PREV_MSG_USER_ID[chat_id] = user_id

    if FloodControl.FLOOD_COUNT[chat_id] >= FLOOD_LIMIT:
        await floodmode_action.AntiFLoodModeAction(message)
        if chat_id in FloodControl.PREV_MSG_USER_ID :
            FloodControl.PREV_MSG_USER_ID.pop(chat_id)
        if chat_id in FloodControl.FLOOD_COUNT :
            FloodControl.FLOOD_COUNT.pop(chat_id)
            
    return 

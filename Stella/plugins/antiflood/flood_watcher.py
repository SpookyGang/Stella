import time 
import asyncio

from pyrogram import filters
from pyrogram.types import Message

from Stella import StellaCli

from Stella.helper.chat_status import isUserAdmin

from Stella.database.antiflood_mongo import (
    get_flood,
    get_floodlimit
)

from . import floodmode_action

class FloodControl:
    FLOOD_COUNT = dict() 
    PREV_MSG_USER_ID = dict()


@StellaCli.on_message(filters.group & ~filters.edited, group=4)
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
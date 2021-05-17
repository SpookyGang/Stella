import time

from pyrogram.types import ChatPermissions, Message
from Stella import StellaCli
from Stella.database.antiflood_mongo import get_antiflood_mode
from Stella.helper.chat_status import can_restrict_member
from Stella.helper.convert import convert_time
from Stella.helper.time_checker import time_string_helper


async def AntiFLoodModeAction(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_mention = message.from_user.mention 

    FloodMode, Flood_until_time = get_antiflood_mode(chat_id)
    if FloodMode == 1:
        await StellaCli.kick_chat_member(
            chat_id,
            user_id
        )
        await message.reply(
            f"Yeah, I don't like your flooding. {user_mention} has been banned!"
        )
    
    elif FloodMode == 2:
        await StellaCli.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
                can_send_messages=False
            )
        )
        await message.reply(
            f"Yeah, I don't like your flooding. Quiet now {user_mention}!"
        )
    
    elif FloodMode == 3:
        await StellaCli.kick_chat_member(
            chat_id,
            user_id,
            int(time.time()) + 60 # wait 60 seconds in case of server goes down at unbanning time
        )
        await message.reply(
            f"Yeah, I don't like your flooding. {user_mention} has been kicked!"
        )

        # Unbanning proceess and wait 5 sec to give server to kick user first
        await asyncio.sleep(5) 
        await StellaCli.unban_chat_member(chat_id, user_id)

    elif FloodMode == 4:
        until_time = convert_time(int(Flood_until_time[:-1]), Flood_until_time[-1])
        time_limit, time_format = time_string_helper(Flood_until_time)
        await StellaCli.kick_chat_member(
            chat_id,
            user_id,
            int(time.time()) + int(until_time)
        )
        
        await message.reply(
                f"Yeah, I don't like your flooding. {user_mention} has been banned for {time_limit} {time_format}!"
        )
    
    elif FloodMode == 5:
        until_time = convert_time(int(Flood_until_time[:-1]), Flood_until_time[-1])
        time_limit, time_format = time_string_helper(Flood_until_time)
        await StellaCli.restrict_chat_member(
            chat_id,
            user_id,
            ChatPermissions(
            can_send_messages=False
            ),
            until_date=int(time.time()) + int(until_time)
        )
        await message.reply(
                f"Yeah, I don't like your flooding. {user_mention} has been muted for {time_limit} {time_format}!"
        )

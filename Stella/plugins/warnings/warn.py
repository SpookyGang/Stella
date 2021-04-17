from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message
)

from Stella import BOT_ID
from Stella.helper.get_user import get_user_id
from Stella.helper.chat_status import can_restrict_member
from Stella.database.warnings_mongo import (
    warn_db,
    count_user_warn,
    warn_limit
)
from Stella.plugins.warnings.warn_checker import warn_checker

async def warn(message, reason, silent=False, warn_user=None):

    chat_id = message.chat.id 
    admin_id = message.from_user.id 
    
    if warn_user is None:
        user_info = await get_user_id(message)
        user_id = user_info.id
        if user_id == BOT_ID:
            await message.reply(
                "I'm not gonna warn myself!"
            )
            return

        if not await can_restrict_member(message, user_id):
            await message.reply(
                "I'm not going to warn an admin!"
            )
            return

    else:
        user_info = warn_user.from_user
        user_id = warn_user.from_user.id 

    warn_db(chat_id, admin_id, user_id, reason)
    warnchecker = await warn_checker(message, user_id, silent)
    
    if (
        warnchecker == True
        or warnchecker == None
    ):
        return False

    countuser_warn = count_user_warn(chat_id, user_id)
    warnlimit = warn_limit(chat_id)

    warn_text = f"User {user_info.mention} has {countuser_warn}/{warnlimit} warnings; be careful!\n"
    if reason:
        warn_text += f"**Reason:**\n{reason}"

    button = [[InlineKeyboardButton(text='Remove warn (admin only)', callback_data=f'warn_{user_id}_{countuser_warn}')]]

    if not silent:    
        await message.reply(
            text=warn_text,
            reply_markup=InlineKeyboardMarkup(button)
        )
        return True
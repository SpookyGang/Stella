import html 

from pyrogram.types import ChatPermissions

from Stella import StellaCli, BOT_ID
from Stella.helper import custom_filter
from Stella.helper.chat_status import isBotCan, isUserCan, isUserBanned
from Stella.helper.get_user import get_user_id, get_text
from Stella.helper.anon_admin import anonadmin_checker


@StellaCli.on_message(custom_filter.command(commands=('unban')))
@anonadmin_checker
async def ban(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await isBotCan(message, permissions='can_restrict_members'):
        return
    if not await isUserCan(message, permissions='can_restrict_members'):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    if not await isUserBanned(chat_id, user_id):
        await message.reply(
            "This person hasn't been banned... how am I meant to unban them?"
        )
        return

    await StellaCli.unban_chat_member(
        chat_id,
        user_id
        )
    
    await message.reply(
        "Fine, they can join again."
    )
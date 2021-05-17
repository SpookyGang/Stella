import html

from Stella import BOT_ID, StellaCli
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import (CheckAllAdminsStuffs,
                                       can_restrict_member, isUserAdmin)
from Stella.helper.get_user import get_text, get_user_id


@StellaCli.on_message(custom_filter.command(commands=['ban', 'dban', 'sban']))
@anonadmin_checker
async def ban(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title
    message_id = None
    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    if user_id == BOT_ID:
        await message.reply(
            "You know what I'm not going to do? Ban myself."
        )
        return

    if not await can_restrict_member(message, user_id):
        await message.reply(
            "Why would I ban an admin? That sounds like a pretty dumb idea."
        )
        return
    
    await StellaCli.kick_chat_member(
        chat_id,
        user_id
        )
        
    
    if message.command[0].find('dban') >= 0:
        if message.reply_to_message:
            message_id = message.reply_to_message.message_id

    elif message.command[0].find('sban') >= 0:
        message_id = message.message_id   
    
    
    if not message.command[0].find('sban') >= 0:
        text = f"{user_info.mention} was Banned in {html.escape(chat_title)}.\n"
        
        reason = get_text(message)
        if reason:
            text += f"Reason: {reason}"

        await message.reply(
            text
        )
    
    # Deletaion of message according to user admin command
    if message_id is not None:
        await StellaCli.delete_messages(
                chat_id=chat_id,
                message_ids=message_id
            )

import html 

from pyrogram.types import ChatPermissions

from Stella import StellaCli, BOT_ID

from Stella.helper import custom_filter
from Stella.helper.chat_status import isBotAdmin, isUserAdmin, can_restrict_member
from Stella.helper.get_user import get_user_id, get_text
from Stella.helper.anon_admin import anonadmin_checker

MUTE_PERMISSIONS = ChatPermissions(
    can_send_messages=False
)



@StellaCli.on_message(custom_filter.command(commands=['mute', 'dmute', 'smute']))
@anonadmin_checker
async def mute(client, message):
    chat_id = message.chat.id 
    chat_title = message.chat.title
    message_id = None
    if not await isUserAdmin(message):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    if user_id == BOT_ID:
        await message.reply(
            "You know what I'm not going to do? mute myself."
        )
        return

    if not await isBotAdmin(message):
        return

    if not await can_restrict_member(message, user_id):
        await message.reply(
            "Why would I mute an admin? That sounds like a pretty dumb idea."
        )
        return
    
    await StellaCli.restrict_chat_member(
        chat_id,
        user_id,
        MUTE_PERMISSIONS
        )
        
    
    if message.command[0].find('dmute') >= 0:
        if message.reply_to_message:
            message_id = message.reply_to_message.message_id

    elif message.command[0].find('smute') >= 0:
        message_id = message.message_id   
    
    
    if not message.command[0].find('smute') >= 0:
        text = f"{user_info.mention} is mute now in {html.escape(chat_title)}.\n"
        
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
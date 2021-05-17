from pyrogram import filters
from Stella import StellaCli
from Stella.database.federation_mongo import (get_fed_from_chat,
                                              get_fed_reason, is_user_fban)
from Stella.helper.chat_status import isBotCan


@StellaCli.on_message(filters.all & filters.group, group=2)
async def fed_checker(client, message):
    
    chat_id = message.chat.id
    
    if not message.from_user:
        return

    user_id = message.from_user.id 
    fed_id = get_fed_from_chat(chat_id)
    
    if not fed_id == None:
        if is_user_fban(fed_id, user_id):
            fed_reason = get_fed_reason(fed_id, user_id)
            text = (
                    "**This user is banned in the current federation:**\n\n"
                    f"User: {message.from_user.mention} (`{message.from_user.id}`)\n"
                    f"Reason: `{fed_reason}`"
                )
            if await isBotCan(message, permissions='can_restrict_members'):
                if await StellaCli.kick_chat_member(chat_id, user_id): 
                    text += '\nAction: `Banned`'
            
            await message.reply(
                text
            )
            return 

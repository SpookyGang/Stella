from Stella import StellaCli, BOT_ID

from pyrogram.types import ChatPermissions

from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs, isUserAdmin, can_restrict_member
from Stella.helper.get_user import get_user_id
from Stella.helper.anon_admin import anonadmin_checker

@StellaCli.on_message(custom_filter.command(commands=('demote')))
@anonadmin_checker
async def promote(client, message):

    if not await CheckAllAdminsStuffs(message, permissions='can_promote_members'):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    chat_id = message.chat.id 
    
    if user_id == BOT_ID:
        await message.reply(
            "I'm not gonna demote myself."
        )
        return
        
    try:
        await StellaCli.restrict_chat_member(
            chat_id=chat_id,
            user_id=user_id,
            permissions=ChatPermissions(
                can_send_messages=True,
                can_pin_messages=False,
                can_invite_users=False,
                can_change_info=False
            )
        )
    except:
        user_data = await StellaCli.get_chat_member(
            chat_id=chat_id,
            user_id=user_id
            )

        await message.reply(
            (
                f"{user_info.mention} was promoted by {user_data.promoted_by.first_name} id `{user_data.promoted_by.id}`.\n"
                "__Nobody else can demote them except the chat owner and the one they were promoted by..__"
            )
        )
        return

    await message.reply(
        f"{user_info.mention} has been demoted!"
    )
    



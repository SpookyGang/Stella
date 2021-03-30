from Stella import StellaCli, BOT_ID, SUDO_USERS

from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs, can_restrict_member
from Stella.helper.get_user import get_user_id
from Stella.helper.anon_admin import anonadmin_checker


@StellaCli.on_message(custom_filter.command(commands=('promote')))
@anonadmin_checker
async def promote(client, message):

    if not await CheckAllAdminsStuffs(message, permissions='can_promote_members'):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id 
    chat_id = message.chat.id 

    if user_id == BOT_ID:
        await message.reply(
            "Pffff, I wish I could just promote myself."
        )
        return
    
    if user_id not in SUDO_USERS:
        if not await can_restrict_member(message, user_id):
            await message.reply(
                "How I suppose to promote a admin again?"
            )
            return

    await StellaCli.promote_chat_member(
        chat_id=chat_id,
        user_id=user_id,
        can_change_info=False
    )

    await message.reply(
        f"{user_info.mention} has been promoted!"
    )
    



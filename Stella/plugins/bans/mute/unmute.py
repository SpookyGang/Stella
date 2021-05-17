import html

from pyrogram.types import ChatPermissions
from Stella import BOT_ID, StellaCli
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import CheckAllAdminsStuffs
from Stella.helper.get_user import get_text, get_user_id

UNMUTE_PERMISSIONS = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_animations=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True
)


@StellaCli.on_message(custom_filter.command(commands=('unmute')))
@anonadmin_checker
async def ban(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title

    if not await CheckAllAdminsStuffs(message, permissions='can_restrict_members'):
        return
    
    user_info = await get_user_id(message)
    user_id = user_info.id
    
    await StellaCli.restrict_chat_member(
        chat_id,
        user_id,
        UNMUTE_PERMISSIONS
        )
    
    await message.reply(
        "Fine, they can speak again."
    )

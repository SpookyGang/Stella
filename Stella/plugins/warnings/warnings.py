import html
from Stella import StellaCli

from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin

from Stella.database.warnings_mongo import (
    warn_limit,
    get_warn_mode
)
from Stella.plugins.warnings.set_warn_mode import WarnModeMap

def warn_mode_map(warn_mode_in):
    warn_mode_raw = WarnModeMap(warn_mode_in)
    warn_mode_out = warn_mode_raw.name 
    return warn_mode_out

@StellaCli.on_message(custom_filter.command(commands=('warnings')))
async def warnings(client, message):

    chat_id = message.chat.id 
    chat_title = message.chat.title 
    if not await isUserAdmin(message):
        return
    
    warn_chat_limit = warn_limit(chat_id)
    text = (
        f"There is a {warn_chat_limit} warning limit in {html.escape(chat_title)}. "
    )
    warn_mode_in, warn_mode_time = get_warn_mode(chat_id) 
    warn_mode = warn_mode_map(warn_mode_in)
    if warn_mode == 'Ban': 
        text += (
            "When that limit has been exceeded, the user will be banned."
        ) 
    elif warn_mode == 'Kick':
        text += (
            "When that limit has been exceeded, the user will be kicked."
        )
    elif warn_mode == 'Mute':
        text += (
            "When that limit has been exceeded, the user will be muted."
        )
    elif warn_mode == 'Tmute':
        text += (
            "When that limit has been exceeded, the user will be temporarily muted."
        )
    elif warn_mode == 'Tban':
        text += (
            "When that limit has been exceeded, the user will be temporarily banned."
        )
    
    await message.reply(
        text,
        quote=True
    )

        

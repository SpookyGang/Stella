from Stella import StellaCli, BOT_ID

from Stella.helper import custom_filter
from Stella.helper.get_user import get_text
from Stella.helper.chat_status import (
    isUserCan,
    isBotCan
)

from Stella.plugins.warnings.warn import warn

@StellaCli.on_message(custom_filter.command(commands=['warn', 'swarn', 'dwarn']))
async def addwarn(client, message):

    chat_id = message.chat.id
    message_id = None
    silent=False

    if not await isUserCan(message, permissions='can_restrict_members'):
        return 
    
    if not await isBotCan(message, permissions='can_restrict_members'):
        return 

    reason = get_text(message)
    if not reason:
        reason = None
    
    if message.command[0].find('dwarn') >= 0:
        if message.reply_to_message:
            message_id = message.reply_to_message.message_id

    elif message.command[0].find('swarn') >= 0:
        message_id = message.message_id  

    if message.command[0].find('swarn') >= 0:
        silent=True

    warn_r = await warn(message, reason, silent, warn_user=None)

    if warn_r:
        # Deletaion of message according to user admin command
        if message_id is not None:
            await StellaCli.delete_messages(
                    chat_id=chat_id,
                    message_ids=message_id
                )
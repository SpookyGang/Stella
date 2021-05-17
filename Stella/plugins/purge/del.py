from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs


@StellaCli.on_message(custom_filter.command(commands=('del')))
async def delete(client, message):
    chat_id = message.chat.id
    message_id = message.message_id

    if not await CheckAllAdminsStuffs(message, permissions='can_delete_messages'):
        return

    if not message.reply_to_message:
        await message.reply(
            'Reply to any message to delete message.'
        )
        return
        
    try:
        reply_to_message = message.reply_to_message.message_id
        await StellaCli.delete_messages(
            chat_id=chat_id,
            message_ids=(
                [message_id, reply_to_message]
            )
        )
    except:
        await message.reply(
            "I can't delete messages here! Make sure I'm admin and can delete other user's messages."
        )

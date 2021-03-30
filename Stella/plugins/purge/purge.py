from Stella.helper import custom_filter
from Stella import StellaCli

from Stella.helper.chat_status import (
    CheckAllAdminsStuffs
)


@StellaCli.on_message(custom_filter.command(commands=['purge', 'spurge']))
async def purge(client, message):
    message_id = message.message_id + 1
    chat_id = message.chat.id
    command = message.command[0]
    MessageIDs = []

    if command == 'purge':
        LastMessageDelete = False
    elif command == 'spurge':
        LastMessageDelete = True

    if not await CheckAllAdminsStuffs(message, permissions='can_delete_messages'):
        return

    if not message.reply_to_message:
        await message.reply(
            'Reply to a message to show me where to purge from.'
        )
        return
        
    reply_to_message = message.reply_to_message.message_id
    for messageID in range(reply_to_message, message_id):
        MessageIDs.append(messageID)
    
    try:
        await StellaCli.delete_messages(
            chat_id=chat_id,
            message_ids=MessageIDs
        )

        if not LastMessageDelete:
            await StellaCli.send_message(
                chat_id=chat_id,
                text="Purge completed!"
            )
    except:
        await message.reply(
            "I can't delete messages here! Make sure I'm admin and can delete other user's messages."
        )


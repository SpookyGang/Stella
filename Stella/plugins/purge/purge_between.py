from Stella.helper import custom_filter
from Stella import StellaCli

from Stella.helper.chat_status import (
    CheckAllAdminsStuffs
)

from Stella.plugins.purge.purge_helper import (
    PurgeDictData,
    PurgeDictDataUpdater
)

@StellaCli.on_message(custom_filter.command(commands=['purgefrom', 'purgeto']))
async def PurgeBetween(client, message):
    chat_id = message.chat.id
    message_id = message.message_id 
    command = message.command[0]
    MessagesIDs = []
    PurgeData = PurgeDictData.PurgeDict

    if not await CheckAllAdminsStuffs(message, permissions='can_delete_messages'):
        return

    if not message.reply_to_message:
        await message.reply(
            'Reply to a message to show me where to purge from.'
        )
        return
        
    reply_to_message = message.reply_to_message.message_id
    if command == 'purgefrom':
        purge_from_message = await message.reply(
            "Message marked for deletion. Reply to another message with /purgeto to delete all messages in between."
        )
        purge_from_messageID = purge_from_message.message_id
        PurgeDictDataUpdater(
            chat_id, purge_from=reply_to_message,
            first_messageID=message_id,
            purge_from_messageID=purge_from_messageID
            )
        return

    elif command == 'purgeto':

        if not message.reply_to_message:
            await message.reply(
                'Reply to a message to let me know what to delete.'
            )
            return

        if chat_id in PurgeData.keys():
            PurgeDictDataUpdater(chat_id, purge_to=(reply_to_message + 1))

            purge_from = PurgeData[chat_id]['purge_from']
            first_messageID = PurgeData[chat_id]['first_messageID']
            purge_from_messageID = PurgeData[chat_id]['purge_from_messageID']
            purge_to = PurgeData[chat_id]['purge_to']

            ExtraMessageIDs = [
                message_id,
                first_messageID,
                purge_from_messageID
            ]

            for MessageID in range(purge_from, purge_to):
                MessagesIDs.append(MessageID)
            
            for MessageID in ExtraMessageIDs:
                MessagesIDs.append(MessageID)
            
            try:
                await StellaCli.delete_messages(
                    chat_id=chat_id,
                    message_ids=MessagesIDs
                )
                PurgeData.clear()
            except:
                await message.reply(
                    "I can't delete messages here! Make sure I'm admin and can delete other user's messages."
                )
            await message.reply(
                "Purge completed!"
            )
        else:
            await message.reply(
                "You can only use this command after having used the /purgefrom command."
            )

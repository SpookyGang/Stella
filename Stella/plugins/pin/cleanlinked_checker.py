from pyrogram import filters
from pyrogram.types import Message
from Stella import StellaCli
from Stella.database.pin_mongo import get_cleanlinked
from Stella.helper.chat_status import isBotCan


@StellaCli.on_message(filters.all & filters.group, group=6)
async def cleanlinkedChecker(client, message):
    chat_id = message.chat.id
    if not get_cleanlinked(chat_id):
        return

    channel_id = await GetLinkedChannel(chat_id)
    if channel_id is not None:
        if (
            message.forward_from_chat
            and message.forward_from_chat.type == 'channel'
            and message.forward_from_chat.id == channel_id
        ):
            if await isBotCan(message , permissions='can_delete_messages', silent=True):
                await message.delete()
            else:
                await message.reply(
                    "I don't the right to delete messages in the linked channel.\nError: `not_enough_permissions`"
                )

async def GetLinkedChannel(chat_id: int) -> str:
    chat_data = await StellaCli.get_chat(
        chat_id=chat_id
    )
    if chat_data.linked_chat:
        return chat_data.linked_chat.id
    else:
        return None

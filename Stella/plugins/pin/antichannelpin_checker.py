from pyrogram import filters
from pyrogram.types import Message
from Stella import StellaCli
from Stella.database.pin_mongo import get_antichannelpin
from Stella.helper.chat_status import isBotCan


@StellaCli.on_message(filters.all & filters.group, group=7)
async def cleanlinkedChecker(client, message):
    chat_id = message.chat.id
    message_id = message.message_id
    if not get_antichannelpin(chat_id):
        return

    channel_id = await GetLinkedChannel(chat_id)
    if channel_id is not None:
        if (
            message.forward_from_chat
            and message.forward_from_chat.type == 'channel'
            and message.forward_from_chat.id == channel_id
        ):
            if not await isBotCan(message , permissions='can_pin_messages', silent=True):
                await message.reply(
                    "I don't have the right to pin or unpin messages in this chat.\nError: `could_not_unpin`"
                )
                return
    
            await StellaCli.unpin_chat_message(
                chat_id=chat_id,
                message_id=message_id
            )

async def GetLinkedChannel(chat_id: int) -> str:
    chat_data = await StellaCli.get_chat(
        chat_id=chat_id
    )
    if chat_data.linked_chat:
        return chat_data.linked_chat.id
    else:
        return None

from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs


@StellaCli.on_message(custom_filter.command(commands=('unpin')))
async def unpin(client, message):

    chat_id = message.chat.id
    if not await CheckAllAdminsStuffs(message, permissions='can_pin_messages'):
        return 
    
    if message.reply_to_message:
        pinned_message_id = message.reply_to_message.message_id
        message_link = f"http://t.me/c/{str(chat_id).replace(str(-100), '')}/{pinned_message_id}"
        await StellaCli.unpin_chat_message(
            chat_id=chat_id,
            message_id=pinned_message_id
        )
        await message.reply(
            f"Unpinned [this message]({message_link})."
        )
    else:
        chat_data = await StellaCli.get_chat(
            chat_id=chat_id
        )
        if chat_data.pinned_message:
            pinned_message_id = chat_data.pinned_message.message_id
            await StellaCli.unpin_chat_message(
                chat_id=chat_id,
                message_id=pinned_message_id
            )
            await message.reply(
                f"Unpinned the last pinned message."
            )
        else:
            await message.reply(
                "There are no pinned messages. What are you trying to unpin?"
            )

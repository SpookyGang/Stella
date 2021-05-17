from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import CheckAllAdminsStuffs


@StellaCli.on_message(custom_filter.command(commands=('pin')))
async def pin(client, message):

    chat_id = message.chat.id
    if not await CheckAllAdminsStuffs(message, permissions='can_pin_messages'):
        return 
    
    if not message.reply_to_message:
        await message.reply(
            "You need to reply to a message to pin it!"
        )
        return

    pin_message_id = message.reply_to_message.message_id
    message_link = f"http://t.me/c/{str(chat_id).replace(str(-100), '')}/{pin_message_id}"

    if (
        len(message.command) == 1
        or (
            len(message.command) >= 2
            and message.command[1] in (
                'silent',
                'quiet'
            )
        )
    ):
        await StellaCli.pin_chat_message(
            chat_id=chat_id,
            message_id=pin_message_id,
            disable_notification=True
        )
        await message.reply(
            f"I have pinned [this message]({message_link})."
        )
    
    elif (
        len(message.command) >= 2
        and message.command[1] in (
            'loud',
            'notify',
            'violent'
        )
    ):
        await StellaCli.pin_chat_message(
            chat_id=chat_id,
            message_id=pin_message_id,
            disable_notification=False
        )
        await message.reply(
            f"I have pinned [this message]({message_link}) and notified all members."
        )
    
    elif (
        len(message.command) >= 2
    ):
        await message.reply(
            f"'{message.command[1]}' was not recognised as a valid pin option. Please use one of: loud/violent/notify/silent/quiet"
        )

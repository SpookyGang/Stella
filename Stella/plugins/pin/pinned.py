import html

from Stella import StellaCli
from Stella.helper import custom_filter


@StellaCli.on_message(custom_filter.command(commands=('pinned')))
async def pinned(client, message):

    chat_id = message.chat.id
    chat_title = message.chat.title

    chat_data = await StellaCli.get_chat(
        chat_id=chat_id
    )
    if chat_data.pinned_message:
        pinned_message_id = chat_data.pinned_message.message_id
        message_link = f"http://t.me/c/{str(chat_id).replace(str(-100), '')}/{pinned_message_id}"
        await message.reply(
            (
                f"The pinned message in {html.escape(chat_title)} is [here]({message_link})."
            )
        )
    else:
        await message.reply(
            (
                f"There is no pinned message in {html.escape(chat_title)}."
            )
        )

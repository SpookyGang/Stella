import html 
from Stella import StellaCli
from Stella.helper import custom_filter

from Stella.helper.chat_status import isUserCreator
from Stella.database.federation_mongo import (
    is_fed_exist,
    join_fed_db,
    get_fed_name
)

@StellaCli.on_message(custom_filter.command(commands=('joinfed')))
async def JoinFeb(client, message):
    
    if not (
        message.chat.type == 'supergroup'
    ):
        await message.reply(
            "Only supergroups can join feds."
        )
        return 
    
    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You need to specify which federation you're asking about by giving me a FedID!"
        )
        return

    if not (
        await isUserCreator(message)
    ):
        await message.reply(
            "Only Group Creator can join new fed!"
        )
        return 

    if not (
        is_fed_exist(message.command[1])
    ):
        await message.reply(
            "This FedID does not refer to an existing federation."
        )
        return

    fed_id = message.command[1]
    chat_id = message.chat.id
    chat_title = html.escape(message.chat.title)
    fed_name = get_fed_name(fed_id)

    join_fed_db(chat_id, chat_title,  fed_id)
    await message.reply(
        f'Successfully joined the "{fed_name}" federation! All new federation bans will now also remove the members from this chat.'
    )
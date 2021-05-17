from Stella import StellaCli
from Stella.database.users_mongo import add_chat
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin


@StellaCli.on_message(custom_filter.command(commands=('forcecachechat')))
async def forcecachechat(client, message):
    chat_id = message.chat.id 
    chat_title = message.chat.title

    if (
        message.chat.type == 'private'
    ):
        await message.reply(
            "This command is made to be used in group chats, not in pm!"
        )
        return 
    
    if not await isUserAdmin(message):
        return
    
    add_chat(chat_id, chat_title)
    await message.reply(
        "I've exported your chat's data to my database. I hope to not forget it again~ tee-hee"
    )
    

    

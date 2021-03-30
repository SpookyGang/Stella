from Stella import StellaCli
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin
from Stella.helper.get_user import get_user_id
from Stella.database.users_mongo import add_user

@StellaCli.on_message(custom_filter.command(commands=('forcecacheuser')))
async def forcecacheuser(client, message):
    
    if not (
        message.chat.type == 'private'
    ):
        if not await isUserAdmin(message):
            return
    
    user_info = await get_user_id(message)
    user_id = user_info.id 

    user_data = await StellaCli.get_users(
        user_ids=user_id
    )
    
    user_name = user_data.username

    add_user(user_id, username=user_name, Forwared=True)
    await message.reply(
        "I've exported this user's data to my database. I hope to not forget it again~ tee-hee"
    )
    

    

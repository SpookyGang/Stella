from Stella import BOT_ID, StellaCli
from Stella.database.federation_mongo import (get_connected_chats,
                                              get_fed_admins,
                                              get_fed_from_chat, get_fed_name,
                                              is_user_fban, user_unfban)
from Stella.helper import custom_filter
from Stella.helper.get_user import get_user_id


@StellaCli.on_message(custom_filter.command(commands=('unfban')))
async def unfed_ban(client, message):
    chat_id = message.chat.id
    user_info = await get_user_id(message)
    userID = user_info.id 
    
    bannerMention = message.from_user.mention 
    banner_name = message.from_user.first_name
    bannedID = message.from_user.id

    fed_id = get_fed_from_chat(chat_id)
    fed_name = get_fed_name(fed_id=fed_id)
    get_user = await StellaCli.get_users(
                user_ids=userID
            )

    FED_ADMINS = get_fed_admins(fed_id)
    
    if userID == BOT_ID:
        await message.reply(
            "Oh you're a funny one aren't you! How do you think I would have fbanned myself hm?."
        )
        return
    
    if bannedID not in FED_ADMINS:
        await message.reply(
            f"You aren't a federation admin of {fed_name}."
        )
        return

    if (
        message.reply_to_message 
        and len(message.command) >= 2
    ):
        reason_text = ' '.join(message.text.split()[1:])   
    
    elif (
        len(message.command) >= 3
    ):
        reason_text = ' '.join(message.text.split()[2:])  

    else:
        reason_text = 'No reason was given'
     
    
    reason = f"{reason_text} // un-Fbanned by {banner_name} id {bannedID}"
    if is_user_fban(fed_id, userID):
        user_unfban(fed_id, userID)
    else:
        pass

    # await message.reply(
    #     unfed_message
    # )


from Stella import StellaCli

from Stella.helper import custom_filter 
from Stella.helper.chat_status import isUserAdmin

@StellaCli.on_message(custom_filter.command(commands=('report')))
async def report(client, message):
    chat_id = message.chat.id
    
    # if await isUserAdmin(message, silent=True):
    #     await message.reply(
    #         "You're an admin here, why'd you need to report someone?"
    #     )
    #     return
    
    if not message.reply_to_message:
        await message.reply(
            "Which user you want to report?"
        )
        return
    
    reported_user = message.reply_to_message.from_user

    admin_list = await StellaCli.get_chat_members(
        chat_id=chat_id,
        filter='administrators'
        )
        
    ADMINS_LINK = []
    for admin in admin_list:
        if not admin.user.is_bot:
            ADMINS_LINK.append(
                f'[ ](tg://user?id={admin.user.id})'
            )

    ADMINS_ARRAY = ''.join(ADMINS_LINK)
    print(ADMINS_ARRAY)
    await message.reply(
        f"Reported {reported_user.mention} to admins. [{ADMINS_ARRAY}] (tg://user?id=604968079)"
    )   

#[​[](tg://user?id=680240877)​[](tg://user?id=1313665327)​](tg://user?id=604968079)

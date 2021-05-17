from Stella import OWNER_ID, StellaAPI, StellaCli
from Stella.helper import custom_filter


@StellaCli.on_message(custom_filter.command(commands=('promoteapi')))
async def promote_api_level(client, message):

    if (
        message.chat.type == 'private'
    ):
        return
        
    if not (
        message.from_user.id in OWNER_ID
    ):
        return 
    
    if not message.reply_to_message:
        return 
    
    status, operation = StellaAPI.promote_api(message.reply_to_message.from_user.id)

    if operation:
        await message.reply_to_message.reply(
            f"{message.reply_to_message.from_user.mention} has been promoted to `api_level: admin`."
        )
    
    else:
        await message.reply(
            status
        )



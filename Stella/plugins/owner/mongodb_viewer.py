from Stella import (
    StellaCli,
    StellaDB,
    OWNER_ID
)

from Stella.helper import custom_filter

@StellaCli.on_message(custom_filter.command('mongo'))
async def mongoViewer(client, message):
    
    if (
        message.from_user.id not in OWNER_ID
    ):
        return

    if (
        len(message.command) == 1
    ):
        await message.reply(
            'Give me `MongoDB argument!`'
        )
        return

    mongo_coll = message.command[1]
    await message.reply(
        f"`{StellaDB[mongo_coll].find_one({'chat_id': message.chat.id})}`"
    )
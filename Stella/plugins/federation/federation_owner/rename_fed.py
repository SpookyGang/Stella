from Stella import StellaCli
from Stella.helper import custom_filter

from Stella.database.federation_mongo import (
    fed_rename_db,
    get_fed_name,
    get_fed_from_ownerid,
    get_connected_chats
)

@StellaCli.on_message(custom_filter.command(commands=('renamefed')))
async def Rename_fed(client, message):
    owner_id = message.from_user.id 

    if not (
        message.chat.type == 'private'
    ):
        await message.reply(
            "You can only rename your fed in PM."
        )
        return

    if not (
        len(message.command) >= 2
    ):
        await message.reply(
            "You need to give your federation a name! Federation names can be up to 64 characters long."
        )
        return
    
    if (
        len(' '.join(message.command[1:])) > 60
    ):
        await message.reply(
            "you fed must be smaller than 60 words."
        )
        return

    fed_id = get_fed_from_ownerid(owner_id)
    if fed_id == None:
        await message.reply(
            "It doesn't look like you have a federation yet!"
        )
        return
    
    fed_name = ' '.join(message.command[1:])
    old_fed_name = get_fed_name(owner_id=owner_id)
    

    fed_rename_db(owner_id, fed_name)
    await message.reply(
        f"Tada! I've renamed your federation from '{old_fed_name}' to '{fed_name}'. ( FedID: `{fed_id}`.)"
    )

    # Send notification of Rename Fed to the all connected chat

    connected_chats = get_connected_chats(fed_id)
    for chat_id in connected_chats:
        await StellaCli.send_message(
            chat_id=chat_id,
            text=(
                "**Federation renamed**\n"
                f"**Old fed name:** {old_fed_name}\n"
                f"**New fed name:** {fed_name}\n"
                f"FedID: `{fed_id}`"
            )
        )
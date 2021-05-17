import html

from Stella import BOT_ID, StellaCli
from Stella.database.log_channels_mongo import set_log_db
from Stella.helper import custom_filter
from Stella.helper.anon_admin import anonadmin_checker
from Stella.helper.chat_status import isUserCan
from Stella.helper.get_data import GetChat
from Stella.plugins.connection.connection import connection


@StellaCli.on_message(custom_filter.command(commands=('setlog')))
@anonadmin_checker
async def set_log(client, message):
    
    if message.chat.type == 'channel':
        await message.reply(
            "Now, forward the previous message (your /setlog command) to the chat you wish to log here."
        )
        return

    if await connection(message) is not None:
        chat_id = await connection(message)
        chat_title = await GetChat(chat_id)
    else:
        chat_id = message.chat.id 
        chat_title = message.chat.title

    if not await isUserCan(message, permissions='can_change_info'):
        return
    
    if not (
        message.forward_from_chat 
        and message.forward_from_chat.type == 'channel'
    ):
        await message.reply(
            "You need to forward the /setlog message from a channel to set that channel as this chat's log channel. More info in /help.",
            quote=True
        )
        return 

    try:
        GetChannelData = await StellaCli.get_chat_member(
        chat_id=message.forward_from_chat.id,
        user_id=BOT_ID
        )
        
    except:
        await message.reply(
            "I'm not in the channel, make me an admin there and then repeat the command.",
            quote=True
        )
        return  

    if GetChannelData:
        if GetChannelData['can_post_messages']:
            channel_id = message.forward_from_chat.id
            channel_title = message.forward_from_chat.title
            set_log_db(chat_id, channel_id, channel_title)
            await message.reply(
                f"Successfully set log channel to {html.escape(channel_title)}. Further admin actions will be logged there.",
                quote=True
            )

            await StellaCli.send_message(
                chat_id=channel_id,
                text=(
                    f"This channel has been set as the log channel for {html.escape(chat_title)}. All new admin actions will be logged here."
                )
            )

        else:
            await message.reply(
                "I don't have rights to `can_post_messages` in the channel, make sure I have admin rights.",
                quote=True
            )
    

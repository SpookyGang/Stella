import html

from Stella import StellaCli
from Stella.database.connection_mongo import (GetConnectedChat,
                                              get_allow_connection,
                                              isChatConnected)
from Stella.helper import custom_filter
from Stella.helper.chat_status import isUserAdmin, isUserBanned
from Stella.plugins.connection.connect import connect_button


@StellaCli.on_message(custom_filter.command(commands=('connection')))
async def ConnectionChat(client, message):
    if not (
        message.chat.type == 'private'
    ):
        await message.reply(
            "You need to be in pm to use this."
        )
        return
    if await connection(message) is not None:
        chat_id = await connection(message)
        await connect_button(message, chat_id)
    else:
        await message.reply(
            "You aren't connected to any chats! Anything you save here is for your eyes only :)",
            quote=True
        )


async def connection(message):
    if not (
        message.chat.type == 'private'
    ):
        return None
        
    user_id = message.from_user.id
    connected_chat = GetConnectedChat(user_id)
    if isChatConnected:
        if connected_chat is not None:
            if get_allow_connection(connected_chat):
                if not await isUserBanned(connected_chat, user_id):
                    return connected_chat
                else:
                    await message.reply(
                        f"You are banned user of {chat_title}",
                        quote=True
                    )
                    return None
            else:
                return None
        else:
            return None
    else:
        return None
    
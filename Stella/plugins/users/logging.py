from pyrogram import filters

from Stella import StellaCli

from Stella.database.users_mongo import (
    add_user,
    add_chat
)

@StellaCli.on_message(filters.all & filters.group, group=1)
async def logger(client, message):
    if message.chat:
        chat_id = message.chat.id
        chat_title = message.chat.title
        add_chat(chat_id, chat_title)

    if message.from_user:
        user_id = message.from_user.id
        username = message.from_user.username
        chat_id = message.chat.id
        chat_title = message.chat.title
        add_user(user_id, username, chat_id, chat_title)
        add_chat(chat_id, chat_title)
    
    if (
        message.reply_to_message
        and message.reply_to_message.from_user
    ):

        user_id = message.reply_to_message.from_user.id
        username = message.reply_to_message.from_user.username
        chat_id = message.chat.id 
        chat_title = message.chat.title
        
        add_user(user_id, username, chat_id, chat_title)
        add_chat(chat_id, chat_title)

    if message.forward_from:

        user_id = message.forward_from.id
        username = message.forward_from.username
    
        add_user(user_id, username, Forwared=True)
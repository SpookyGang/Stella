import html
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
from Stella import StellaCli 

from Stella.helper.chat_status import isBotCan
from Stella.helper.welcome_helper.welcome_send_message import SendWelcomeMessage
from Stella.helper.welcome_helper.welcome_fillings import Welcomefillings
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.anon_admin import anonadmin_checker

from Stella.database.welcome_mongo import (
    GetCleanService,
    GetGoobye,
    isGoodbye,
    GetGoodbyemessageOnOff,
    DEFAUT_GOODBYE
)
@StellaCli.on_message(filters.left_chat_member)
@anonadmin_checker
async def goodbye_member(client, message):
    chat_id = message.chat.id
    chat_title = html.escape(message.chat.title)
    message_id = message.message_id

    # Check if bot is admin to delete services messages 
    if await isBotCan(message, permissions='can_delete_messages', silent=True):
        if GetCleanService(chat_id):
            await message.delete()
    else:
        await message.reply(
            "I dont have much permssion in this chat to clean service messages."
        )

    # If user set goodbye 
    if isGoodbye(chat_id):
        # If Goodbye: ON 
        if GetGoodbyemessageOnOff(chat_id):
            Content, Text, DataType = GetGoobye(chat_id)
            Text, buttons = button_markdown_parser(Text)

            # If Goodbye message has button greater than 0
            reply_markup = None
            if len(buttons) > 0:
                reply_markup = InlineKeyboardMarkup(buttons)
            
            GoodByeMessageSet = await SendWelcomeMessage(message, message.left_chat_member, Content, Text, DataType, reply_markup=reply_markup)
    else:
        # If Goodbye has No any messages set 
        Text = Welcomefillings(message, DEFAUT_GOODBYE, message.left_chat_member)
        reply_markup = None
        GoodByeMessageSet = await StellaCli.send_message(
            chat_id=chat_id,
            text=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
            )
        
            

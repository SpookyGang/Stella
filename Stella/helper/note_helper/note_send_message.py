import html
import re

from pyrogram.types import InlineKeyboardMarkup
from Stella import StellaCli
from Stella.database.notes_mongo import GetNote
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.note_helper.note_fillings import NoteFillings
from Stella.helper.note_helper.note_misc_helper import preview_text_replace
from Stella.plugins.connection.connection import connection


async def SendNoteMessage(message, note_name, from_chat_id):
    user_id = message.from_user.id
    if await connection(message) is not None:
        from_chat_id = await connection(message)
        message_id = message.message_id
        Content, Text, DataType = GetNote(from_chat_id, note_name)
        chat_id = message.from_user.id 
    else:
        # if /privatenotes on
        if not from_chat_id == None:
            message_id = message.message_id
            chat_id = message.from_user.id
            Content, text, DataType = GetNote(from_chat_id, note_name)
            Text = (
                f"**{note_name}:**\n\n"
                f"{text}"
            ) 

        else:
            message_id = message.message_id
            if message.reply_to_message:
                message_id = message.reply_to_message.message_id
            chat_id = message.chat.id 
            Content, Text, DataType = GetNote(chat_id, note_name)
    
    
    Text, Buttons = button_markdown_parser(Text)
    preview, Text = preview_text_replace(Text)

    Text = NoteFillings(message, Text)

    Text = html.escape(Text)
    
    # Check if string is empty or contain spaces only
    if (
        not Text
        or re.search("^\s*$", Text)
    ):
        Text = note_name

    reply_markup = None
    if len(Buttons) > 0:
        reply_markup = InlineKeyboardMarkup(Buttons)
    else:
        reply_markup = None

    if (
        DataType == 'TEXT'
    ):
        await StellaCli.send_message(
            chat_id=chat_id,
            text=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup,
            disable_web_page_preview=preview
        )
    
    elif (
        DataType == 'STICKER'
    ):
        await StellaCli.send_sticker(
            chat_id=chat_id,
            sticker=Content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        DataType == 'DOCUMENTS'
    ):
        
        await StellaCli.send_document(
            chat_id=chat_id,
            document=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        DataType == 'PHOTO'
    ):
        await StellaCli.send_photo(
            chat_id=chat_id,
            photo=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )  
    
    elif (
        DataType == 'AUDIO'
    ):
        await StellaCli.send_audio(
            chat_id=chat_id,
            audio=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    elif (
        DataType == 'VOICE'
    ):
        await StellaCli.send_voice(
            chat_id=chat_id,
            voice=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        DataType == 'VIDEO'
    ):
        await StellaCli.send_video(
            chat_id=chat_id,
            video=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        DataType == 'VIDEO_NOTE'
    ):
        await StellaCli.send_video_note(
            chat_id=chat_id,
            video_note=Content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    return 

#  Exceptions [400 BUTTON_URL_INVALID]: The button url is invalid (caused by "messages.SendMessage")
async def exceNoteMessageSender(message, note_name, from_chat_id=None):
    try:
        await SendNoteMessage(message, note_name, from_chat_id)
    except:
        await message.reply(
            (
                "The notedata was incorrect, please update it. The buttons are most likely to be broken. If you are sure you aren't doing anything wrong and this was unexpected - please report it in my support chat.\n"
                "**Error:** `invalid_url`"
            ),
            quote=True
        )

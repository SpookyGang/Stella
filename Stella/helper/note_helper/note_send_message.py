import html
import re

from pyrogram.types import InlineKeyboardMarkup, Message
from Stella import StellaCli
from Stella.database.notes_mongo import GetNote
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.note_helper.note_fillings import NoteFillings
from Stella.helper.note_helper.note_misc_helper import preview_text_replace
from Stella.plugins.connection.connection import connection


async def SendNoteMessage(message: Message, note_name: str, from_chat_id: int):
    
    user_id = message.from_user.id
    if await connection(message) is not None:
        from_chat_id = await connection(message)
        message_id = message.message_id
        content, text, data_type = GetNote(from_chat_id, note_name)
        chat_id = message.from_user.id 
    else:
        # if /privatenotes on
        if from_chat_id is not None:
            message_id = message.message_id
            chat_id = message.from_user.id
            content, text, data_type = GetNote(from_chat_id, note_name)
            text = (
                f"**{note_name}:**\n\n"
                f"{text}"
            ) 

        else:
            message_id = message.message_id
            if message.reply_to_message:
                message_id = message.reply_to_message.message_id
            chat_id = message.chat.id 
            content, text, data_type = GetNote(chat_id, note_name)
    
    
    text, buttons = button_markdown_parser(text)
    preview, text = preview_text_replace(text)

    text = NoteFillings(message, text)

    text = html.escape(text)
    
    # Check if string is empty or contain spaces only
    if (
        not text
        or re.search("^\s*$", text)
    ):
        text = note_name

    reply_markup = None
    if len(buttons) > 0:
        reply_markup = InlineKeyboardMarkup(buttons)
    else:
        reply_markup = None

    if (
        data_type == 1
    ):
        await StellaCli.send_message(
            chat_id=chat_id,
            text=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup,
            disable_web_page_preview=preview
        )
    
    elif (
        data_type == 2
    ):
        await StellaCli.send_sticker(
            chat_id=chat_id,
            sticker=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 3
    ):
        await StellaCli.send_animation(
            chat_id=chat_id,
            animation=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        data_type == 4
    ):
        
        await StellaCli.send_document(
            chat_id=chat_id,
            document=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        data_type == 5
    ):
        await StellaCli.send_photo(
            chat_id=chat_id,
            photo=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )  
    
    elif (
        data_type == 6
    ):
        await StellaCli.send_audio(
            chat_id=chat_id,
            audio=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    elif (
        data_type == 7
    ):
        await StellaCli.send_voice(
            chat_id=chat_id,
            voice=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 8
    ):
        await StellaCli.send_video(
            chat_id=chat_id,
            video=content,
            caption=text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        data_type == 9
    ):
        await StellaCli.send_video_note(
            chat_id=chat_id,
            video_note=content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    return 

#  Exceptions [400 BUTTON_URL_INVALID]: The button url is invalid (caused by "messages.SendMessage")
async def exceNoteMessageSender(message, note_name, from_chat_id=None):
    try:
        await SendNoteMessage(message, note_name, from_chat_id)
    except Exception as e:
        await message.reply(
            (
                "The notedata was incorrect, please update it. The buttons are most likely to be broken. If you are sure you aren't doing anything wrong and this was unexpected - please report it in my support chat.\n"
                f"**Error:** `{e}`"
            ),
            quote=True
        )

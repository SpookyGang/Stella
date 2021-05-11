from pyrogram.types import (
    Message,
    InlineKeyboardMarkup
)

from Stella import StellaCli
from Stella.helper.button_gen import button_markdown_parser
from Stella.helper.note_helper.note_fillings import NoteFillings

async def SendFilterMessage(message: Message, filter_name: str, content: str, text: str, data_type: int):
    
    chat_id = message.chat.id
    message_id = message.message_id
    text, buttons = button_markdown_parser(text)
    
    text = NoteFillings(message, text)
    # Check if button button len is Zero then reply_markup=None
    reply_markup = None
    if len(buttons) > 0:
        reply_markup = InlineKeyboardMarkup(buttons)
    else:
        reply_markup = None

    if data_type == 1:
        await StellaCli.send_message(
            chat_id=chat_id,
            text=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )

    elif data_type == 2:
        await StellaCli.send_sticker(
            chat_id=chat_id,
            sticker=content,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
        
    elif data_type ==3:
        await StellaCli.send_animation(
            chat_id=chat_id,
            animation=content,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )

    elif data_type == 4:
        await StellaCli.send_document(
            chat_id=chat_id,
            document=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )

    elif data_type == 5:
        await StellaCli.send_photo(
            chat_id=chat_id,
            photo=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
    
    elif data_type == 6:
        await StellaCli.send_audio(
            chat_id=chat_id,
            audio=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
    
    elif data_type == 7:
        await StellaCli.send_voice(
            chat_id=chat_id,
            voice=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
    
    elif data_type == 8:
        await StellaCli.send_video(
            chat_id=chat_id,
            video=content,
            caption=text,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
    
    elif data_type == 9:
        await StellaCli.send_video_note(
            chat_id=chat_id,
            video_note=content,
            reply_markup=reply_markup,
            reply_to_message_id=message_id
        )
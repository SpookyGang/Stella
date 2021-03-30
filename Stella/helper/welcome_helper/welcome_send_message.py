import pyrogram
from pyrogram.types import InlineKeyboardMarkup
from Stella import StellaCli
from Stella.helper.welcome_helper.welcome_fillings import Welcomefillings

async def SendWelcomeMessage(message, NewUserJson, Content, Text, DataType, reply_markup):
    message_id = message.message_id
    chat_id = message.chat.id
    Text = Welcomefillings(message, Text, NewUserJson)

    if (
        DataType == 'TEXT'
    ):
        SentMessage = await StellaCli.send_message(
            chat_id=chat_id,
            text=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        DataType == 'STICKER'
    ):
        SentMessage = await StellaCli.send_sticker(
            chat_id=chat_id,
            sticker=Content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        DataType == 'DOCUMENTS'
    ):
        
        SentMessage = await StellaCli.send_document(
            chat_id=chat_id,
            document=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )

    elif (
        DataType == 'PHOTO'
    ):
        SentMessage = await StellaCli.send_photo(
          chat_id=chat_id,
          photo=Content,
          caption=Text,
          reply_to_message_id=message_id,
          reply_markup=reply_markup
      )  
    
    elif (
        DataType == 'AUDIO'
    ):
        SentMessage = await StellaCli.send_audio(
            chat_id=chat_id,
            audio=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    elif (
        DataType == 'VOICE'
    ):
        SentMessage = await StellaCli.send_voice(
            chat_id=chat_id,
            voice=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        DataType == 'VIDEO'
    ):
        SentMessage = await StellaCli.send_video(
            chat_id=chat_id,
            video=Content,
            caption=Text,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    elif (
        DataType == 'VIDEO_NOTE'
    ):
        SentMessage = await StellaCli.send_video_note(
            chat_id=chat_id,
            video_note=Content,
            reply_to_message_id=message_id,
            reply_markup=reply_markup
        )
    
    return SentMessage
from enum import Enum, auto

class FilterMessageTypeMap(Enum):
    text = auto()
    sticker = auto()
    animation= auto()
    document = auto()
    photo = auto()
    audio = auto()
    voice = auto()
    video = auto()
    video_note = auto()

async def GetFIlterMessage(message):
    data_type = None
    content = None
    text = str()

    raw_text = message.text or message.caption
    args = raw_text.split(None, 2)
        
    if len(args) >= 3 and not message.reply_to_message:
        text = message.text.markdown[len(message.command[0]) + len(message.command[1]) + 4 :]
        data_type = FilterMessageTypeMap.text.value

    if (
        message.reply_to_message
        and message.reply_to_message.text
    ):
        if len(args) >= 2:
            text = message.reply_to_message.text.markdown
            data_type = FilterMessageTypeMap.text.value
            
    elif (
        message.reply_to_message
        and message.reply_to_message.sticker
    ):
        content = message.reply_to_message.sticker.file_id
        data_type = FilterMessageTypeMap.sticker.value
    
    elif (
        message.reply_to_message
        and message.reply_to_message.animation
    ):
        content = message.reply_to_message.animation.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown
        data_type = FilterMessageTypeMap.animation.value
        
    elif (
        message.reply_to_message
        and message.reply_to_message.document
    ):
        content = message.reply_to_message.document.file_id
        if message.reply_to_message.caption: 
            text = message.reply_to_message.caption.markdown 
        data_type = FilterMessageTypeMap.document.value

    elif (
        message.reply_to_message
        and message.reply_to_message.photo
    ):
        content = message.reply_to_message.photo.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown
        data_type = FilterMessageTypeMap.photo.value

    elif (
        message.reply_to_message
        and message.reply_to_message.audio
    ):
        content = message.reply_to_message.audio.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown 
        data_type = FilterMessageTypeMap.audio.value

    elif (
        message.reply_to_message
        and message.reply_to_message.voice
    ):
        content = message.reply_to_message.voice.file_id
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown
        data_type = FilterMessageTypeMap.voice.value

    elif (
        message.reply_to_message
        and message.reply_to_message.video
    ):
        content = message.reply_to_message.video.file_id 
        if message.reply_to_message.caption:
            text = message.reply_to_message.caption.markdown 
        data_type= FilterMessageTypeMap.video.value

    elif (
        message.reply_to_message
        and message.reply_to_message.video_note
    ):
        content = message.reply_to_message.video_note.file_id
        text = None 
        data_type = FilterMessageTypeMap.video_note.value

    return (
        content,
        text,
        data_type
    )
def GetWelcomeMessage(message):
    DataType = None
    Content = None
    Text = ''

    if not (
        message.reply_to_message
    ):
        Content = None
        Text = message.text.markdown[len(message.command[0]) + 2 :]
        DataType = 'TEXT'

    elif (
        message.reply_to_message
        and message.reply_to_message.text
    ):
        Content = None
        Text = message.reply_to_message.text.markdown 
        DataType = 'TEXT'

    elif (
        message.reply_to_message
        and message.reply_to_message.sticker
    ):
        Content = message.reply_to_message.sticker.file_id
        Text = None
        DataType = 'STICKER'

    elif (
        message.reply_to_message
        and message.reply_to_message.document
    ):
        Content = message.reply_to_message.document.file_id
        if message.reply_to_message.caption:
            Text = message.reply_to_message.caption.markdown 
        DataType = 'DOCUMENT'

    elif (
        message.reply_to_message
        and message.reply_to_message.photo
    ):
        Content = message.reply_to_message.photo.file_id
        if message.reply_to_message.caption:
            Text = message.reply_to_message.caption.markdown
        DataType = 'PHOTO'

    elif (
        message.reply_to_message
        and message.reply_to_message.audio
    ):
        Content = message.reply_to_message.audio.file_id
        if message.reply_to_message.caption:
            Text = message.reply_to_message.caption.markdown 
        DataType = 'AUDIO'

    elif (
        message.reply_to_message
        and message.reply_to_message.voice
    ):
        Content = message.reply_to_message.voice.file_id
        if message.reply_to_message.caption:
            Text = message.reply_to_message.caption.markdown 
        DataType = 'VOICE'

    elif (
        message.reply_to_message
        and message.reply_to_message.video
    ):
        Content = message.reply_to_message.video.file_id 
        if message.reply_to_message.caption:
            Text = message.reply_to_message.caption.markdown 
        DataType= 'VIDEO'

    elif (
        message.reply_to_message
        and message.reply_to_message.video_note
    ):
        Content = message.reply_to_message.video_note.file_id
        Text = None 
        DataType = 'VIDEO_NOTE'
    
    return (
        Content,
        Text,
        DataType
    )

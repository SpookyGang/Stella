def NoteFillings(message, message_text):
  if not message == None:
    user_id = message.from_user.id 
    first_name = message.from_user.first_name 
    last_name = message.from_user.last_name
    if last_name == None:
      last_name = ''
    full_name = f'{first_name} {last_name}'
    username = message.from_user.username
    mention = message.from_user.mention 
    chat_title = message.chat.title
    
    try:
      FillingText = message_text.format(
        id=user_id,
        first=first_name,
        fullname=full_name,
        username=username,
        mention=mention,
        chatname=chat_title
        ) 
    except KeyError:
      FillingText = message_text

  else:
    FillingText = message_text
  
  return FillingText
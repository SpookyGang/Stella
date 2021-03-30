import html

def Welcomefillings(message, message_text, NewUserJson):
  if not NewUserJson == None:
    user_id = NewUserJson.id 
    first_name = NewUserJson.first_name 
    last_name = NewUserJson.last_name
    if last_name == None:
      last_name = ''
    full_name = f'{first_name} {last_name}'
    username = NewUserJson.username
    mention = NewUserJson.mention 
    chat_title = html.escape(message.chat.title)
    
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
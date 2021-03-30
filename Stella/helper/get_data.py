from emojis import decode
from Stella import StellaCli
from Stella.database.users_mongo import GetChatName

async def GetChat(chat_id):
    if GetChatName(chat_id) is not None:
        chat_title = GetChatName(chat_id)
        return chat_title
    else:
        await StellaCli.send_message(
            chat_id=chat_id,
            text=(
                "I couldn't find the `{chat_title}` in my database. Please execute /forcecachechat here to make me be able to store your chat's data!"
            )
        )
        return

def get_text_reason(message):
    text = decode(message.text)
    index_finder = [x for x in range(len(text)) if text[x] == '"']
    if len(index_finder) >= 2:
        text = text[index_finder[0]+1: index_finder[1]]
        reason = text[:index_finder[1] + 2]
        if not reason:
            reason = None
    else:
        text = message.command[1]
        reason = ' '.join(message.command[2:])
        if not reason:
            reason = None
    
    return (
        text,
        reason
        )
import re 

from Stella.helper.chat_status import isUserAdmin
from Stella.database.blocklists_mongo import get_blocklist
from Stella.plugins.blocklists.checker import blocklist_action

async def blocklist_checker(message):
    chat_id = message.chat.id 

    if await isUserAdmin(message, silent=True):
        return
    
    BLOCKLIST_DATA = get_blocklist(chat_id)
    if (
        BLOCKLIST_DATA is None
        or len(BLOCKLIST_DATA) == 0
    ):
        return

    BLOCKLIST_ITMES = []
    for blocklist_array in BLOCKLIST_DATA:
        BLOCKLIST_ITMES.append(blocklist_array['blocklist_text'])

    message_text = extract_text(message)

    for blitmes in BLOCKLIST_ITMES:
        if '*' in blitmes:
            star_position = blitmes.index('*')
            if blitmes[star_position-1] == '/':
                block_char = blitmes[:star_position]
                URLS = extact_url(message_text)
                for url in URLS:    
                    if block_char in url:
                        await blocklist_action(message, f'{block_char}*')
                        return
            
            elif (
                len(blitmes) > len(blitmes)
                and blitmes[star_position+1] == '.'
            ):
                if (
                    message.document
                    or message.animation
                ):
                    extensions = blitmes[star_position+1:]
                    file_name = None
                    if message.document:
                        file_name = message.document.file_name
                    elif message.animation:
                        file_name = message.animation.file_name  
                    if file_name.endswith(extensions):
                        await blocklist_action(message, f'*{extensions}')
                        return
        else:
            if message_text is not None:
                pattern = r"( |^|[^\w])" + re.escape(blitmes) + r"( |$|[^\w])"
                if re.search(pattern, message_text, flags=re.IGNORECASE):
                    await blocklist_action(message, blitmes)
                    return

def extract_text(message) -> str:
    return (
        message.text
        or message.caption
        or (message.sticker.emoji if message.sticker else None)
    )

def extact_url(message_text):
  
    # findall() has been used 
    # with valid conditions for urls in message_text
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, message_text)      
    return [x[0] for x in url] 
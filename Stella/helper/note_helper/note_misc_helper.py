from pyrogram.types import Message
from Stella.helper.chat_status import isUserAdmin

async def privateNote_and_admin_checker(message, text: str):
    privateNote = True
    if '{noprivate}' in text:
        privateNote = False 
    elif '{private}' in text:
        privateNote = True 
    else:
        privateNote = None

    allow = True
    if '{admin}' in text:
        if not await isUserAdmin(message, silent=True):
            allow = False 
        else:
            allow = True 
    
    return (
        privateNote,
        allow
    )

def preview_text_replace(text):
        if '{preview}' in text:
            text = text.replace('{preview}', '')
            preview =  False
        else:
            preview = True
        
        if '{admin}' in text:
            text = text.replace('{admin}', '')
        
        if '{private}' in text:
            text = text.replace('{private}', '')
        elif '{noprivate}' in text:
            text = text.replace('{noprivate}', '')
        
        return (
            preview, text
        )
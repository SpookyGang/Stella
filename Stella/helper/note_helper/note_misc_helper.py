from Stella.helper.chat_status import isUserAdmin

async def private_note_and_admin_checker(message, Text):
    PRIVATE_NOTE = True
    if (
        '{noprivate}' in Text
    ):
        PRIVATE_NOTE = False 

    elif (
        '{private}' in Text
    ):
        PRIVATE_NOTE = True 

    else:
        PRIVATE_NOTE = None

    ALLOW = True
    if (
        '{admin}' in Text
    ):
        if not await isUserAdmin(message, silent=True):
            ALLOW = False 
        else:
            ALLOW = True 
    
    return (
        PRIVATE_NOTE,
        ALLOW
    )

def preview_text_replace(Text):
        if '{preview}' in Text:
            Text = Text.replace('{preview}', '')
            preview =  False
        else:
            preview = True
        
        if '{admin}' in Text:
            Text = Text.replace('{admin}', '')
        
        if '{private}' in Text:
            Text = Text.replace('{private}', '')
        elif '{noprivate}' in Text:
            Text = Text.replace('{noprivate}', '')
        
        return (
            preview, Text
        )
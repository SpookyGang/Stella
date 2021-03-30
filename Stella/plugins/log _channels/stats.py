from Stella import StellaDB

log_channels  = StellaDB.log_channels 

def __stats__():
    TOTAL_CONNECTED_CHATS = log_channels.count_documents({})
    text = (
        f'`{TOTAL_CONNECTED_CHATS}` chats are setted their logs channels.\n'
    )
    return text
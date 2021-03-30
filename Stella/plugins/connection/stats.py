from Stella import StellaDB

connection  = StellaDB.connection 

def __stats__():
    TOTAL_CONNECTED_CHATS = connection.count_documents({})
    text = (
        f'`{TOTAL_CONNECTED_CHATS}` users are currently connected to theire chats.\n'
    )
    return text
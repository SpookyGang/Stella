from Stella import StellaDB

disable = StellaDB.disable

def __stats__():
    disable_data = disable.find()
    DISABLED_ITEMS = []
    TOTAL_DISABLE_CHATS = disable.count_documents({})

    for chat in disable_data:
        DISABLED_ITEMS.append(
            len(chat['disabled_items'])
        )
    
    text = (
        f"`{sum(DISABLED_ITEMS)}` disabled items, across `{TOTAL_DISABLE_CHATS}` chats.\n"
    )
    return text
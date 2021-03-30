from Stella import StellaDB

welcome = StellaDB.welcome 

def __stats__():
    TOTAL_WELCOME_CHATS = welcome.count_documents({})
    text = (
        f'owo, I\'m welcoming in `{TOTAL_WELCOME_CHATS}` chats.\n'
    )

    return text


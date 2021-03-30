from Stella import StellaDB

warnings = StellaDB.warnings

def __stats__():
    TOTAL_WARNINGS = []
    TOTAL_WARNED_USER = []
    TOTAL_CHATS = warnings.count_documents({})

    warning_data = warnings.find({})
    for chat_data in warning_data:
        warns = chat_data['warns']
        TOTAL_WARNED_USER.append(len(warns))
        for warn in warns:
            len_of_warn = len(warn['user_warns'])
            TOTAL_WARNINGS.append(len_of_warn)
    text = (
        f"Erm, they've received `{sum(TOTAL_WARNINGS)}` warnings by me- including total of `{sum(TOTAL_WARNED_USER)}` bad people (__idk for sure if they're bad tho but that's that heh__) in `{TOTAL_CHATS}` chats :p"
    )
    return text
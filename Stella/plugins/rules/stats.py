from Stella import StellaDB

rules = StellaDB.rules

def __stats__():
    TOTAL_RULE_CHATS = rules.count_documents({})
    text = (
        f"`{TOTAL_RULE_CHATS}` rules are setted in chats.\n"
    )
    return text
        
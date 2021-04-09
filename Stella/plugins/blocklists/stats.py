from Stella import StellaDB

blocklists = StellaDB.blocklists

def __stats__():
    TOTAL_BLOCKLIST = []
    blocklists_data = blocklists.find()
    TOTAL_BLOCKLIST_CHATS = blocklists.count_documents({})
    for chats_data in blocklists_data:
        blocklist_text_len = len(chats_data['blocklist_text'])
        TOTAL_BLOCKLIST.append(blocklist_text_len)

    text = (
        f"`{sum(TOTAL_BLOCKLIST)}` blocklisted words in `{TOTAL_BLOCKLIST_CHATS}` chats.\n"
    )
    return text
        
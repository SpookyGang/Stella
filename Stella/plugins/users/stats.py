import datetime
from Stella import StellaDB

users = StellaDB.users
chats = StellaDB.chats

def __stats__():
    NUM_CHATS = chats.count_documents({})
    NUM_USERS = users.count_documents({})
    CHATS24HR = chats.count_documents({'first_found_date': {'$gte': datetime.datetime.now() - datetime.timedelta(days=1)}})
    USER24HR = users.count_documents({'first_found_date': {"$gte": datetime.datetime.now() - datetime.timedelta(days=1)}})
    
    text = (
        f"I've seen `{NUM_USERS}` users in total and have joined `{NUM_CHATS}` chats.\n"
        f"- Eto~ I saw `{USER24HR}`  users and `{CHATS24HR}` chats in the last 24 hours, heh.\n"
    )
    return text
from Stella import StellaDB

chats = StellaDB.chats

def anonadmin_db(chat_id, arg):
    chat_data = chats.find_one(
        {
            'chat_id': chat_id
        }
    )

    ChatsNums = chats.count_documents({})
    ChatsIDs = ChatsNums + 1

    if chat_data is None:
        chats.insert_one(
            {
                '_id': ChatsIDs,
                'chat_id': chat_id,
                'chat_title': None,
                'anon_admin': arg
            }
        )
    else:
        chats.update_one(
            {
                'chat_id': chat_id
            },
            {
                "$set": {
                    'anon_admin': arg
                }
            },
            upsert=True
        )

def get_anon_setting(chat_id) -> bool:
    chat_data = chats.find_one(
        {
            'chat_id': chat_id
        }
    )

    if chat_data is not None:
        if 'anon_admin' in chat_data:
            return chat_data['anon_admin']
        else:
            return False
    else:
        return False
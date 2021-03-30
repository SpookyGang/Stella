import datetime 
from Stella import StellaDB

users = StellaDB.users
chats = StellaDB.chats

first_found_date = datetime.datetime.now()

def add_user(user_id, username=None, chat_id=None, chat_title=None, Forwared=False):
    
    UserData = users.find_one(
        {
            'user_id': user_id
        }
    )

    if UserData == None:
        UsersNums = users.count_documents({})
        UsersIDs = UsersNums + 1
        
        if Forwared:
            UsersData = {
                '_id': UsersIDs,
                'user_id': user_id,
                'username': username,
                'chats': [],
                'first_found_date': first_found_date
                }
        else:
            UsersData = {
                '_id': UsersIDs,
                'user_id': user_id,
                'username': username,
                'chats': [
                    {   '_id': 1,
                        'chat_id': chat_id,
                        'chat_title': chat_title
                    }
                ],
                'first_found_date': first_found_date
                }


        users.insert_one(
            UsersData
        )

    else:
        if username != UserData['username']:
            users.update_one(
                {
                    'user_id': user_id
                },
                {
                    "$set": {
                        'username': username
                    }
                },
                upsert=True
            )

        GetUserChatList = []
        UsersChats = UserData['chats']

        if len(UsersChats) == 0:
            return

        for UserChat in UsersChats:
            GetUserChat = UserChat.get('chat_id')
            GetUserChatList.append(GetUserChat)

        ChatsIDs = len(GetUserChatList) + 1
        if not chat_id in GetUserChatList:
            users.update(
                {
                    'user_id': user_id
                },
                {
                '$push': {
                    'chats': {
                        '_id': ChatsIDs,
                        'chat_id': chat_id,
                        'chat_title': chat_title
                            }
                        }
                }

            )
    

def add_chat(chat_id, chat_title):
    ChatData = chats.find_one(
        {
            'chat_id': chat_id
        }
    )

    if ChatData == None:
        ChatsNums = chats.count_documents({})
        ChatsIDs = ChatsNums + 1

        ChatData = {
            '_id': ChatsIDs,
            'chat_id': chat_id,
            'chat_title': chat_title,
            'first_found_date': first_found_date
            }
        
        chats.insert_one(
            ChatData
        )
    else:
        chats.update_one(
            {
                'chat_id': chat_id
            },
            {
                "$set": {
                    'chat_id': chat_id,
                    'chat_title': chat_title
                }
            },
            upsert=True
        )

def GetAllChats() -> list:
    CHATS_LIST = []
    chatsList = chats.find({})
    for chatData in chatsList:
        chat_id = chatData['chat_id']
        CHATS_LIST.append(chat_id)
    return CHATS_LIST
    

def GetChatName(chat_id):
    ChatData = chats.find_one(
        {
            'chat_id': chat_id
        }
    )
    if ChatData is not None:
        chat_title = ChatData['chat_title']
        return chat_title
    else:
        return None 
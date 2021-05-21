#    Stella (Development)
#    Copyright (C) 2021 - meanii (Anil Chauhan)
#    Copyright (C) 2021 - SpookyGang (Neel Verma, Anil Chauhan)

#    This program is free software; you can redistribute it and/or modify 
#    it under the terms of the GNU General Public License as published by 
#    the Free Software Foundation; either version 3 of the License, or 
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import datetime 
from Stella import StellaDB

connection = StellaDB.connection 
chats = StellaDB.chats 

first_found_date = datetime.datetime.now()

def connectDB(user_id, chat_id):
    connectionData = connection.find_one(
        {
            'user_id': user_id
        }
    )
    totalConnections = connection.count_documents({})
    NumofConnections = totalConnections + 1
    
    if connectionData is None:
        connection.insert_one(
            {
                '_id': NumofConnections,
                'user_id': user_id,
                'connection': True,
                'connected_chat': int(chat_id)
            }
        )
    else:
        connection.update_one(
            {
                'user_id': user_id
            },
            {   
                "$set": {
                    'connection': True,
                    'connected_chat': int(chat_id)
                }
            },
            upsert=True
        )

def GetConnectedChat(user_id):
    connectionData = connection.find_one(
        {
            'user_id': user_id
        }
    )
    if connectionData is not None:
        chat_id = connectionData['connected_chat']
        return chat_id 
    else:
        return None

def isChatConnected(user_id) -> bool:
    connectionData = connection.find_one(
        {
            'user_id': user_id
        }
    )
    if connectionData is not None:
        return connectionData['connection']
    else:
        return False

def disconnectChat(user_id):
    connection.update_one(
        {
            'user_id': user_id
        },
        {
            "$set": {
                'connection': False
            }
        }
    )

def reconnectChat(user_id):
    connection.update_one(
        {
            'user_id': user_id
        },
        {
            "$set": {
                'connection': True
            }
        }
    )

def allow_collection(chat_id, chat_title, allow_collection):
    chat_data = chats.find_one(
        {
            'chat_id': chat_id
        }
    )
    if chat_data == None:
        ChatsNums = chats.count_documents({})
        ChatsIDs = ChatsNums + 1

        ChatData = {
            '_id': ChatsIDs,
            'chat_id': chat_id,
            'chat_title': chat_title,
            'first_found_date': first_found_date,
            'allow_collection': allow_collection
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
                    'allow_collection': allow_collection
                }
            },
            upsert=True
        )

def get_allow_connection(chat_id)-> bool:
    chat_data = chats.find_one(
        {
            'chat_id': chat_id
        }
    )
    if chat_data is not None:
        if 'allow_collection' in chat_data:
            return chat_data['allow_collection']
        else:
            return False
    return False
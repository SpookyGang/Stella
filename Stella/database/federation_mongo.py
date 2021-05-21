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


from Stella import StellaDB

federation = StellaDB.federation

def new_fed_db(new_fed, fed_id, created_time, owner_id):
    GetFed = federation.find_one(
        {
            'owner_id': owner_id
        }
    )

    if GetFed == None:
        FedNums = federation.count_documents({})
        FedIDs = FedNums + 1
        federation.insert_one(
            {
                '_id': FedIDs,
                'fed_id': fed_id,
                'fed_name': new_fed,
                'owner_id': owner_id,
                'created_time': created_time
            }
        )

def is_fed_exist(fed_id=None, owner_id=None) -> bool:
    if fed_id == None:
        GetFed = federation.find_one(
            {
                'owner_id': owner_id
            }
        )

        if GetFed is not None:
            return True 
        else:
            return False 
    
    else:
        GetFed = federation.find_one(
            {
                'fed_id': fed_id
            }
        )
        if GetFed is not None:
            return True 
        else:
            return False 

def join_fed_db(chat_id, chat_title, fed_id):
    federation.update_one(
        {
            'fed_id': fed_id
        },
        {
            "$addToSet": {
                'chats': {
                    "$each": [
                        {
                            'chat_id': chat_id  ,
                            'chat_title': chat_title
                        }
                    ]
                }
            }
        }
    )

def user_fban(fed_id, user_id, reason):
    federation.update(
        {
            'fed_id': fed_id
        },
        {
            "$set": {
                'banned_users': [
                    {
                        'user_id': user_id,
                        'reason': reason
                    }
                ]
            }
        }
    )

def user_unfban(fed_id, user_id):
    federation.update(
        {
            'fed_id': fed_id,
            'banned_users.user_id': user_id
        },
        {
            "$pull": {
                'banned_users': {
                    'user_id': user_id
                }
            }
        }
    )
    
def is_user_fban(fed_id, user_id) -> bool:
    GetFed = federation.find_one(
        {
            'fed_id': fed_id
        }
    )

    user_ids_list = []
    if not GetFed == GetFed:
        if 'banned_users' in GetFed:
            for users in GetFed['banned_users']:
                banned_user = users['user_id']
                user_ids_list.append(banned_user)
            if user_id in user_ids_list:
                return True 
            else:
                return False 
        else:
            return False 
    else:
        return False 

def update_reason(fed_id, user_id, new_reason):
    federation.update_one(
        {
            'fed_id': fed_id,
            'banned_users.user_id': user_id
        },
        {
            "$set": {
                'banned_users.$.reason': new_reason
            }
        },
        False,
        True
    )

def get_fed_from_chat(chat_id):
    for fedData in federation.find(
        {
            'chats': {
                "$elemMatch": {
                    'chat_id': chat_id
                }
            }
        }
    ):  
        if 'fed_id' in fedData:
            fed_id = fedData['fed_id']
            return fed_id
        else:
            return None

def get_fed_from_ownerid(owner_id):
    fedData = federation.find_one(
        {
            'owner_id': owner_id
        }
    )   
    if not fedData == None:
        fed_id = fedData['fed_id']
        return fed_id
    else:
        return None

def get_fed_reason(fed_id, user_id):
    fedData = federation.find_one(
        {
            'fed_id': fed_id
        }
    )   
    
    for user in fedData['banned_users']:
        banned_user = user['user_id']
        reason = user['reason']
        if user_id == banned_user:
            return reason

def get_connected_chats(fed_id) -> list:
    fedData = federation.find_one(
        {
            'fed_id': fed_id
        }
    )
    connected_chats = []
    if 'chats' in fedData:
        for chats in fedData['chats']:
            chat_id = chats['chat_id']
            connected_chats.append(chat_id)
        return connected_chats
    else:
        return None

def get_fed_name(fed_id=None, owner_id=None):
    if fed_id == None:
        GetFed = federation.find_one(
            {
                'owner_id': owner_id
            }
        )

        if GetFed is not None:
            fed_name = GetFed['fed_name']
            return fed_name
    
    else:
        GetFed = federation.find_one(
            {
                'fed_id': fed_id
            }
        )
        if GetFed is not None:
            fed_name = GetFed['fed_name']
            return fed_name
        
def is_fed_creator(fed_id, owner_id) -> bool:
    GetFed = federation.find_one(
        {
            'fed_id': fed_id
        }
    )

    if (
        owner_id == GetFed['owner_id']
    ):
        return True 
    else:
        return False

def fed_rename_db(owner_id, fed_name):
    federation.update_one(
        {
            'owner_id': owner_id
        },
        {
            "$set": {
                'fed_name': fed_name
            }
        },
        False,
        True
    )

def get_fed_owner(fed_id):
    GetFed = federation.find_one(
        {
            'fed_id': fed_id
        }
    )
    owner_id = GetFed['owner_id']
    return owner_id

def fed_promote(fed_id, user_id):
    federation.update_one(
        {
            'fed_id': fed_id
        },
        {
            "$addToSet": {
                'Admins': {
                    "$each": [
                        user_id
                    ]
                }
            }
        }
    )

def get_fed_admins(fed_id) -> list:
    GetFed = federation.find_one(
        {
            'fed_id': fed_id
        }
    )
    FedAdmins = []
    if 'admins' in GetFed:
        for admins in GetFed['admins']:
            FedAdmins.append(admins)
    owner_id = get_fed_owner(fed_id)
    FedAdmins.append(owner_id)

    return FedAdmins

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
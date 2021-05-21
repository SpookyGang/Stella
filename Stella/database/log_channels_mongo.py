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

log_channels = StellaDB.log_channels

def set_log_db(chat_id, channel_id, channel_title):
    get_data = log_channels.find_one(
        {
            'chat_id': chat_id
        }
    )

    total_logs = log_channels.count_documents({})
    NumofLogs = total_logs + 1

    if get_data is None:
        log_channels.insert_one(
            {
                '_id': NumofLogs,
                'chat_id': chat_id,
                'channel_id': channel_id,
                'channel_title': channel_title,
                'categories': {
                    'settings': True,
                    'admin': True, 
                    'user': True,
                    'automated': True,
                    'reports': True,
                    'other': True
                }
            }
        )
    else:
        log_channels.update_one(
            {
                'chat_id': chat_id
            },
            {
                "$set": {
                    'channel_id': channel_id,
                    'categories': {
                        'settings': True,
                        'admin': True, 
                        'user': True,
                        'automated': True,
                        'reports': True,
                        'other': True
                    }   
                }
            },
            upsert=True
        )
    
def unset_log_db(chat_id):
    get_data = log_channels.find_one(
        {
            'chat_id': chat_id
        }
    )

    if get_data is not None:
        log_channels.delete_one(
            {
                'chat_id': chat_id
            }
        )

def get_set_channel(chat_id):
    get_data = log_channels.find_one(
        {
            'chat_id': chat_id
        }
    )

    if get_data is not None:
        channel_title = get_data['channel_title']
        return channel_title
    else:
        return None
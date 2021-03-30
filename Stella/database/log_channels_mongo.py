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
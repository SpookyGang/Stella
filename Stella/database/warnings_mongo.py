from Stella import StellaDB

warnings = StellaDB.warnings

def warn_db(chat_id, admin_id, user_id, reason):
    warn_data = warnings.find_one(
        {
            'chat_id': chat_id
        }
    )

    _id = warnings.count_documents({}) + 1
    if warn_data is None:
        warnings.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'warn_limit': 3,
                'warn_mode': {
                    'warn_mode': 1,
                    'warn_time': None
                },
                'warns': [
                    {
                        'user_id': user_id,
                        'user_warns': [
                            {
                                'warn_id': 1,
                                'reason': reason,
                                'admin_id': admin_id
                            }
                        ]
                    }
                ]
            }
        )
    else:

        # warn count 
        warn_count = 1
        user_list = warn_data['warns']
        for user in user_list:
            if user_id == user['user_id']:
                warn_count = len(user['user_warns']) + 1
            
        warn_user_data = warnings.find_one(
            {
                'chat_id': chat_id,
                'warns': {
                    '$elemMatch': {
                        'user_id': user_id
                    }
                }
            }
        )
        if warn_user_data is not None:
            warnings.update_one(
                {
                    'chat_id': chat_id,
                    'warns.user_id': user_id
                },
                {
                    '$push': {
                        'warns.$.user_warns': {
                            'warn_id': warn_count,
                            'reason': reason,
                            'admin_id': admin_id
                        }
                    }
                }
            )
        else:
            warnings.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    '$push': {
                        'warns': {
                            'user_id': user_id,
                            'user_warns': [
                                {
                                    'warn_id': 1,
                                    'reason': reason,
                                    'admin_id': admin_id
                                }
                            ]
                        }
                    }
                },
                upsert=True
            )


def warn_limit(chat_id):
    warn_data = warnings.find_one(
        {
            'chat_id': chat_id
        }
    )

    if warn_data is not None:
        _warn_limit = warn_data['warn_limit']
        return _warn_limit
    else:
        return 3

def count_user_warn(chat_id, user_id):
    warn_data = warnings.find_one(
        {
            'chat_id': chat_id
        }
    )

    if warn_data is not None:
        user_list = warn_data['warns']
        for user in user_list:
            if user_id == user['user_id']:
                warn_count = len(user['user_warns'])
                return warn_count
        
def remove_warn(chat_id, user_id, warn_id):
    warnings.update(
        {
            'chat_id': chat_id,
            'warns.user_id': user_id,
            'warns.user_warns.warn_id': warn_id
        },
        {
            '$pull': {
                'warns.$.user_warns': {
                    'warn_id': warn_id
                }
            }
        }
    )
        

def set_warn_mode_db(chat_id, warn_mode, time=None):
    warn_data = warnings.find_one(
        {
            'chat_id': chat_id
        }
    )

    if warn_data is None:
        warnings.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'warn_limit': 3,
                'warn_mode': {
                    'warn_mode': warn_mode,
                    'warn_time': time
                },
                'warns': []
            }
        )
    else:
        warnings.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'warn_mode.warn_mode': warn_mode,
                    'warn_mode.warn_time': time
                }
            },
            upsert=True
        )

def get_warn_mode(chat_id):
    warn_data = warnings.find_one(
        {
            'chat_id': chat_id
        }
    )

    if warn_data is not None:
        warn_mode_data = warn_data['warn_mode']
        warn_mode = warn_mode_data['warn_mode']
        warn_mode_time = warn_mode_data['warn_time']
        return (
            warn_mode,
            warn_mode_time
        )
    else:
        warn_mode = 1
        warn_mode_time = None 

        return (
            warn_mode,
            warn_mode_time
        )

def get_all_warn_reason(chat_id, user_id) -> list:
    warn_data = warnings.find_one(
        {
            'chat_id': chat_id
        }
    )
    REASONS = []
    if warn_data is not None:
        warns = warn_data['warns']
        for data_user_id in warns:
            if data_user_id['user_id'] == user_id:
                user_warns = data_user_id['user_warns']
                for reason_data in user_warns:
                    warn_id = reason_data['warn_id']
                    reason = reason_data['reason']
                    if reason is None:
                        reason = 'Reason wasn\'t given'
                    reason_text = f'{warn_id}: {reason}\n'
                    REASONS.append(reason_text)
                return REASONS

def reset_user_warns(chat_id, user_id):
    warnings.update_one(
        {
            'chat_id': chat_id,
            'warns.user_id': user_id
        },
        {
            '$pull': {
                'warns': {
                    'user_id': user_id
                }
            }
        }
    )

def reset_all_warns_db(chat_id):
    warnings.update_one(
        {
            'chat_id': chat_id
        },
        {
            '$set': {
                'warns': []
            }
        }
    )

def set_warn_limit_db(chat_id, warn_limit):
    warn_data = warnings.find_one(
        {
            'chat_id': chat_id
        }
    )

    if warn_data is not None:
        warnings.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'warn_limit': warn_limit
                }
            },
            upsert=True
        )
    else:
        _id = warnings.count_documents({}) + 1
        warnings.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'warn_limit': warn_limit,
                'warn_mode': {
                    'warn_mode': 1,
                    'warn_time': None
                },
                'warns': []
            }
        )

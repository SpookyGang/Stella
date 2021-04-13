from Stella import StellaDB

locks = StellaDB.locks

def lock_db(chat_id, lock_item):
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )

    if locks_data is None:
        _id = locks.count_documents({}) + 1
        locks.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'locked': [lock_item],
                'lockwarns': True,
                'allow_list': []
            }
        )
    else:
        locks.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$addToSet': {
                    'locked': lock_item
                }
            }
        )

def get_locks(chat_id) -> list:
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )

    if locks_data is not None:
        return locks_data['locked']
    else:
        return []

def unlock_db(chat_id, locked_item):
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )
    if locks_data is not None:
        locks.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$pull': {
                    'locked': locked_item
                }
            }
        )

def lockwarns_db(chat_id) -> bool:
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )

    if locks_data is not None:
        return locks_data['lockwarns']
    else:
        return True

def set_lockwarn_db(chat_id, warn_args):
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )
    if locks_data is not None:
        locks.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'lockwarns': warn_args
                },
            },
            upsert=True
        )
    else:
        _id = locks.count_documents({}) + 1
        locks.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'locked': [],
                'lockwarns': warn_args,
                'allow_list': []
            }
        )

def allowlist_db(chat_id, allowlist_arg):
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )
    if locks_data is not None:
        locks.update(
            {
                'chat_id': chat_id
            },
            {
                '$addToSet': {
                    'allow_list': allowlist_arg
                }
            }
        )
    else:
        _id = lock.count_documents({}) + 1
        locks.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'locked': [],
                'lockwarns': True,
                'allow_list': [allowlist_arg]
            }
        )

def rmallow_db(chat_id, allow_arg):
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )
    if locks_data is not None:
        locks.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$pull': {
                    'allow_list': allow_arg
                }
            },
            upsert=True
        )

def rmallowall_db(chat_id):
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )
    if locks_data is not None:
        locks.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'allow_list': []
                }
            },
            upsert=True
        )

def get_allowlist(chat_id) -> list:
    locks_data = locks.find_one(
        {
            'chat_id': chat_id
        }
    )
    if locks_data is not None:
        return locks_data['allow_list']
    else:
        return []
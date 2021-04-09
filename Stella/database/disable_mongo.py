from Stella import StellaDB

disable = StellaDB.disable

def disable_db(chat_id, disable_arg):
    disable_data = disable.find_one(
        {
            'chat_id': chat_id
        }
    )
    if disable_data is None:
        _id = disable.count_documents({}) + 1

        disable.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'disabled_items': [disable_arg],
                'disabledel': False
            }
        )
    else:
        disabled_list = get_disabled(chat_id)
        if disable_arg not in disabled_list:
            disable.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    '$push': {
                        'disabled_items': disable_arg
                    }
                },
                upsert=True
            )

def enable_db(chat_id, enable_arg):
    disable_data = disable.find_one(
        {
            'chat_id': chat_id
        }
    )
    if disable_data is not None:
        disabled_list = get_disabled(chat_id)
        if enable_arg in disabled_list:
            disable.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    '$pull': {
                        'disabled_items': enable_arg
                    }
                },
                upsert=True
            )

def get_disabled(chat_id) -> list:
    disable_data = disable.find_one(
        {
            'chat_id': chat_id
        }
    )

    if disable_data is not None:
        return disable_data['disabled_items']
    else:
        return []

def disabledel_db(chat_id, disabledel):
    disable_data = disable.find_one(
        {
            'chat_id': chat_id
        }
    )
    if disable_data is not None:
        disable.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'disabledel': disabledel
                }
            },
            upsert=True
        )
    else:
        _id = disable.count_documents({}) + 1
        disable.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'disabled_items': [],
                'disabledel': disabledel
            }
        )

def get_disabledel(chat_id) -> bool:
    disable_data = disable.find_one(
        {
            'chat_id': chat_id
        }
    )
    if disable_data is not None:
        return disable_data['disabledel']
    else:
        return False
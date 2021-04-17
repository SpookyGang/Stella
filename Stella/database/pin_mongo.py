from Stella import StellaDB

pin = StellaDB.pin

def cleanlinked_db(chat_id: int, cleanlinked: bool) -> None:
    pin_data = pin.find_one(
        {
            'chat_id': chat_id
        }
    )

    if pin_data is None:
        _id = pin.count_documents({}) + 1
        pin.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'cleanlinked': cleanlinked,
                'antichannelpin': None
            }
        )
    else:
        pin.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'cleanlinked': cleanlinked
                }
            },
            upsert=True
        )

def get_cleanlinked(chat_id: int) -> bool:
    pin_data = pin.find_one(
        {
            'chat_id': chat_id
        }
    )

    if pin_data is not None:
        return pin_data['cleanlinked']
    else:
        return False

def antichannelpin_db(chat_id: int, antichannelpin: bool) -> None:
    pin_data = pin.find_one(
        {
            'chat_id': chat_id
        }
    )
    if pin_data is None:
        _id = pin.count_documents({}) + 1
        pin.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'cleanlinked': False,
                'antichannelpin': antichannelpin
            }
        )
    else:
        pin.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'antichannelpin': antichannelpin
                }
            },
            upsert=True
        )

def get_antichannelpin(chat_id: int) -> bool:
    pin_data = pin.find_one(
        {
            'chat_id': chat_id
        }
    )
    if pin_data is not None:
        return pin_data['antichannelpin']
    else:
        return False

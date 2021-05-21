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
        disable.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$addToSet': {
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
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


from typing import Union
from Stella import StellaDB

antiflood = StellaDB.antiflood

def setflood_db(chat_id: int, flood_arg: Union[int, bool]):
    antiflood_data = antiflood.find_one(
        {
            'chat_id': chat_id
        }
    )

    if antiflood_data is None:
        _id = antiflood.count_documents({}) + 1
        
        if type(flood_arg) == int:
            flood_limit = flood_arg
            flood =  True
        elif type(flood_arg) == bool:
            flood_limit = 4
            flood = flood_arg
        antiflood.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'flood_limit': flood_limit,
                'flood': flood,
                'flood_mode': {
                    'flood_mode': 1,
                    'until_time': None
                }
            }
        )
    else:
        if isinstance(flood_arg, int):
            set_key = {
                'flood_limit': flood_arg,
                'flood': True
            }
        elif isinstance(flood_arg, bool):
            set_key = {
                'flood': flood_arg
            }

        antiflood.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': set_key
            },
            upsert=True
        )

def get_floodlimit(chat_id: int) -> int:
    antiflood_data = antiflood.find_one(
        {
            'chat_id': chat_id
        }
    )

    if antiflood_data is not None:
        return antiflood_data['flood_limit']

def get_flood(chat_id: int) -> bool:
    antiflood_data = antiflood.find_one(
        {
            'chat_id': chat_id
        }
    )
    if antiflood_data is not None:
        return antiflood_data['flood']
    else:
        return False

def set_antiflood_mode(chat_id, flood_mode, until_time=None):
    antiflood_data = antiflood.find_one(
        {
            'chat_id': chat_id
        }
    )
    if antiflood_data is not None:
        antiflood.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'flood_mode': {
                        'flood_mode': flood_mode,
                        'until_time': until_time
                    }
                }
            },
            upsert=True
        )
    else:
        _id = antiflood.count_documents({}) + 1
        antiflood.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'flood_limit': 4,
                'flood': False,
                'flood_mode': {
                    'flood_mode': flood_mode,
                    'until_time': until_time
                }
            }
        )

def get_antiflood_mode(chat_id):
    antiflood_data = antiflood.find_one(
        {
            'chat_id': chat_id
        }
    )
    if antiflood_data is not None:
        FloodMode = antiflood_data['flood_mode']['flood_mode']
        Flood_until_time = antiflood_data['flood_mode']['until_time']
        return (
            FloodMode,
            Flood_until_time
        )
    else:
        FloodMode = 1
        Flood_until_time = None
        return (
            FloodMode,
            Flood_until_time
        )
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

blocklists = StellaDB.blocklists

def add_blocklist_db(chat_id, blocklist_text, blocklist_reason):
    blocklist_data =  blocklists.find_one(
        {
            'chat_id': chat_id
        }
    )

    _id = blocklists.count_documents({}) + 1
    if blocklist_data is None:
        blocklists.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'blocklist_text': [
                    {
                        'blocklist_text': blocklist_text,
                        'blocklist_reason': blocklist_reason
                    }
                ],
                'blocklist_mode': {
                    'blocklist_mode': 1,
                    'blocklist_time': None,
                    'blocklist_default_reason': None 
                },
                'blocklistdelete': True,
                'blocklist_default_reason': None
            }
        )
    else:
        BLOCKLIST_LIST = blocklist_data['blocklist_text']
        BLOCKLIST_TEXT_LIST = []
        BLOCKLIST_REASON_LIST = []
        for blacklist_obj in BLOCKLIST_LIST:
            BLOCKLIST_TEXT_LIST.append(blacklist_obj['blocklist_text'] )
            BLOCKLIST_REASON_LIST.append(blacklist_obj['blocklist_reason'])
            
        if blocklist_text not in BLOCKLIST_TEXT_LIST:
            blocklists.update_one(
                {
                    'chat_id': chat_id
                },
                {
                    '$push': {
                        'blocklist_text': {
                                'blocklist_text': blocklist_text,
                                'blocklist_reason': blocklist_reason
                            }
                    }
                },
                upsert=True
            )
        
        for reason_list in BLOCKLIST_LIST:
            text = reason_list['blocklist_text']
            reason = reason_list['blocklist_reason']
            if text == blocklist_text:
                if reason != blocklist_reason:
                    blocklists.update_one(
                        {
                            'chat_id': chat_id,
                            'blocklist_text.blocklist_text': blocklist_text
                        },
                        {
                            '$set': {
                                'blocklist_text.$.blocklist_reason': blocklist_reason
                                }
                        },
                        upsert=True
                    )

def rmblocklist_db(chat_id, blocklist_name):
    blocklist_data = blocklists.find_one(
        {
            'chat_id': chat_id
        }
    )

    if blocklist_data is not None:
        blocklists.update_one(
            {
                'chat_id': chat_id,
                'blocklist_text.blocklist_text': blocklist_name
            },
            {
                '$pull': {
                    'blocklist_text': {
                        'blocklist_text': blocklist_name
                    }
                }
            }
        )

def unblocklistall_db(chat_id):
    blocklists.update_one(
        {
            'chat_id': chat_id
        },
        {
            '$set': {
                'blocklist_text': []
            }
        }
    )

def get_blocklist(chat_id) -> list:
    blocklist_data = blocklists.find_one(
        {
            'chat_id': chat_id
        }
    )
    
    if blocklist_data is not None:
        BLOCKLIST = blocklist_data['blocklist_text']
        return BLOCKLIST

def get_blocklist_reason(chat_id, blocklist_text):
    blocklist_data = blocklists.find_one(
        {
            'chat_id': chat_id,
            'blocklist_text.blocklist_text': blocklist_text
        }
    )
    if blocklist_data is not None:
        blocklist_text_array = blocklist_data['blocklist_text']
        for bl_data in blocklist_text_array:
            bl_text = bl_data['blocklist_text']
            if bl_text == blocklist_text:
                blocklist_reason = bl_data['blocklist_reason']
                return blocklist_reason
        else:
            return None
    else:
        return Nones

def blocklistMessageDelete(chat_id, blocklistdelete):
    blocklist_data = blocklists.find_one(
        {
            'chat_id': chat_id
        }
    )

    if blocklist_data is not None:
        blocklists.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'blocklistdelete': blocklistdelete
                }
            },
            upsert=True
        )
    else:
        _id = blocklists.count_documents({}) + 1
        blocklists.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'blocklist_text': [],
                'blocklist_mode': {
                    'blocklist_mode': 1,
                    'blocklist_time': None
                },
                'blocklistdelete': True,
                'blocklist_default_reason': None 
            }
        )

def getblocklistMessageDelete(chat_id) -> bool:
    blocklist_data = blocklists.find_one(
        {
            'chat_id': chat_id
        }
    )
    if blocklist_data is not None:
        return blocklist_data['blocklistdelete']
    else:
        return True

def setblocklistmode(chat_id, blocklist_mode, blocklist_time=None):
    blocklist_data = blocklists.find_one(
        {
            'chat_id': chat_id
        }
    )

    if blocklist_data is not None:
        blocklists.update(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'blocklist_mode': {
                        'blocklist_mode': blocklist_mode,
                        'blocklist_time': blocklist_time
                    }
                }
            },
            upsert=True
        )
    else:
        _id = blocklists.count_documents({}) + 1
        blocklists.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'blocklist_text': [],
                'blocklist_mode': {
                    'blocklist_mode': blocklist_mode,
                    'blocklist_time': blocklist_time
                },
                'blocklistdelete': True,
                'blocklist_default_reason': None
            }
        )

def getblocklistmode(chat_id):
    blocklist_data = blocklists.find_one(
        {

            'chat_id': chat_id
        }
    )

    if blocklist_data is not None:
        blocklist_mode = blocklist_data['blocklist_mode']['blocklist_mode']
        blocklist_time = blocklist_data['blocklist_mode']['blocklist_time']
        blocklist_default_reason = blocklist_data['blocklist_default_reason']
        
        return (
            blocklist_mode,
            blocklist_time,
            blocklist_default_reason
        )

    else:
        blocklist_mode = 1
        blocklist_time = None
        blocklist_default_reason = None

        return (
            blocklist_mode,
            blocklist_time,
            blocklist_default_reason
        )

def setblocklistreason_db(chat_id, reason):
    blocklist_data = blocklists.find_one(
        {
            'chat_id': chat_id
        }
    )

    if blocklist_data is not None:
        blocklists.update_one(
            {
                'chat_id': chat_id
            },
            {
                '$set': {
                    'blocklist_default_reason': reason
                }
            },
            upsert=True
        ) 
    else:
        _id = blocklists.count_documents({}) + 1
        blocklists.insert_one(
            {
                '_id': _id,
                'chat_id': chat_id,
                'blocklist_text': [],
                'blocklist_mode': {
                    'blocklist_mode': 1,
                    'blocklist_time': None
                },
                'blocklistdelete': True,
                'blocklist_default_reason': reason
            }
        )

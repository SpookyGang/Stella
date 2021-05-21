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

filters = StellaDB.filters

def add_filter_db(chat_id: int, filter_name: str, content: str, text: str, data_type: int):
   filter_data = filters.find_one(
      {
         'chat_id': chat_id
      }
   )

   if filter_data is None:
      _id = filters.count_documents({}) + 1
      filters.insert_one(
         {
            '_id': _id,
            'chat_id': chat_id,
            'filters': [
               {
                  'filter_name': filter_name,
                  'content': content,
                  'text': text,
                  'data_type': data_type
               }
            ]
         }
      )
   
   else:
         FILTERS_NAME = get_filters_list(chat_id)
         if filter_name not in FILTERS_NAME:
            filters.update_one(
               {
                  'chat_id': chat_id
               },
               {
                  '$addToSet': {
                     'filters': {
                        'filter_name': filter_name,
                        'content': content,
                        'text': text,
                        'data_type': data_type
                     }
                  }
               },
               upsert=True
            )
         else:
            filters.update_one(
               {
                  'chat_id': chat_id,
                  'filters.filter_name': filter_name
               },
               {
                  '$set': {
                     'filters.$.filter_name': filter_name,
                     'filters.$.content': content,
                     'filters.$.text': text,
                     'filters.$.data_type': data_type
                  }
               }
            )

def stop_db(chat_id: int, filter_name:str):
   filters.update(
      {
         'chat_id': chat_id
      },
      {
         '$pull': {
            'filters': {
               'filter_name': filter_name
            }
         }
      }
   )

def stop_all_db(chat_id: id):
   filters.update(
      {
         'chat_id': chat_id
      },
      {
         '$set': {
            'filters': []
         }
      },
      upsert=True
   )
   
def get_filter(chat_id: int, filter_name: str):
   filter_data = filters.find_one(
      {
         'chat_id': chat_id
      }
   )
   if filter_data is not None:
      filters_ = filter_data['filters']
      for filter_ in filters_:
         if filter_['filter_name'] == filter_name:
            content = filter_['content']
            text = filter_['text']
            data_type = filter_['data_type']
            return (
               filter_name,
               content,
               text,
               data_type
            )

def get_filters_list(chat_id: int):
   filter_data = filters.find_one(
      {
         'chat_id': chat_id
      }
   )
   if filter_data is not None:
      FILTERS_NAME = list()
      for filter_name in filter_data['filters']:
         FILTERS_NAME.append(filter_name['filter_name'])
      return FILTERS_NAME
   else:
      return []
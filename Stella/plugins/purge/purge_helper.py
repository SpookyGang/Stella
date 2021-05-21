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


def PurgeDictDataUpdater(chat_id, purge_from=None, purge_to=None, first_messageID=None, purge_from_messageID=None):
    PurgeData = PurgeDictData.PurgeDict
    if purge_to == None:
        PurgeData.update(
            {
                chat_id: {
                    "purge_from": purge_from,
                    "first_messageID": first_messageID,
                    "purge_from_messageID": purge_from_messageID
                }
            }
        )
    elif purge_from == None:
        PurgeData[chat_id].update(
            {
                "purge_to": purge_to
            }
        )
    
    

class PurgeDictData:
    PurgeDict = dict()

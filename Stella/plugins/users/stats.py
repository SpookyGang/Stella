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

import datetime

from Stella import StellaDB

users = StellaDB.users
chats = StellaDB.chats

def __stats__():
    NUM_CHATS = chats.count_documents({})
    NUM_USERS = users.count_documents({})
    CHATS24HR = chats.count_documents({'first_found_date': {'$gte': datetime.datetime.now() - datetime.timedelta(days=1)}})
    USER24HR = users.count_documents({'first_found_date': {"$gte": datetime.datetime.now() - datetime.timedelta(days=1)}})
    
    text = (
        f"I've seen `{NUM_USERS}` users in total and have joined `{NUM_CHATS}` chats.\n"
        f"- Eto~ I saw `{USER24HR}`  users and `{CHATS24HR}` chats in the last 24 hours, heh.\n"
    )
    return text

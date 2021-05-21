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

warnings = StellaDB.warnings

def __stats__():
    TOTAL_WARNINGS = []
    TOTAL_WARNED_USER = []
    TOTAL_CHATS = warnings.count_documents({})

    warning_data = warnings.find({})
    for chat_data in warning_data:
        warns = chat_data['warns']
        TOTAL_WARNED_USER.append(len(warns))
        for warn in warns:
            len_of_warn = len(warn['user_warns'])
            TOTAL_WARNINGS.append(len_of_warn)
    text = (
        f"Erm, they've received `{sum(TOTAL_WARNINGS)}` warnings by me- including total of `{sum(TOTAL_WARNED_USER)}` bad people (__idk for sure if they're bad tho but that's that heh__) in `{TOTAL_CHATS}` chats :p"
    )
    return text
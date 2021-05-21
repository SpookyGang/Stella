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

notes = StellaDB.notes

notes_data = notes.find({})

def __stats__():
    TOTAL_NOTES = []
    TOTAL_CHATS = notes.count_documents({})     

    notes_data = notes.find()
    for chat_notes in notes_data:
        num_of_notes = len(chat_notes['notes'])
        TOTAL_NOTES.append(num_of_notes)
    text = f"Minna has saved `{sum(TOTAL_NOTES)}` notes and the number of chats that have saved is `{TOTAL_CHATS}`.\n"
    return text
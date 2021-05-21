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

__mod_name__ = "Notes"

__help__ = (
    "Save data for future users with notes!\n\n"
    "Notes are great to save random tidbits of information; a phone number, a nice gif, a funny picture - anything!\n\n"
    "**User commands::**\n"
    "- /get `<notename>`: Get a note.\n"
    "- `#notename`: Same as /get.\n\n"
    "Admin commands:\n"
    "- /save `<notename> <note text>`: Save a new note called \"word\". Replying to a message will save that message. Even works on media!n\n"
    "- /clear `<notename>`: Delete the associated note.\n"
    "- /notes: List all notes in the current chat.\n"
    "- /saved: Same as `/notes`.\n"
    "- /clearall: Delete ALL notes in a chat. This cannot be undone.\n"
    "- /privatenotes: Whether or not to send notes in PM. Will send a message with a button which users can click to get the note in PM."
)
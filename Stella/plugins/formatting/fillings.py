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


__mod_name__ = "Fillings"

__hidden__ = True 

__help__ = """
You can also customise the contents of your message with contextual data. For example, you could mention a user by name in the welcome message, or mention them in a filter!

Supported fillings:
- `{first}`: The user's first name.
- `{last}`: The user's last name.
- `{fullname}`: The user's full name.
- `{username}`: The user's username. If they don't have one, mentions the user instead.
- `{mention}`: Mentions the user with their firstname.
- `{id}`: The user's ID.
- `{chatname}`: The chat's name.
- `{rules}`: Create a button to the chat's rules.
- `{preview}`: Enables link previews for this message. Useful when using links to Instant View pages.

Example usages:
- Save a filter using the user's name.
-> `/filter test {first} triggered this filter.`
- Add a rules button to a note.
-> `/save info Press the button to read the chat rules! {rules}`
- Mention a user in the welcome message
-> `/setwelcome Welcome {mention} to {chatname}!`
"""

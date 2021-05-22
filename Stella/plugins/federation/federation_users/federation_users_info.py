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


__mod_name__ = "User Commands"

__hidden__ = True

__help__ = """
These commands do not require you to be admin of a federation. These commands are for general commands, such as looking up information on a fed, or checking a user's fbans.

**Commands:**
- /fedinfo `<FedID>`: Information about a federation.
- /fedadmins `<FedID>`: List the admins in a federation.
- /fedsubs `<FedID>`: List all federations your federation is subscribed to.
- /joinfed `<FedID>`: Join the current chat to a federation. A chat can only join one federation. Chat owners only.
- /leavefed: Leave the current federation. Only chat owners can do this.
- /fedstat: List all the federations you are banned in.
- /fedstat `<user ID>`: List all the federations a user has been banned in.
- /fedstat `<user ID> <FedID>`: Gives information about a user's ban in a federation.
- /chatfed: Information about the federation the current chat is in.
- /quietfed `<yes/no/on/off>`: Whether or not to send ban notifications when fedbanned users join the chat.
"""

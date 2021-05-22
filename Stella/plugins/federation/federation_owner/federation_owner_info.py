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


__mod_name__ = "Federation Owner Commands"

__hidden__ = True

__help__ = """
These are the list of available fed owner commands. To run these, you have to own the current federation.

**Owner Commands:**
- /newfed `<fedname>`: Creates a new federation with the given name. Only one federation per user.
- /renamefed `<fedname>`: Rename your federation.
- /delfed: Deletes your federation, and any information related to it. Will not unban any banned users.
- /fedtransfer `<reply/username/mention/userid>`: Transfer your federation to another user.
- /fedpromote: Promote a user to fedadmin in your fed. To avoid unwanted fedadmin, the user will get a message to confirm this.
- /feddemote: Demote a federation admin in your fed.
- /fednotif `<yes/no/on/off>`: Whether or not to receive PM notifications of every fed action.
- /fedreason `<yes/no/on/off>`: Whether or not fedbans should require a reason.
- /subfed `<FedId>`: Subscribe your federation to another. Users banned in the subscribed fed will also be banned in this one.
Note: This does not affect your banlist. You just inherit any bans.
- /unsubfed `<FedId>`: Unsubscribes your federation from another. Bans from the other fed will no longer take effect.
- /fedexport `<csv/minicsv/json/human>`: Get the list of currently banned users. Default output is CSV.
- /fedimport: Import a list of banned users.
- /setfedlog: Sets the current chat as the federation log. All federation events will be logged here.
- /unsetfedlog: Unset the federation log. Events will no longer be logged.
"""

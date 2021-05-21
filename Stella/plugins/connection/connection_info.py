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


__mod_name__ = "Connections"

__help__ = (
    "This module allows you to connect my PM to your chat - you can easily change welcome settings/add notes/filters etc. without letting your members know about it. Obviously, you need to be an admin of the connected to perform such actions!\n\n"
    "**Command list:**\n\n"
    "• /connect - Do this in the chat you want to connect to and I'll send a button there which you can tap to get the chat connected, you can also use the chat's id. (Example: `/connect <id>`) - you'll execute this in my PM.\n\n"
    "• /disconnect - Disconnect my PM with the chat you connected.\n\n"
    "• /reconnect - I'll reconnect to the last chat you connected.\n\n"
    "• /connection - There are obviously some things that cannot be done when connected to PM, this will get you the list of all possible commands that can be executed when connected to PM.\n\n"
    "• /allowconnection - Enable this if you want to let your members connect and be able to view notes/filters, disable if you don't want them to. (Bool values: `yes/no/on/off`)"
)


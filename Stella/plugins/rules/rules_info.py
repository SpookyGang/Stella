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

__mod_name__ = "Rules"

__help__ = (
    "Every chat works with different rules; this module will help make those rules clearer!\n\n"
    "**User commands:**\n"
    "- /rules: Check the current chat rules.\n\n"
    "**Admin commands:**\n"
    "- /setrules `<text>`: Set the rules for this chat. Supports markdown, buttons, fillings, etc.\n"
    "- /privaterules `<yes/no/on/off>`: Enable/disable whether the rules should be sent in private.\n"
    "- /resetrules: Reset the chat rules to default.\n"
    "- /setrulesbutton: Set the rules button name when using {rules}.\n"
    "- /resetrulesbutton: Reset the rules button name from {rules} to default.\n"
)
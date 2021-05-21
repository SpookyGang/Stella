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


__mod_name__ = "Antiflood"

__help__ = (
    "You know how sometimes, people join, send 100 messages, and ruin your chat? With antiflood, that happens no more!\n\n"
    "Antiflood allows you to take action on users that send more than x messages in a row. Actions are: ban/kick/mute/tban/tmute\n\n"
    "**Admin commands:**\n"
    "- /flood: Get the current antiflood settings\n"
    "- /setflood `<number/off/no>`: Set the number of messages after which to take action on a user. Set to '0', 'off', or 'no' to disable.\n"
    "- /setfloodmode `<action type>`: Choose which action to take on a user who has been flooding. Options: ban/kick/mute/tban/tmute"
)